import guideme.libs.mdast.MdAst;
import guideme.libs.mdast.MdastOptions;
import guideme.libs.mdast.YamlFrontmatterExtension;
import guideme.libs.mdast.gfm.GfmTableMdastExtension;
import guideme.libs.mdast.gfmstrikethrough.GfmStrikethroughMdastExtension;
import guideme.libs.mdast.mdx.MdxMdastExtension;
import guideme.libs.mdx.MdxSyntax;
import guideme.libs.micromark.ParseException;
import guideme.libs.micromark.extensions.YamlFrontmatterSyntax;
import guideme.libs.micromark.extensions.gfm.GfmTableSyntax;
import guideme.libs.micromark.extensions.gfmstrikethrough.GfmStrikethroughSyntax;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

/** Syntax-only verification with the actual shaded parser from GuideME 21.1.19. */
public final class ValidateHandbookSyntax {
    private static MdastOptions options() {
        return new MdastOptions()
                .withSyntaxExtension(MdxSyntax.INSTANCE)
                .withSyntaxExtension(YamlFrontmatterSyntax.INSTANCE)
                .withSyntaxExtension(GfmTableSyntax.INSTANCE)
                .withSyntaxExtension(GfmStrikethroughSyntax.INSTANCE)
                .withMdastExtension(MdxMdastExtension.INSTANCE)
                .withMdastExtension(YamlFrontmatterExtension.INSTANCE)
                .withMdastExtension(GfmTableMdastExtension.INSTANCE)
                .withMdastExtension(GfmStrikethroughMdastExtension.INSTANCE);
    }

    private static void parse(String source) {
        MdAst.fromMarkdown(source.replaceAll("\\r\\n?", "\n"), options());
    }

    public static void main(String[] args) throws Exception {
        // Prove this harness catches genuine parser errors, not a permissive substitute.
        boolean caught = false;
        try {
            parse("<ItemLink id=\"minecraft:stone\">Unclosed link\n");
        } catch (ParseException expected) {
            caught = true;
            System.out.println("Negative control rejected: " + expected.getMessage());
        }
        if (!caught) {
            throw new AssertionError("Malformed native tag was accepted by the negative control");
        }
        parse("| Item | Use |\n| --- | --- |\n| Stone | Building |\n\n<ItemGrid>\n<ItemIcon id=\"minecraft:stone\" />\n</ItemGrid>\n\nUse <ItemLink id=\"minecraft:stone\">Stone</ItemLink> and <KeyBind id=\"key.jump\" />.\n");
        Path root = Path.of(args[0]).toAbsolutePath();
        int expectedCount = Integer.parseInt(args[1]);
        List<Path> pages;
        try (var stream = Files.walk(root)) {
            pages = stream.filter(Files::isRegularFile)
                    .filter(path -> path.getFileName().toString().endsWith(".md"))
                    .sorted().toList();
        }
        if (pages.size() != expectedCount) {
            throw new AssertionError("Expected " + expectedCount + " pages, found " + pages.size());
        }
        int failures = 0;
        for (Path page : pages) {
            try {
                parse(Files.readString(page));
                System.out.println("PASS " + root.relativize(page));
            } catch (ParseException failure) {
                failures++;
                System.err.println("FAIL " + root.relativize(page) + ": " + failure.getMessage());
            }
        }
        System.out.println("GuideME 21.1.19 MdAst syntax: " + pages.size() + " pages, " + failures + " parse failures.");
        if (failures != 0) {
            throw new AssertionError("Handbook syntax failures: " + failures);
        }
    }
}
