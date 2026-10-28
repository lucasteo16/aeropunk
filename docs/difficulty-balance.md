# Difficulty balance

The difficulty replacement was developed on `test/difficulty` from committed `dev` at `6ed72bf`, with trial version `0.19.0-difficulty`. Dangerous 1.5.2 is removed; Scaling Difficulty 1.1.0 and Levelplate 1.0.0 are selected. Existing Cloth Config 15.0.140, Minecraft 1.21.1 and NeoForge 21.1.259 remain unchanged. Preparing or merging this source does not update live servers or launcher instances.

## Applied balance

Ordinary combat stays close to the existing Hard difficulty, with modest exploration growth. Distance contributes 0.05 per 500 blocks, time contributes 0.004 per 100 world days, and Overworld height contributes 0.025 per complete 30 blocks away from height 62. These combine before attribute ceilings. Time continues past day 5,000 and can eventually saturate ordinary ceilings near spawn.

Ordinary health is capped at 1.5 before randomness. Forty percent of eligible enemies receive up to 5 percent variation in both health and melee damage. Rounded upper estimates are 1.58 times ordinary health, 1.26 times melee damage, unchanged armor, and approximately 1.19 times creeper explosion damage. Arrows and qualifying special attacks follow the stored health multiplier, not the melee cap. Other mods and vanilla mechanics can affect final damage independently.

## Rare big zombies

Five percent of eligible adult zombie-family creatures receive twenty extra health points, one additional melee attack-attribute point, 1.2 visual size and 85 percent movement speed. Speedy variants are disabled. The fixed bonuses follow ordinary caps and randomness, intentionally exceeding the ordinary ceilings. One attack point is the smallest positive integer this setting accepts; for a three-point base attack attribute it is not a ten-percent bonus.

For a base-20-health zombie, ordinary and large health are respectively about 20 and 40 near baseline, 30 and 50 at the unrandomized ceiling, and up to 31.6 and 51.6 with positive random variation. Across the full random range, the fixed bonus makes large zombies roughly 63 to 105 percent more durable than corresponding ordinary versions. Exact hit counts depend on actual damage after armor, weapon effects, critical hits, class abilities and attack timing. At an illustrative ten effective damage per strike, the baseline comparison is two versus four hits and the unrandomized ceiling is three versus five hits. This is not a claim about unmodified diamond-sword damage.

## Complete Scaling Difficulty configuration, in file order

