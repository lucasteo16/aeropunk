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

    static Optional<Rect> findGuide(int screenWidth, int screenHeight, int width, Rect search, List<Rect> occupied) {
        if (search != null) {
            var left = new Rect(search.x() - width - 4, search.y() + search.height() / 2 - 10, width, 20);
            if (fits(left, screenWidth, screenHeight, occupied)) return Optional.of(left);
        }
        // Bounded bottom-first fallback when left adjacency is impossible or EMI is absent.
        for (int y = screenHeight - 22; y >= 2; y -= 4) {
            for (int x = 2; x + width <= screenWidth - 2; x += 4) {
                var candidate = new Rect(x, y, width, 20);
                if (fits(candidate, screenWidth, screenHeight, occupied)) return Optional.of(candidate);
            }
        }
        return Optional.empty();
    }

    private static boolean fits(Rect rect, int width, int height, List<Rect> occupied) {
        return rect.x() >= 2 && rect.y() >= 2 && rect.x() + rect.width() <= width - 2
                && rect.y() + rect.height() <= height - 2 && occupied.stream().noneMatch(rect::overlaps);
    }

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
