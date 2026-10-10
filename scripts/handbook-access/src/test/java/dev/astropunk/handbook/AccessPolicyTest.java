package dev.astropunk.handbook;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class AccessPolicyTest {
    @Test void availableGuideOpensOnce() {
        int[] opened = {0};
        AccessPolicy.open(true, true, () -> opened[0]++, key -> fail(key));
        assertEquals(1, opened[0]);
    }

    @Test void absentPlayerDoesNothing() {
        AccessPolicy.open(false, false, () -> fail("Opened without a player"), key -> fail(key));
    }

    @Test void missingGuideProducesFeedbackInsteadOfOpening() {
        boolean[] opened = {false};
        String[] feedback = {null};
        AccessPolicy.open(true, false, () -> opened[0] = true, key -> feedback[0] = key);
        assertFalse(opened[0]);
        assertEquals("astropunk_handbook_access.missing_guide", feedback[0]);
    }
}
