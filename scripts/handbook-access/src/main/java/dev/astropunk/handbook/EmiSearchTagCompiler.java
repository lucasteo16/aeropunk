package dev.astropunk.handbook;

import guideme.color.ConstantColor;
import guideme.compiler.PageCompiler;
import guideme.compiler.tags.FlowTagCompiler;
import guideme.compiler.tags.MdxAttrs;
import guideme.document.flow.LytFlowLink;
import guideme.document.flow.LytFlowParent;
import guideme.document.flow.LytFlowText;
import guideme.libs.mdast.mdx.model.MdxJsxElementFields;
import java.util.Set;
import java.util.function.Consumer;

/** Native GuideME component, not a URL or a command. */
public final class EmiSearchTagCompiler extends FlowTagCompiler {
    private final Consumer<String> openSearch;

    public EmiSearchTagCompiler() { this(EmiQueryClient::open); }
    public EmiSearchTagCompiler(Consumer<String> openSearch) { this.openSearch = openSearch; }
    @Override public Set<String> getTagNames() { return Set.of("EmiSearch"); }

    @Override protected void compile(PageCompiler compiler, LytFlowParent parent, MdxJsxElementFields element) {
        String query = MdxAttrs.getString(compiler, parent, element, "query", null);
        if (query == null || query.isBlank()) {
            parent.appendError(compiler, "EmiSearch requires a nonblank quoted query", element);
            return;
        }
        var link = new LytFlowLink();
        link.modifyStyle(style -> style.color(new ConstantColor(0xffF28CBD)).italic(false));
        link.setClickCallback(host -> openSearch.accept(query));
        parent.append(link);
        if (element.children().isEmpty()) {
            link.append(LytFlowText.of(query));
        } else {
            compiler.compileFlowContext(element.children(), link);
        }
    }
}
