---
navigation:
  title: "Deferred optimizers"
  position: 0
  parent: reference.technical.md
  icon: minecraft:repeater
---

# Deferred optimizers

## Separate trials

Experimental optimizers are tested on separate branches before adoption. Async Logger, Jasione and ServerCore have now been promoted to the shared pack.

- [Shared optimizers](performance.baseline.md)


***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| <ItemImage id="minecraft:redstone" /> [Async Logger](performance.deferred.md) | Asynchronous log processing. | No separate item search |
| <ItemImage id="minecraft:redstone" /> [Jasione](performance.deferred.md) | Reduces repeated enumeration-array allocations. | No separate item search |
| <ItemImage id="minecraft:redstone" /> [ServerCore](performance.deferred.md) | Optimizes server chunk ticking and creature spawning, with configurable workload controls. | No separate item search |
