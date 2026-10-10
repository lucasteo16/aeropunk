# Handbook access

Astropunk provides a custom whole-handbook action named Open Astropunk Handbook, under the Astropunk Handbook keybinding category. Its default is comma. The Guide button beside the recipe search field opens the same handbook and does not disable the shortcut. The button leaves eight logical pixels before the search field.

GuideME's own Open Guide for Items action is different. It opens contextual pages from associated item tooltips. Astropunk leaves that action unbound by default. Filtering the controls list for GuideME can omit the custom Astropunk category. Search for Astropunk or Handbook instead.

Existing installations preserve saved bindings. Changing packaged defaults does not override a player assignment such as backtick. In an existing installation, set Open Astropunk Handbook to comma and leave Open Guide for Items unbound. Fresh installations receive the corrected defaults.

## Sources

- https://guideme.appliedenergistics.org/open-guide-hotkey
- https://guideme.appliedenergistics.org/integration/
- https://guideme.appliedenergistics.org/commands

The implementation was also checked against the selected GuideME 21.1.19 archive, not just current online documentation. Compiled wiring tests verify the custom registration listener and independent world and inventory input paths. Placement tests verify the increased search-field gap. These checks do not substitute for a user-controlled game launch.
