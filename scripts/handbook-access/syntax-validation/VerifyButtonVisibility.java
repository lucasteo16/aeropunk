package dev.astropunk.handbook;

import java.util.List;

/** Characterizes the existing placer with real helper code, not a game. */
public final class VerifyButtonVisibility {
    public static void main(String[] args) {
        // Inventory 176 by 166, centered in a compact scaled viewport.
        var inventory = new ButtonPlacement.Rect(82, 12, 180, 170);
        var compact = ButtonPlacement.find(344, 194, 96, 20, List.of(inventory));
        if (compact.isPresent()) throw new AssertionError("Expected existing compact viewport omission");
        var roomy = ButtonPlacement.find(480, 270, 96, 20,
                List.of(new ButtonPlacement.Rect(150, 50, 180, 170)));
        if (roomy.isEmpty()) throw new AssertionError("Expected a visible button with room");
        System.out.println("CONFIRMED compact 344 by 194 viewport silently omits 96 by 20 button.");
        System.out.println("PASS roomy 480 by 270 viewport produces a button.");
        System.out.println("Characterization only. Actual running viewport was not measured.");
    }
}
