import guideme.color.ColorValue;
import guideme.color.ConstantColor;
import guideme.compiler.PageCompiler;
import guideme.compiler.TagCompiler;
import guideme.compiler.tags.ColorTagCompiler;
import guideme.document.flow.LytFlowContent;
import guideme.document.flow.LytFlowParent;
import guideme.document.flow.LytFlowSpan;
import guideme.extensions.ExtensionCollection;
import guideme.libs.mdast.mdx.model.MdxJsxTextElement;
import guideme.libs.mdast.model.MdAstParagraph;
import guideme.libs.unist.UnistNode;
import java.util.ArrayList;
import java.util.List;
import net.minecraft.resources.ResourceLocation;

/** Runs the selected parser and Color compiler, without a game or window. */
public final class VerifyNativeColor {
    static final class Sink implements LytFlowParent {
        final List<LytFlowContent> children = new ArrayList<>();
        final List<String> errors = new ArrayList<>();
        public void append(LytFlowContent node) { children.add(node); }
        public void appendError(PageCompiler compiler, String text, UnistNode node) { errors.add(text); }
    }
    static Sink compile(String attributes) {
        String source = "Type <Color " + attributes + ">/guidemec open astropunk:handbook @create</Color> now.";
        var id = ResourceLocation.fromNamespaceAndPath("astropunk", "probe.md");
        var parsed = PageCompiler.parse("probe", "en_us", id, source);
        var paragraph = (MdAstParagraph) parsed.getAstRoot().children().getFirst();
        var element = (MdxJsxTextElement) paragraph.children().get(1);
        var extensions = ExtensionCollection.builder().add(TagCompiler.EXTENSION_POINT, new ColorTagCompiler()).build();
        var compiler = new PageCompiler(null, extensions, "probe", id, source);
        var sink = new Sink();
        new ColorTagCompiler().compileFlowContext(compiler, sink, element);
        return sink;
    }
    static void check(boolean value, String message) {
        if (!value) throw new AssertionError(message);
    }
    static void valid(String attributes, int expected) {
        var result = compile(attributes);
        check(result.errors.isEmpty(), result.errors.toString());
        check(result.children.size() == 1, "Expected a styled span");
        var span = (LytFlowSpan) result.children.getFirst();
        var color = (ConstantColor) span.getStyle().color();
        check(color.lightModeColor() == expected, attributes + " had unexpected packed color");
        check(span.getStyle().italic() == null, "Color must not introduce italics");
        check(span.getChildren().size() == 1 && ((guideme.document.flow.LytFlowText) span.getChildren().getFirst()).getText().equals("/guidemec open astropunk:handbook @create"), "Typed command and query text changed");
        System.out.println("PASS " + attributes);
    }
    public static void main(String[] args) {
        valid("color=\"#123456\"", 0xff123456);
        valid("color=\"#80123456\"", 0x80123456);
        valid("color=\"transparent\"", 0);
        var named = compile("id=\"gold\"");
        check(named.errors.isEmpty() && named.children.size() == 1, "Symbolic color rejected");
        check(((LytFlowSpan) named.children.getFirst()).getStyle().color() != null, "Missing symbolic color");
        System.out.println("PASS symbolic gold");
        for (String attributes : List.of("color=\"#abc\"", "color=\"red\"", "color={\"#123456\"}", "style=\"color: red\"", "id=\"missing_color\"", "id=\"missing_color\" color=\"#123456\"")) {
            var result = compile(attributes);
            check(!result.errors.isEmpty(), "Invalid color accepted: " + attributes);
            System.out.println("REJECT " + attributes + " " + result.errors);
        }
        System.out.println("Native color parser and compiler checks passed.");
    }
}
