package dev.astropunk.handbook;

import dev.emi.emi.api.EmiApi;
import net.minecraft.client.Minecraft;
import net.minecraft.client.gui.screens.Screen;
import net.minecraft.client.gui.GuiGraphics;
import net.minecraft.client.gui.screens.inventory.AbstractContainerScreen;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.inventory.InventoryMenu;
import net.minecraft.network.chat.Component;
import net.minecraft.world.entity.player.Player;
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
            minecraft.setScreen(new QueryInventoryScreen(minecraft.player, guide));
            // setScreen initializes the handled inventory first; EMI search mutation does not open a screen.
            EmiApi.setSearchText(query);
        }
    }
    // Do not subclass InventoryScreen: it redirects creative players to a different
    // screen during init, losing our return-to-guide callback.
    static final class QueryInventoryScreen extends AbstractContainerScreen<InventoryMenu> {
        private static final ResourceLocation BACKGROUND = ResourceLocation.withDefaultNamespace("textures/gui/container/inventory.png");
        private final Screen returnScreen;
        QueryInventoryScreen(Player player, Screen returnScreen) {
            super(player.inventoryMenu, player.getInventory(), Component.translatable("container.inventory"));
            this.returnScreen = returnScreen;
            titleLabelY = 6;
        }
        @Override protected void renderBg(GuiGraphics graphics, float partialTick, int mouseX, int mouseY) {
            graphics.blit(BACKGROUND, leftPos, topPos, 0, 0, imageWidth, imageHeight);
        }
        @Override public void render(GuiGraphics graphics, int mouseX, int mouseY, float partialTick) {
            super.render(graphics, mouseX, mouseY, partialTick);
            renderTooltip(graphics, mouseX, mouseY);
        }
        @Override public void onClose() { Minecraft.getInstance().setScreen(returnScreen); }
    }
}
