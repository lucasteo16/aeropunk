package dev.astropunk.handbook;

import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Properties;

final class LiveEditing {
    static final String SOURCES = "guideme.astropunk.handbook.sources";
    static final String NAMESPACE = "guideme.astropunk.handbook.sourcesNamespace";

    private LiveEditing() {}

    static void configure(Path gameDirectory, Properties properties) {
        Path preview = gameDirectory.resolve("resourcepacks/astropunk-guide-preview");
        Path sources = preview.resolve("assets/astropunk/guides/astropunk/handbook");
        if (Files.isSymbolicLink(preview) && Files.isDirectory(sources)) {
            properties.putIfAbsent(SOURCES, sources.toAbsolutePath().toString());
            properties.putIfAbsent(NAMESPACE, "astropunk");
        }
    }
}
