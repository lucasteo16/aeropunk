import guideme.*;
import guideme.color.SymbolicColor;
import guideme.compiler.*;
import guideme.compiler.tags.*;
import guideme.document.block.*;
import guideme.document.flow.*;
import guideme.extensions.ExtensionCollection;
import guideme.indices.*;
import guideme.libs.mdast.mdx.model.*;
import guideme.libs.mdast.model.*;
import guideme.libs.unist.UnistNode;
import guideme.navigation.NavigationTree;
import guideme.scene.ItemImageTagCompiler;
import java.nio.file.*;
import java.util.*;
import net.minecraft.resources.ResourceLocation;

/** Selected-release PageCompiler layout-tree checks, not rendering or pack registry checks. */
public final class VerifyNativeItemGrid {
    static final class Pages implements PageCollection {
        final ItemIndex items = new ItemIndex();
        @SuppressWarnings("unchecked") public <T extends PageIndex> T getIndex(Class<T> clazz) { return (T) items; }
        public Collection<ParsedGuidePage> getPages() { return List.of(); }
        public ParsedGuidePage getParsedPage(ResourceLocation id) { return null; }
        public GuidePage getPage(ResourceLocation id) { return null; }
        public byte[] loadAsset(ResourceLocation id) { return null; }
        public NavigationTree getNavigationTree() { return null; }
        public boolean pageExists(ResourceLocation id) { return true; }
    }
    /** Deliberate boundaries, counted and reported, never called native validation. */
    static final class RuntimeBoundary extends FlowTagCompiler {
        public Set<String> getTagNames() { return Set.of("Recipe", "KeyBind"); }
        protected void compile(PageCompiler compiler, LytFlowParent parent, MdxJsxElementFields el) {
            parent.appendText("[runtime boundary " + el.name() + "]");
        }
    }
    static final class Result {
        final List<String> errors = new ArrayList<>();
        final Map<String,Integer> tags = new TreeMap<>();
        int grids, slots, itemLabels, expectedGrids, expectedSlots, expectedLabels;
    }
    static void normalize(UnistNode node, Result result, boolean insideGrid) {
        if (node instanceof MdAstText text && text.value.startsWith("Failed to parse GuideME page")) result.errors.add(text.value);
        if (node instanceof MdxJsxElementFields el) {
            result.tags.merge(el.name(), 1, Integer::sum);
            if (el.name().equals("ItemGrid")) result.expectedGrids++;
            if (el.name().equals("ItemIcon") && insideGrid) result.expectedSlots++;
            if (el.name().equals("ItemLink")) result.expectedLabels++;
            if (Set.of("ItemIcon", "ItemLink", "ItemImage").contains(el.name())) {
                // Only the item-registry boundary is normalized. AST whitespace, child nodes,
                // original positions, tag kind and compiler dispatch remain untouched.
                var attr = el.getAttribute("id");
                if (attr != null && attr.hasStringValue()) {
                    ResourceLocation.parse(attr.getStringValue());
                    attr.setValue("minecraft:stone");
                }
            }
        }
        if (node instanceof MdAstParent<?> parent) {
            boolean grid = node instanceof MdxJsxElementFields el && el.name().equals("ItemGrid");
            for (var child : parent.children()) normalize(child, result, grid);
        }
    }
    static Result compile(String source) {
        var result = new Result();
        var id = ResourceLocation.fromNamespaceAndPath("astropunk", "probe.md");
        var parsed = PageCompiler.parse("markup-probe", "en_us", id, source);
        normalize(parsed.getAstRoot(), result, false);
        var extensions = ExtensionCollection.builder()
            .add(TagCompiler.EXTENSION_POINT, new ItemGridCompiler())
            .add(TagCompiler.EXTENSION_POINT, new ItemLinkCompiler())
            .add(TagCompiler.EXTENSION_POINT, new ItemImageTagCompiler())
            .add(TagCompiler.EXTENSION_POINT, new ColorTagCompiler())
            .add(TagCompiler.EXTENSION_POINT, new dev.astropunk.handbook.EmiSearchTagCompiler(query -> {}))
            .add(TagCompiler.EXTENSION_POINT, new RuntimeBoundary()).build();
        var document = PageCompiler.compile(new Pages(), extensions, parsed).document();
        document.visit(new LytVisitor() {
            public Result beforeNode(LytNode node) {
                if (node instanceof LytItemGrid) result.grids++;
                if (node instanceof LytSlot) result.slots++;
                return Result.CONTINUE;
            }
            public Result beforeFlowContent(LytFlowContent node) {
                if (node instanceof LytTooltipSpan tooltip && tooltip.getTooltip(0, 0).orElse(null) instanceof guideme.document.interaction.ItemTooltip) result.itemLabels++;
                if (node instanceof LytFlowSpan span && span.getStyle().color() == SymbolicColor.ERROR_TEXT) {
                    var text = new StringBuilder();
                    span.visit(new LytVisitor() { public void text(String value) { text.append(value); } });
                    result.errors.add(text.toString());
                }
                return Result.CONTINUE;
            }
        });
        return result;
    }
    static void check(boolean condition, String message) { if (!condition) throw new AssertionError(message); }
    static void controls() {
        String icon = "<ItemIcon id=\"minecraft:stone\" />";
        var standalone = compile("<ItemGrid>\n  " + icon + "\n  " + icon + "\n</ItemGrid>\n");
        check(standalone.errors.isEmpty() && standalone.grids == 1 && standalone.slots == 2, "Standalone multiline grid failed");
        var compact = compile("| Label | Items |\n| --- | --- |\n| Stone | <ItemGrid>" + icon + "</ItemGrid> <ItemLink id=\"minecraft:stone\" /> |\n");
        check(compact.errors.isEmpty() && compact.grids == 1 && compact.slots == 1 && compact.itemLabels == 1, "Compact table grid failed or swallowed its sibling ItemLink");
        var spaced = compile("| Label | Items |\n| --- | --- |\n| Stone | <ItemGrid> " + icon + " </ItemGrid> <ItemLink id=\"minecraft:stone\" /> |\n");
        check(spaced.errors.size() == 2 && spaced.slots == 1 && spaced.itemLabels == 1, "Whitespace control must report two text children while preserving icon and sibling label");
        for (String child : List.of(" " + icon + " ", "text", "<ItemLink id=\"minecraft:stone\" />", "**text**")) {
            var malformed = compile("| Label | Items |\n| --- | --- |\n| Stone | <ItemGrid>" + child + "</ItemGrid> |\n");
            check(malformed.errors.stream().anyMatch(e -> e.contains("Unsupported child-element in ItemGrid")), "Malformed child was accepted: " + child);
            System.out.println("NEGATIVE " + child + " " + malformed.errors);
        }
        var missing = compile("<ItemGrid>\n<ItemIcon />\n</ItemGrid>\n");
        check(missing.errors.stream().anyMatch(e -> e.contains("Missing id attribute")), "Missing icon id was accepted");
        var badColor = compile("Type <Color color=\"#abc\">stone</Color>.");
        check(!badColor.errors.isEmpty(), "Invalid native Color was accepted");
        var badSyntax = compile("<ItemGrid>\n<ItemIcon id=\"minecraft:stone\" />\n");
        check(!badSyntax.tags.containsKey("ItemGrid"), "Unclosed grid survived parsing");
        System.out.println("CONTROLS passed: multiline block, compact table, whitespace and illegal children, missing id, Color, unclosed tag");
    }
    public static void main(String[] args) throws Exception {
        net.minecraft.SharedConstants.tryDetectVersion();
        net.minecraft.server.Bootstrap.bootStrap();
        controls();
        int pages = 0, failures = 0, grids = 0, slots = 0, labels = 0;
        Map<String,Integer> tags = new TreeMap<>();
        List<Path> files;
        try (var stream = Files.walk(Path.of(args[0]))) {
            files = stream.filter(p -> p.toString().endsWith(".md")).sorted().toList();
        }
        check(files.size() == Integer.parseInt(args[1]), "Unexpected page count: " + files.size());
        for (var file : files) {
            var result = compile(Files.readString(file));
            pages++; grids += result.grids; slots += result.slots; labels += result.itemLabels;
            result.tags.forEach((key, count) -> tags.merge(key, count, Integer::sum));
            if (!result.errors.isEmpty() || result.grids != result.expectedGrids || result.slots != result.expectedSlots || result.itemLabels != result.expectedLabels) {
                failures++;
                System.out.println("FAIL " + file + " grids " + result.grids + "/" + result.expectedGrids + " slots " + result.slots + "/" + result.expectedSlots + " errors " + result.errors.size());
                for (var error : result.errors) System.out.println("COMPILER_ERROR " + error);
            } else System.out.println("PASS " + file + " grids " + result.grids + " slots " + result.slots);
        }
        System.out.println("SUMMARY pages " + pages + " failing_pages " + failures + " grids " + grids + " slots " + slots + " tooltip_labels " + labels + " tags " + tags);
        System.out.println("BOUNDARIES item ids normalized to vanilla stone, empty item index, absent image assets, Recipe and KeyBind not compiled, no rendering or pack registry claims");
        check(failures == 0, "Native structural compiler failures: " + failures);
    }
}
