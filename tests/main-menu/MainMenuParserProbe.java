import java.nio.file.*;
import de.keksuccino.fancymenu.util.properties.*;
import de.keksuccino.konkrete.config.Config;

/** Headless probe of the selected released parsers, not a Minecraft startup. */
public class MainMenuParserProbe {
    private static void require(boolean condition, String message) {
        if (!condition) throw new AssertionError(message);
    }
    public static void main(String[] args) throws Exception {
        Path root = Path.of(args[0]);
        var screens = PropertiesParser.deserializeSetFromFancyString(Files.readString(root.resolve("config/fancymenu/customizablemenus.txt")));
        require(screens != null && screens.getType().equals("customizablemenus"), "screen list type");
        require(screens.getContainers().size() == 1 && screens.getContainers().getFirst().getType().equals("net.minecraft.client.gui.screens.TitleScreen"), "main menu only");
        var layout = PropertiesParser.deserializeSetFromFancyString(Files.readString(root.resolve("config/fancymenu/customization/astropunk-title.txt")));
        require(layout != null && layout.getType().equals("fancymenu_layout"), "layout type");
        require(layout.getContainersOfType("menu_background").size() == 1, "only one background per builder is consumed");
        require(layout.getContainersOfType("element").size() == 2, "shade and separate title");
        var meta = layout.getFirstContainerOfType("layout-meta");
        require(meta.getValue("identifier").equals("net.minecraft.client.gui.screens.TitleScreen"), "target screen");
        require(meta.getValue("render_custom_elements_behind_vanilla").equals("true"), "shade must not cover native controls");
        for (var c : layout.getContainersOfType("vanilla_button")) {
            require(c.getValue("instance_identifier").matches("minecraft_(logo|splash)_widget"), "functional widgets must remain unchanged");
            require(c.getValue("is_hidden").equals("true"), "hide old branding");
        }
        for (var c : layout.getContainers()) {
            for (var key : new String[]{"source", "image_path"}) {
                String value = c.getValue(key);
                if (value != null) {
                    require(value.startsWith("[source:local]/config/fancymenu/assets/"), "local pack assets only");
                    require(Files.isRegularFile(root.resolve(value.substring("[source:local]/".length()))), "asset exists");
                }
            }
        }
        String serialized = PropertiesParser.serializeSetToFancyString(layout);
        var roundTrip = PropertiesParser.deserializeSetFromFancyString(serialized);
        require(roundTrip != null && roundTrip.getContainers().size() == layout.getContainers().size(), "round trip");
        require(PropertiesParser.deserializeSetFromFancyString("missing type") == null, "negative control");
        var options = new Config(root.resolve("configureddefaults/config/fancymenu/options.txt").toString());
        require(!options.getBoolean("show_customization_overlay"), "hide editor toolbar by default");
        System.out.println("PASS released FancyMenu 3.9.14 parser, round trip, negative control, menu scope, local assets and Konkrete 1.9.9 options parser");
    }
}
