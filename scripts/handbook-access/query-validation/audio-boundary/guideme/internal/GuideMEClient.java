package guideme.internal;

/** Test-only audio boundary. The released link constructor reads this field.
 * Avoids booting the entire NeoForge mod loader in a headless compiler probe.
 * This class MUST NOT be packaged in the helper or installed in Minecraft.
 */
public final class GuideMEClient {
    public static net.minecraft.sounds.SoundEvent GUIDE_CLICK_EVENT;
}
