package dev.astropunk.handbook;

import dev.emi.emi.api.EmiApi;
import net.minecraft.client.Minecraft;
import net.minecraft.client.gui.screens.Screen;
import net.minecraft.client.gui.screens.inventory.CreativeModeInventoryScreen;
import net.minecraft.client.gui.screens.inventory.InventoryScreen;
import net.minecraft.client.player.LocalPlayer;
import net.minecraft.network.chat.Component;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.flag.FeatureFlagSet;
import net.neoforged.fml.ModList;

/** EMI classes are resolved only after the optional mod-presence guard. */
public final class EmiQueryClient {
    private EmiQueryClient() {}
    public static void open(String query) {
        var minecraft = Minecraft.getInstance();
        if (minecraft.player == null) return;
        if (!ModList.get().isLoaded("emi")) {
            minecraft.player.displayClientMessage(Component.literal("EMI is not installed. Search: " + query), true);
            return;
        }
        Present.open(minecraft, query);
    }
    private static final class Present {
        static void open(Minecraft minecraft, String query) {
            Screen guide = minecraft.screen;
            // Select the native creative screen directly. InventoryScreen.init would
            // redirect creative players to a new screen without our close callback.
            Screen inventory = minecraft.gameMode.hasInfiniteItems()
                    ? new QueryCreativeInventoryScreen(minecraft.player,
                            minecraft.player.connection.enabledFeatures(),
                            minecraft.options.operatorItemsTab().get(), guide)
                    : new QueryInventoryScreen(minecraft.player, guide);
            minecraft.setScreen(inventory);
            // The selected public setter only changes search, so initialize the native screen first.
            EmiApi.setSearchText(query);
        }
    }
    // Native screens own all rendering, recipe book, input and inventory lifecycle.
    // A later game-mode change may trigger their normal redirect and lose the return target.
    static final class QueryInventoryScreen extends InventoryScreen {
        private final Screen returnScreen;
        QueryInventoryScreen(Player player, Screen returnScreen) {
            super(player);
            this.returnScreen = returnScreen;
        }
        @Override public void onClose() {
            super.onClose();
            Minecraft.getInstance().setScreen(returnScreen);
        }
    }
    static final class QueryCreativeInventoryScreen extends CreativeModeInventoryScreen {
        private final Screen returnScreen;
        QueryCreativeInventoryScreen(LocalPlayer player, FeatureFlagSet features, boolean operatorItemsTab, Screen returnScreen) {
            super(player, features, operatorItemsTab);
            this.returnScreen = returnScreen;
        }
        @Override public void onClose() {
            super.onClose();
            Minecraft.getInstance().setScreen(returnScreen);
        }
    }
}
