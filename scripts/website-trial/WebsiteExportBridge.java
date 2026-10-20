package dev.astropunk.handbook;

import guideme.Guides;
import guideme.internal.siteexport.SiteExporter;
import java.nio.file.Path;
import net.minecraft.client.Minecraft;
import net.minecraft.client.gui.screens.LoadingOverlay;
import net.minecraft.resources.ResourceLocation;
import net.neoforged.api.distmarker.Dist;
import net.neoforged.bus.api.SubscribeEvent;
import net.neoforged.fml.common.EventBusSubscriber;
import net.neoforged.neoforge.client.event.ClientTickEvent;

/** Disposable entry point for the official exporter already present in GuideME 21.1.19. */
@EventBusSubscriber(modid = "astropunk_handbook_access", value = Dist.CLIENT)
public final class WebsiteExportBridge {
    private static boolean scheduled;

    @SubscribeEvent
    public static void tick(ClientTickEvent.Post event) {
        String destination = System.getProperty("astropunk.websiteTrial.destination");
        var client = Minecraft.getInstance();
        if (scheduled || destination == null || client.getOverlay() instanceof LoadingOverlay) return;
        var guide = Guides.getById(ResourceLocation.fromNamespaceAndPath("astropunk", "handbook"));
        if (guide == null || guide.getPages().isEmpty()) return;
        scheduled = true;
        System.out.println("ASTROPUNK_WEBSITE_TRIAL: starting official GuideME 21.1.19 export to " + destination);
        new SiteExporter(client, Path.of(destination), guide) {
            @Override protected String getModVersion() {
                return "0.16.4-authored-guide-with-0.17.0-instance-mods-trial";
            }
        }.exportOnNextTickAndExit();
    }
}
