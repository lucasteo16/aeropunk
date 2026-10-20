package dev.astropunk.website;

import guideme.web.CustomElementWebRenderer;
import guideme.web.CustomElementWebRenderingContext;
import guideme.web.html.HtmlNode;
import java.util.Set;
import java.util.function.Consumer;

/** This is intentionally plain text, never a browser button claiming to open the game. */
public final class EmiSearchWebFallback implements CustomElementWebRenderer {
    public record Attributes(String query) {}
    @Override public Set<String> getTagNames() { return Set.of("EmiSearch"); }
    @Override public void render(CustomElementWebRenderingContext context, Consumer<HtmlNode> output) {
        var attributes = context.map(Attributes.class);
        output.accept(HtmlNode.tag("span").setAttribute("class", "game-only-search")
                .setAttribute("title", "Recipe browser search is available only in the game")
                .append(attributes.query() + " (game-only search)"));
    }
}
