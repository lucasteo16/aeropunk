package dev.astropunk.handbook;

import java.util.List;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ButtonPlacementTest {
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

    @Test void noSpaceDoesNotReplaceControls() {
        assertTrue(ButtonPlacement.find(320, 240, 96, 20,
                List.of(new ButtonPlacement.Rect(0, 0, 320, 240))).isEmpty());
    }
}
