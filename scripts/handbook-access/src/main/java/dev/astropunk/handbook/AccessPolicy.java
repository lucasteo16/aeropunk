package dev.astropunk.handbook;

import java.util.function.Consumer;

final class AccessPolicy {
    private AccessPolicy() {}

    static void open(boolean playerPresent, boolean guidePresent, Runnable open, Consumer<String> feedback) {
        if (!playerPresent) {
            return;
        }
        if (!guidePresent) {
            feedback.accept("astropunk_handbook_access.missing_guide");
        } else {
            open.run();
        }
    }
}