| Setting | Applied value | Explanation |
| --- | --- | --- |
| `increasingDistance` | `500` | Distance interval in blocks. Growth is approximately continuous, not a sudden jump every interval. |
| `distanceFactor` | `0.05` | Adds 0.05 per 500 blocks. Distance alone reaches the ordinary 1.5 health ceiling around 5,000 blocks. |
| `increasingTime` | `2000` | World-clock minutes per time increase, corresponding to 100 world days. Sleep advances this clock. |
| `timeFactor` | `0.004` | Adds 0.004 per completed time interval: 0.02 by day 500 and 0.2 by day 5,000. No independent time cap. |
| `heightDistance` | `30` | Complete vertical blocks per height interval, relative to startingHeight. |
| `heightFactor` | `0.025` | Adds 0.025 per height interval: 0.1 near height minus 64 and 0.2 at height 319 in the Overworld. |
| `maxFactorHealth` | `1.5` | Ordinary health ceiling before random variation and special-zombie bonuses. |
| `maxFactorDamage` | `1.2` | Ordinary melee-damage ceiling before random variation. Projectile and qualifying special damage instead use the stored health multiplier. |
| `maxFactorProtection` | `1.0` | No additional armor scaling. Existing mob armor and equipment still work. |
| `maxFactorSpeed` | `1.1` | Special-zombie speed ceiling. Does not accelerate ordinary mobs. No speedy variants are currently enabled. |
| `allowRandomValues` | Enabled | Enable one shared random modifier for a selected mob's health and melee damage. |
| `randomChance` | `40` | Percent chance for random variation on eligible mobs outside custom zones. |
| `randomFactor` | `5` | Vary the calculated health and melee multipliers by up to 5 percent below or above their capped values. |
| `extraXp` | Enabled | Enable experience increases from the stored difficulty multiplier. |
| `maxXPFactor` | `1.5` | Experience multiplier ceiling outside custom zones. Big-zombie bonus health does not separately increase stored difficulty. |
| `startingFactor` | `1.0` | Baseline multiplier before distance, time and height contributions. |
| `startingDistance` | `0` | Blocks from the dimension's shared spawn before distance begins contributing. |
| `startingTime` | `0` | World-clock minutes before time contributes. Uses the existing world clock, not time since installing the mod. |
| `startingHeight` | `62` | Vertical reference height with no height contribution. |
| `positiveHeightIncrement` | Enabled | Allow height contribution above the reference height in eligible dimensions. |
| `negativeHeightIncrement` | Enabled | Allow height contribution below the reference height in eligible dimensions. |
| `affectBosses` | Disabled | Disable scaling for creatures in the common bosses tag. Explicit exclusions reinforce known boss protection. |
| `excludeDistanceInOtherDimension` | Disabled | Keep ordinary distance scaling outside the Overworld, using that dimension's reference coordinates. |
| `excludeTimeInOtherDimension` | Disabled | Keep the small ordinary time contribution outside the Overworld. |
| `excludeHeightInOtherDimension` | Enabled | Suppress height scaling outside the Overworld, avoiding inappropriate height-62 assumptions. |
| `dropMoreLoot` | Enabled | Allow a restrained probability of one additional existing loot-table roll. A successful roll can still return no items. |
| `lootRollsFactor` | `0.025` | With Levelplate present, add 2.5 percentage points of extra-roll probability per reported level above one, subject to the cap. |
| `maxRollsPerDeath` | `0.2` | Cap the fractional extra-roll budget at 0.2: at most a 20 percent chance of one additional roll, not twenty percent extra of every item. |
| `levelFactor` | `0.0` | Zero contribution from the optional Heroes Levels integration. Not a Pufferfish class-power input. |
| `playerRadius` | `100.0` | Nearby-player radius in blocks for the inactive player-level contribution. |
| `hudTesting` | Disabled | Disable diagnostic difficulty overlay and custom-zone boundaries. |
| `renderDistance` | `8` | Custom-zone boundary display distance in chunks, not enemy scaling range. Inactive with diagnostic display disabled. |
| `devMode` | Disabled | Disable the privileged sddiag diagnostic command. Marked by the mod as requiring restart. |
| `allowSpecialZombie` | Enabled | Enable the rare large variant. The independent speedy-variant chance is zero. |
| `bigZombieChance` | `5` | Percent chance for an eligible adult zombie-family mob to become large. Other compatible Zombie subclasses can qualify. |
| `bigZombieSlownessFactor` | `0.85` | Large zombies move at 85 percent of ordinary speed. |
| `bigZombieBonusLifePoints` | `20` | Twenty additional health points after ordinary caps and randomness. Deliberate exception to the ordinary health ceiling. |
| `bigZombieBonusDamage` | `1` | Add one melee attack-attribute point after ordinary scaling and randomness; actual hit damage still depends on vanilla difficulty and other mechanics. |
| `bigZombieSize` | `1.2` | Large variant visual size multiplier. |
| `speedZombieChance` | `0` | Disable speedy zombies. |
| `speedZombieSpeedFactor` | `1.1` | Inactive restrained fallback if speedy zombies are enabled later. |
| `speedZombieMalusLifePoints` | `0` | Inactive fallback: no fixed health subtraction if speedy zombies are enabled later. |
| `dynamicBossModification` | Disabled | Disable additional boss difficulty from nearby players. |
| `dynamicBossModificator` | `0.3` | Inactive because boss scaling and multiplayer boss modification are disabled. |
| `bossMaxFactor` | `3.0` | Inactive boss health ceiling. Not an active triple-health setting in this preset. |
| `bossDistanceFactor` | `0.05` | Inactive separate boss distance contribution. |
| `bossTimeFactor` | `0.1` | Inactive separate boss time contribution. |
| `bossDistance` | `256.0` | Inactive boss player-counting radius in blocks. |
| `creeperExplosionFactor` | `0.75` | Multiplies stored health-linked creeper damage. With ordinary randomized health up to 1.58, explosion damage is at most about 1.19 times normal from this mod. Results not exceeding one leave original damage unchanged. Radius and block destruction are not controlled here. |
| `affectAnimalBabies` | Disabled | Skip baby mobs, not just baby animals, under the inspected implementation. |
| `excludedEntity` | 117 explicit entries | 117 explicit entity identifiers protecting reviewed wildlife, friendly utility creatures, player summons, known bosses and selected encounter parts. The original Bumblezone exclusion is preserved. See difficulty-exclusions.json for every identifier and provenance. |

