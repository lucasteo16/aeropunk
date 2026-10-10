package dev.astropunk.handbook;

import dev.emi.emi.search.EmiSearch;
import dev.emi.emi.search.ModQuery;
import dev.emi.emi.search.SearchStack;
import net.minecraft.client.searchtree.SuffixArray;

/** Real released ModQuery and Minecraft suffix matching, with an isolated index fixture.
 * This is not an item registry dump or evidence that a candidate has live items.
 */
public final class VerifyEmiModQuery {
    static void check(boolean ok, String text) { if (!ok) throw new AssertionError(text); }
    public static void main(String[] args) {
        var index = new SuffixArray<SearchStack>();
        var entry = new SearchStack(null); // Only identity membership is exercised, not a game item.
        index.add(entry, "create_foo");
        index.add(entry, "localized producer name");
        index.generate();
        EmiSearch.mods = index;
        check(new ModQuery("create_foo").matches(null), "Exact namespace rejected");
        check(new ModQuery("CREATE_FOO").matches(null), "Case folding failed");
        check(new ModQuery("producer").matches(null), "Display name not searchable");
        check(!new ModQuery("createfoo").matches(null), "Underscores unexpectedly removed");
        check(!new ModQuery("create foo").matches(null), "Underscores unexpectedly replaced by spaces");
        check(new ModQuery("create").matches(null), "Expected substring match");
        check(!new ModQuery("absent").matches(null), "Unknown namespace matched");
        System.out.println("PASS released ModQuery namespace, display-name, case-folding, literal underscore and substring matching");
    }
}
