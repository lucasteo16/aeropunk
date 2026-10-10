package dev.emi.emi.search;

/** Test-only index storage boundary. Real ModQuery reads this exact field.
 * Avoids EmiSearch's registry-dependent static initialization. The bake method
 * is inspected from the unmodified selected release, never replaced in production.
 */
public final class EmiSearch {
    public static net.minecraft.client.searchtree.SuffixArray<SearchStack> mods;
}