## Complete Levelplate configuration, in file order

| Setting | Applied value | Explanation |
| --- | --- | --- |
| `levelMultiplier` | `20` | Displays the integer-truncated excess health ratio multiplied by twenty, with a minimum level of one. A 1.5 health ratio displays level ten. It does not increase enemy strength; the health represented by one level depends on the creature's base health. |
| `nameColor` | `#FFFFFFFF` | White nameplate text. |
| `backgroundColor` | `#F52891` | Stored background color, invisible at zero opacity. |
| `backgroundOpacity` | `0.0` | Transparent background. |
| `levelplateHeight` | `0.5` | Nameplate offset above the creature. |
| `levelplateSize` | `-0.0125` | Smaller labels; rendered scale uses the absolute magnitude of this value. |
| `showHealth` | Disabled | Do not add numeric current and maximum health text; the bar provides that feedback. |
| `showLevel` | Enabled | Enable the overhead plate. This implementation hides the whole plate when disabled. |
| `renderDistance` | `30.0` | Maximum overhead nameplate distance in blocks. |
| `showHostileOnly` | Enabled | Display plates only for creatures implementing the hostile Enemy interface. Does not control actual scaling, and some aggressive modded creatures can be omitted. |
| `showLevelplateIfObstructed` | Disabled | Do not reveal plates through obstructing terrain. |
| `useScalingDifficultyLvl` | Enabled | Derive displayed level from the maximum-health ratio. Not a complete measure of danger. |
| `levelTitle` | Disabled | Disable the optional Travelers' Titles integration because the selected releases have a confirmed field-descriptor mismatch. Gameplay failure was not reproduced. |
| `healthBar` | Enabled | Display a health bar above eligible enemies. |
| `debugMode` | Disabled | Disable rendering diagnostic messages. |
| `excludedEntities` | 18 explicit entries | Hide plates on major bosses and selected encounter parts. Elder Guardian, Warden and Wildfire are not display-excluded but remain excluded from scaling. Display exclusion is independent of scaling exclusion. |

## Eligibility and boss protection

The selected archives provide native common boss tags for 13 major modded bosses, in addition to Scaling Difficulty's four explicit vanilla boss tags. Explicit exclusions reinforce those bosses, protect the Invoker and Wildfire, preserve Kraken encounter parts, and keep reviewed wildlife, friendly entities and player-owned summons out of generic scaling. Every newly added identifier was checked against a Minecraft 1.21.1 registry listing or the selected publisher-checksummed mod's registration code or tags. See `docs/difficulty-exclusions.json` for the grouped list and evidence boundary.

This is a reviewed static list, not an automatic hostile-only filter or proof that a future mod addition will be covered. Passive and neutral animals are deliberately left at their native statistics. Babies are skipped. Aggressive ordinary creatures not in this list continue to scale.

Lucas confirmed native boss bars on all eight excluded Cataclysm bosses in game. The Illager Invasion Invoker has its own boss bar according to the author's release notes; this is not the vanilla Evoker. Ender Dragon and Wither have native bars. Bosses'Rise release notes document boss bars and fixes, but command-spawned encounters did not reliably show them during review. Lucas accepted retaining its seven display exclusions on the assumption of native encounter presentation, not individual verification of every boss or encounter part. In particular, Cinematic Kraken and Kraken Tentacle are encounter entities, not proof of independent boss bars.

