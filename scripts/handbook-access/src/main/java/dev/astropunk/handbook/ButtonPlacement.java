package dev.astropunk.handbook;

import java.util.List;
import java.util.Optional;

final class ButtonPlacement {
    record Rect(int x, int y, int width, int height) {
        boolean overlaps(Rect other) {
            return x < other.x + other.width && x + width > other.x
                    && y < other.y + other.height && y + height > other.y;
        }
    }

    private ButtonPlacement() {}

    static Optional<Rect> findInventory(int screenWidth, int screenHeight, List<Rect> occupied) {
        var full = find(screenWidth, screenHeight, 96, 20, occupied);
        return full.isPresent() ? full : find(screenWidth, screenHeight, 20, 20, occupied);
    }

    static Optional<Rect> find(int screenWidth, int screenHeight, int width, int height, List<Rect> occupied) {
        for (int y = 4; y + height <= screenHeight - 4; y += 4) {
            for (int x = screenWidth - width - 4; x >= 4; x -= 4) {
                Rect candidate = new Rect(x, y, width, height);
                if (occupied.stream().noneMatch(candidate::overlaps)) {
                    return Optional.of(candidate);
                }
            }
        }
        return Optional.empty();
    }
}
