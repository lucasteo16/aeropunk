package dev.astropunk.handbook;

import org.lwjgl.glfw.GLFW;
import com.mojang.blaze3d.platform.InputConstants;
import guideme.Guides;
import guideme.internal.GuideMEClient;
import java.util.ArrayList;
import net.minecraft.client.KeyMapping;
import net.minecraft.client.Minecraft;
import net.minecraft.client.gui.components.AbstractWidget;
import net.minecraft.client.gui.components.Button;
import net.minecraft.client.gui.components.Tooltip;
import net.minecraft.client.gui.screens.inventory.AbstractContainerScreen;
import net.minecraft.client.gui.screens.inventory.CreativeModeInventoryScreen;
import net.minecraft.client.gui.screens.inventory.InventoryScreen;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.ResourceLocation;
import net.neoforged.api.distmarker.Dist;
import net.neoforged.bus.api.IEventBus;
import net.neoforged.fml.common.Mod;
import net.neoforged.fml.loading.FMLPaths;
import net.neoforged.neoforge.client.event.ClientTickEvent;
import net.neoforged.neoforge.client.event.RegisterKeyMappingsEvent;
import net.neoforged.neoforge.client.event.ScreenEvent;
import net.neoforged.neoforge.common.NeoForge;
import net.neoforged.neoforge.client.settings.KeyConflictContext;

@Mod(value = HandbookAccess.MOD_ID, dist = Dist.CLIENT)
public final class HandbookAccess {
    static final String MOD_ID = "astropunk_handbook_access";
    private static final ResourceLocation HANDBOOK = ResourceLocation.fromNamespaceAndPath("astropunk", "handbook");
    private final KeyMapping shortcut;

    public HandbookAccess(IEventBus modBus) {
        // GuideBuilder reads these properties during the later first resource reload.
        LiveEditing.configure(FMLPaths.GAMEDIR.get(), System.getProperties());
        shortcut = new KeyMapping("key.astropunk_handbook_access.open", KeyConflictContext.UNIVERSAL,
                InputConstants.Type.KEYSYM, GLFW.GLFW_KEY_F9, "key.categories.astropunk_handbook_access");
        modBus.addListener(this::registerKeys);
        NeoForge.EVENT_BUS.addListener(this::addInventoryButton);
        NeoForge.EVENT_BUS.addListener(this::onClientTick);
        NeoForge.EVENT_BUS.addListener(this::onInventoryKey);
    }

    private void registerKeys(RegisterKeyMappingsEvent event) {
        event.register(shortcut);
    }

    private void addInventoryButton(ScreenEvent.Init.Post event) {
        var screen = event.getScreen();
        if (!(screen instanceof InventoryScreen || screen instanceof CreativeModeInventoryScreen)) {
            return;
        }
        var inventory = (AbstractContainerScreen<?>) screen;
        var occupied = new ArrayList<ButtonPlacement.Rect>();
        // Reserve creative tabs too, without replacing any vanilla widget.
        int padding = screen instanceof CreativeModeInventoryScreen ? 32 : 2;
        occupied.add(new ButtonPlacement.Rect(inventory.getGuiLeft() - padding, inventory.getGuiTop() - padding,
                inventory.getXSize() + padding * 2, inventory.getYSize() + padding * 2));
        for (var listener : event.getListenersList()) {
            if (listener instanceof AbstractWidget widget && widget.visible) {
                occupied.add(new ButtonPlacement.Rect(widget.getX() - 2, widget.getY() - 2,
                        widget.getWidth() + 4, widget.getHeight() + 4));
            }
        }
        ButtonPlacement.findInventory(screen.width, screen.height, occupied).ifPresent(position -> {
            Component label = position.width() == 20 ? Component.literal("H")
                    : Component.translatable("astropunk_handbook_access.button");
            var button = Button.builder(label, ignored -> openHandbook())
                    .bounds(position.x(), position.y(), position.width(), position.height())
                    .tooltip(Tooltip.create(Component.translatable("astropunk_handbook_access.tooltip")))
                    .build();
            event.addListener(button);
        });
    }

    private void onClientTick(ClientTickEvent.Post event) {
        boolean requested = false;
        while (shortcut.consumeClick()) {
            requested = true;
        }
        if (requested && Minecraft.getInstance().screen == null) {
            openHandbook();
        }
    }

    private void onInventoryKey(ScreenEvent.KeyPressed.Post event) {
        // Post runs only for keys the inventory did not already handle.
        if ((event.getScreen() instanceof InventoryScreen || event.getScreen() instanceof CreativeModeInventoryScreen)
                && shortcut.isActiveAndMatches(InputConstants.getKey(event.getKeyCode(), event.getScanCode()))) {
            openHandbook();
            event.setCanceled(true);
        }
    }

    private void openHandbook() {
        var minecraft = Minecraft.getInstance();
        var player = minecraft.player;
        var guide = player != null ? Guides.getById(HANDBOOK) : null;
        AccessPolicy.open(player != null, guide != null,
                // Match the working guidemec open path without common proxy dispatch.
                () -> GuideMEClient.openGuideAtPreviousPage(guide, guide.getStartPage()),
                key -> player.displayClientMessage(Component.translatable(key), true));
    }
}