No custom zones or per-dimension overrides were added. Zones can bypass ordinary attribute and reward caps; introducing them requires another balance review. Removing Dangerous also removes its gear, enchantment and behavior features, and does not prove old saved enemies lose persistent modifiers.

## Numeric overview and boss policy

At world day 500 and height 62, ignoring random variation, approximate ordinary health and melee multipliers are respectively 1.02 and 1.02 at spawn; 1.12 and 1.12 at 1,000 blocks; 1.27 and 1.2 at 2,500 blocks; 1.42 and 1.2 at 4,000 blocks; and 1.5 and 1.2 at 5,000 blocks or farther. Random variation applies to forty percent of eligible mobs after caps. Overall ordinary upper estimates remain 1.58 health, 1.26 melee damage, 1.58 attributed projectile or special damage, and 1.185 creeper explosion damage. Ordinary armor and speed remain unchanged. These are per-attribute modifiers, not a universal combat-strength rating or a live measurement.

For a base-20-health, base-three-attack zombie at the unrandomized ceiling, ordinary attributes are 30 health and 3.6 attack; the large variant has 50 health and 4.6 attack. Positive random extremes are 31.6 health and 3.78 attack ordinarily, or 51.6 health and 4.78 attack for the large variant. The large zombie is therefore roughly 28 percent harder-hitting than the corresponding ordinary zombie at the unrandomized ceiling, not an additional fixed percentage for every zombie subtype. Vanilla Hard damage processing and player mitigation are separate from these attack attributes.

Extra loot is enabled with factor 0.025 and maximum fractional roll budget 0.2. With the selected Levelplate integration, reported level one gives no extra roll; level two gives 2.5 percent probability; level three gives 5 percent; level five gives 10 percent; level nine or above reaches the 20 percent ceiling. With the current multiplier twenty, an ordinary creature at the unrandomized 1.5 health ceiling displays level ten and therefore reaches that loot ceiling when its level has been recorded. The helper first uses Levelplate's stored level when above one, otherwise it falls back to the pre-variant stored health multiplier. Large-zombie bonus rewards can therefore depend on whether Levelplate has recorded the larger health-derived level. The extra-loot method has no separate excludedEntity guard: an excluded creature with an independently elevated reported level can still receive bonus loot. These settings do not increase equipment-drop chances directly.

Boss scaling and multiplayer boss modification remain disabled. All 117 scaling exclusions are retained. The earlier multiplayer-scaling proposal was not adopted; the policy is to preserve native boss statistics and encounter behavior.

## Verification

The isolated Java 21 probe used the actual selected Scaling Difficulty and Levelplate configuration classes, Cloth Config's actual default Gson serializer instance, and the inherited post-load validation hook. All 51 Scaling Difficulty fields and all 16 Levelplate fields passed declared-key coverage, annotated-bound checks and serialization, validation and save/reload comparison. The test compares serialized numeric values rather than expecting binary floating-point numbers to store decimal fractions exactly.

Those Java checks covered the original trial candidate. Later Levelplate display edits passed JSON parsing and diff whitespace checks; they were not a repeat of that full Java probe. Native `packwiz refresh` updates configuration index hashes and the pack index hash after edits. The optional Levelplate biome-title integration is disabled to avoid its confirmed binary field mismatch; this is not an upstream code repair.

Lucas launched the trial in a separate client instance and disposable world, reported successful operation and scaling of newly spawned mobs, and accepted the observed boss behavior. His ordinary-mob observations included displayed level ten and roughly fifteen hearts for creatures with ten base hearts. These observations are user-provided gameplay acceptance, not proof that every creature or random extreme was exercised.

The trial was committed as `d524a97`, with later display changes in `f420d5b` and `40d7897`. A native Modrinth trial export was generated before the final display changes. A difficulty-only server patch was subsequently built from `40d7897`, with downloaded mod checksums and exact configuration bytes verified. The patch requires manually removing Dangerous and adding the two replacement mods and configuration files; it does not change the loader or world.

Dedicated-server startup, multiplayer client connection, exact weapon hit counts and migration of existing-world saved modifiers remain untested. No live deployment or remote push is implied by these checks.
