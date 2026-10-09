package dev.astropunk.handbook;

import guideme.Guide;
import guideme.Guides;
import guideme.color.ConstantColor;
import guideme.compiler.PageCompiler;
import guideme.compiler.TagCompiler;
import guideme.document.block.LytParagraph;
import guideme.document.flow.LytFlowContent;
import guideme.document.flow.LytFlowLink;
import guideme.document.flow.LytFlowParent;
import guideme.document.flow.LytFlowText;
import guideme.libs.unist.UnistNode;
import java.util.ArrayList;
import java.util.List;
import net.minecraft.resources.ResourceLocation;

/** Executes released GuideME builder, registry, parser, compiler dispatch and link click without a window. */
public final class VerifyEmiSearch {
    static final class Sink implements LytFlowParent {
        final List<LytFlowContent> children = new ArrayList<>();
        final List<String> errors = new ArrayList<>();
        public void append(LytFlowContent node) { children.add(node); }
        public void appendError(PageCompiler compiler, String text, UnistNode node) { errors.add(text); }
    }
    static void check(boolean ok, String message) { if (!ok) throw new AssertionError(message); }
    static Sink compile(Guide guide, String markup) {
        var id = ResourceLocation.fromNamespaceAndPath("astropunk", "query-probe.md");
        String source = "Before " + markup + " after.";
        var parsed = PageCompiler.parse("query-probe", "en_us", id, source);
        var compiler = new PageCompiler(guide, guide.getExtensions(), "query-probe", id, source);
        var sink = new Sink();
        compiler.compileFlowContext((guideme.libs.mdast.model.MdAstParagraph) parsed.getAstRoot().children().getFirst(), sink);
        return sink;
    }
    public static void main(String[] args) {
        List<String> clicks = new ArrayList<>();
        var extension = new EmiSearchTagCompiler(clicks::add);
        var id = ResourceLocation.fromNamespaceAndPath("astropunk", "query-probe");
        var guide = HandbookQueryGuide.withQueries(Guide.builder(id).disableDefaultExtensions(), extension).build();
        check(Guides.getById(id) == guide, "Public builder failed registry registration");
        check(guide.getExtensions().get(TagCompiler.EXTENSION_POINT).contains(extension), "Missing registered tag compiler");
        System.out.println("PASS actual Guide.builder extension registration and Guides.getById");
        for (String query : List.of("@creeperoverhaul", "@create", "@createaddition", "@\"Farmer's Delight\"", "@机械动力", "@create | @minecraft")) {
            var sink = compile(guide, "<EmiSearch query='" + query.replace("'", "&#39;") + "' />");
            check(sink.errors.isEmpty(), sink.errors.toString());
            var link = (LytFlowLink) sink.children.get(1);
            check(((LytFlowText) link.getChildren().getFirst()).getText().equals(query), "Query not preserved");
            check(((ConstantColor) link.getStyle().color()).lightModeColor() == 0xffF28CBD, "Not pink");
            check(Boolean.FALSE.equals(link.getStyle().italic()), "Query italicized");
            link.setClickSound(null); // Audio requires the client. Callback uses native released click handling.
            check(!link.mouseClicked(null, 0, 0, 1), "Right click should not execute");
            check(link.mouseClicked(null, 0, 0, 0), "Left click not handled");
            check(clicks.getLast().equals(query), "Click query changed");
            System.out.println("PASS native parser, dispatch, pink label and click " + query);
        }
        var label = (LytFlowLink) compile(guide, "<EmiSearch query=\"@create\">Browse Create</EmiSearch>").children.get(1);
        check(((LytFlowText) label.getChildren().getFirst()).getText().equals("Browse Create"), "Custom label lost");
        System.out.println("PASS custom label");
        for (String markup : List.of("<EmiSearch />", "<EmiSearch query=\"\" />", "<EmiSearch query=\"   \" />", "<EmiSearch query={\"@create\"} />")) {
            check(!compile(guide, markup).errors.isEmpty(), "Malformed query accepted " + markup);
            System.out.println("PASS rejects " + markup);
        }
        // Full page compilation proves the block-context adapter too.
        var pageId = ResourceLocation.fromNamespaceAndPath("astropunk", "block.md");
        var page = PageCompiler.compile(guide, guide.getExtensions(), PageCompiler.parse("query-probe", "en_us", pageId, "<EmiSearch query=\"@create\" />"));
        check(page.document().getChildren().getFirst() instanceof LytParagraph, "Block adapter missing");
        var paragraph = (LytParagraph) page.document().getChildren().getFirst();
        check(paragraph.getContent().iterator().next() instanceof LytFlowLink, "Block did not compile into native link");
        System.out.println("PASS full native page compilation and block-context adapter");
        var missing = Guide.builder(ResourceLocation.fromNamespaceAndPath("astropunk", "no-extension")).disableDefaultExtensions().register(false).build();
        check(compile(missing, "<EmiSearch query=\"@create\" />").children.stream().noneMatch(node -> node instanceof LytFlowLink), "Disconnected registration negative control failed");
        System.out.println("PASS disconnected-extension negative control");
        var production = HandbookQueryGuide.register();
        check(((guideme.internal.MutableGuide) production).getItemSettings().displayName().orElseThrow().getString().equals("Astropunk Handbook"), "Existing handbook display name not preserved");
        check(Guides.getById(production.getId()) == production, "Production guide not registered");
        check(production.getExtensions().get(TagCompiler.EXTENSION_POINT).stream().anyMatch(t -> t instanceof EmiSearchTagCompiler), "Production extension missing");
        System.out.println("PASS production registration with native default extensions retained");
        var override = Guide.builder(production.getId()).register(false).build();
        guideme.internal.GuideRegistry.setDataDriven(java.util.Map.of(production.getId(), (guideme.internal.MutableGuide) override));
        check(Guides.getById(production.getId()) == override, "Expected same-id resource guide to override static registration");
        check(override.getExtensions().get(TagCompiler.EXTENSION_POINT).stream().noneMatch(t -> t instanceof EmiSearchTagCompiler), "JSON override should lack custom extension");
        guideme.internal.GuideRegistry.setDataDriven(java.util.Map.of());
        check(Guides.getById(production.getId()) == production, "Static registration not restored after removing override");
        System.out.println("PASS same-id data-driven override negative control and restoration");
    }
}
