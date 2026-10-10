package dev.astropunk.handbook;

import dev.emi.emi.screen.EmiScreenManager;
import dev.emi.emi.config.SidebarSide;
import java.util.List;
import net.minecraft.client.gui.components.AbstractWidget;

/** Isolated optional compatibility with the checksum-pinned EMI 1.1.24 release.
 * EmiApi does not expose search geometry. Never changes EMI layout or creates a search widget.
 */
final class EmiSearchPlacement {
    private EmiSearchPlacement() {}

    static ButtonPlacement.Rect collect(List<ButtonPlacement.Rect> occupied) {
        // Search can remain visible while EMI is disabled in this selected release.
        var search = EmiScreenManager.search;
        if (search != null && search.visible) add(occupied, search);
        add(occupied, EmiScreenManager.emi);
        add(occupied, EmiScreenManager.tree);
        if (!EmiScreenManager.isDisabled()) {
            for (var side : SidebarSide.values()) {
                if (side == SidebarSide.NONE) continue;
                var panel = EmiScreenManager.getPanelFor(side);
                if (panel == null || !panel.isVisible()) continue;
                var bounds = panel.getBounds();
                occupied.add(new ButtonPlacement.Rect(bounds.x(), bounds.y(), bounds.width(), bounds.height()));
                add(occupied, panel.pageLeft);
                add(occupied, panel.pageRight);
                add(occupied, panel.cycle);
            }
        }
        return search != null && search.visible ? rect(search) : null;
    }

    private static void add(List<ButtonPlacement.Rect> occupied, AbstractWidget widget) {
        if (widget != null && widget.visible) occupied.add(rect(widget));
    }

    private static ButtonPlacement.Rect rect(AbstractWidget widget) {
        return new ButtonPlacement.Rect(widget.getX(), widget.getY(), widget.getWidth(), widget.getHeight());
    }
}
