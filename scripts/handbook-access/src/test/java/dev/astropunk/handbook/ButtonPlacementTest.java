package dev.astropunk.handbook;

import java.util.List;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ButtonPlacementTest {
    @Test void guideFitsImmediatelyLeftOfNativeSearch() {
        var search = new ButtonPlacement.Rect(350, 410, 160, 18);
        // Reserve eight logical pixels to the right, independent of display scale.
        var button = ButtonPlacement.findGuide(900, 440, 48, search, List.of(search)).orElseThrow();
        assertEquals(search.x() - 8, button.x() + button.width());
        assertEquals(search.y() + search.height() / 2, button.y() + button.height() / 2);
    }

    @Test void tracksMovedAndResizedSearchAtCompactScale() {
        for (var search : List.of(new ButtonPlacement.Rect(90, 173, 160, 18),
                new ButtonPlacement.Rect(500, 410, 220, 18))) {
            var button = ButtonPlacement.findGuide(900, 440, 48, search, List.of(search)).orElseThrow();
            assertEquals(search.x() - 8, button.x() + button.width());
            assertFalse(button.overlaps(search));
        }
    }

    @Test void blockedLeftUsesBoundedFallbackWithoutSearchOverlap() {
        var search = new ButtonPlacement.Rect(40, 173, 160, 18);
        var controls = new ButtonPlacement.Rect(2, 172, 42, 20);
        var result = ButtonPlacement.findGuide(344, 194, 48, search, List.of(search, controls)).orElseThrow();
        assertFalse(result.overlaps(search));
        assertFalse(result.overlaps(controls));
        assertTrue(result.x() >= 2 && result.y() >= 2);
        assertTrue(result.x() + result.width() <= 342 && result.y() + result.height() <= 192);
    }

    @Test void absentOrHiddenSearchUsesFullGuideLabelFallback() {
        var inventory = new ButtonPlacement.Rect(82, 12, 180, 170);
        var result = ButtonPlacement.findGuide(344, 194, 48, null, List.of(inventory)).orElseThrow();
        assertEquals(48, result.width());
        assertFalse(result.overlaps(inventory));
    }

    @Test void entirelyOccupiedScreenHidesGuideRatherThanOverlap() {
        assertTrue(ButtonPlacement.findGuide(344, 194, 48, null,
                List.of(new ButtonPlacement.Rect(0, 0, 344, 194))).isEmpty());
    }

    @Test void avoidsExistingControlsAndInventoryPanel() {
        var inventory = new ButtonPlacement.Rect(72, 37, 176, 166);
        var control = new ButtonPlacement.Rect(220, 4, 96, 20);
        var result = ButtonPlacement.find(320, 240, 96, 20, List.of(inventory, control));
        assertTrue(result.isPresent());
        var button = result.orElseThrow();
        assertFalse(button.overlaps(inventory));
        assertFalse(button.overlaps(control));
        assertTrue(button.x() >= 4 && button.y() >= 4);
        assertTrue(button.x() + button.width() <= 316);
        assertTrue(button.y() + button.height() <= 236);
    }

    @Test void compactViewportKeepsAnInventoryEntry() {
        var inventory = new ButtonPlacement.Rect(82, 12, 180, 170);
        var result = ButtonPlacement.findInventory(344, 194, List.of(inventory));
        assertTrue(result.isPresent(), "A compact entry must remain available beside the inventory");
        var button = result.orElseThrow();
        assertFalse(button.overlaps(inventory));
        assertEquals(20, button.width());
        assertEquals(20, button.height());
    }

    @Test void noSpaceDoesNotReplaceControls() {
        assertTrue(ButtonPlacement.find(320, 240, 96, 20,
                List.of(new ButtonPlacement.Rect(0, 0, 320, 240))).isEmpty());
    }
}
