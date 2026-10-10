package dev.astropunk.handbook;

import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Properties;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.io.TempDir;
import static org.junit.jupiter.api.Assertions.*;

class LiveEditingTest {
    @TempDir Path root;

    @Test void symbolicPreviewEnablesNativeSources() throws Exception {
        Path source = Files.createDirectories(root.resolve("source/assets/astropunk/guides/astropunk/handbook"));
        Path packs = Files.createDirectories(root.resolve("game/resourcepacks"));
        Files.createSymbolicLink(packs.resolve("astropunk-guide-preview"), root.resolve("source"));
        Properties properties = new Properties();
        LiveEditing.configure(root.resolve("game"), properties);
        assertEquals(packs.resolve("astropunk-guide-preview/assets/astropunk/guides/astropunk/handbook").toAbsolutePath().toString(), properties.getProperty(LiveEditing.SOURCES));
        assertEquals("astropunk", properties.getProperty(LiveEditing.NAMESPACE));
        assertTrue(Files.isDirectory(source));
    }

    @Test void ordinaryExportDoesNotEnableEditing() throws Exception {
        Files.createDirectories(root.resolve("resourcepacks/astropunk-guide-preview/assets/astropunk/guides/astropunk/handbook"));
        Properties properties = new Properties();
        LiveEditing.configure(root, properties);
        assertTrue(properties.isEmpty());
    }

    @Test void explicitOverrideIsPreserved() throws Exception {
        Files.createDirectories(root.resolve("source/assets/astropunk/guides/astropunk/handbook"));
        Files.createDirectories(root.resolve("game/resourcepacks"));
        Files.createSymbolicLink(root.resolve("game/resourcepacks/astropunk-guide-preview"), root.resolve("source"));
        Properties properties = new Properties();
        properties.setProperty(LiveEditing.SOURCES, "explicit-source");
        properties.setProperty(LiveEditing.NAMESPACE, "explicit-namespace");
        LiveEditing.configure(root.resolve("game"), properties);
        assertEquals("explicit-source", properties.getProperty(LiveEditing.SOURCES));
        assertEquals("explicit-namespace", properties.getProperty(LiveEditing.NAMESPACE));
    }

    @Test void brokenSymbolicPreviewDoesNotEnableEditing() throws Exception {
        Files.createDirectories(root.resolve("resourcepacks"));
        Files.createSymbolicLink(root.resolve("resourcepacks/astropunk-guide-preview"), root.resolve("missing"));
        Properties properties = new Properties();
        LiveEditing.configure(root, properties);
        assertTrue(properties.isEmpty());
    }
}
