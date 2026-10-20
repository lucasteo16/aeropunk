---
navigation:
  title: "Inventory tools"
  position: 1
  parent: reference.machines-storage.md
  icon: minecraft:bundle
---

# Inventory tools

![YouTube](images/tutorial-video.png) [English](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Interactic+Renewed+Mouse+Tweaks+Inventory+tools+tutorial) · [中文](https://www.youtube.com/results?search_query=Minecraft+1.21.1+Interactic+Renewed+Mouse+Tweaks+%E6%95%B4%E7%90%86%E3%80%81%E8%BD%AC%E7%A7%BB%E4%B8%8E%E4%B8%A2%E5%BC%83%E7%89%A9%E5%93%81+%E5%85%A5%E9%97%A8+%E6%95%99%E7%A8%8B)

## The inventory itself is the interface

Most storage time is lost in the screens, not in the containers. This pack installs three interface mods that remove the repeated drag and click work.

Open any supported container and use its search field and sort button. Sophisticated Inventory Interactions adds search, player inventory sorting, container sorting and transfer controls to supported screens.

<ItemGrid><ItemIcon id="minecraft:chest" /><ItemIcon id="minecraft:hopper" /><ItemIcon id="minecraft:shulker_box" /><ItemIcon id="minecraft:lava_bucket" /></ItemGrid>

| Screen action | What it saves |
| --- | --- |
| Search field | Scrolling a full chest for one item |
| Sort button | Manual arrangement after every dump |
| Transfer controls | Shift clicking one stack at a time |
| Mouse wheel over a slot | Dragging a stack by hand |

Mouse Tweaks handles the drag and wheel side. It is a convenience mod, so the exact gesture is worth checking once in the controls screen rather than assuming it matches another pack.

***

## What gets picked up

<EmiSearch query="@interactic" />

<ItemGrid><ItemIcon id="interactic:item_filter" /><ItemIcon id="minecraft:hopper" /></ItemGrid>

| Setting | Effect |
| --- | --- |
| Filter contents | Items that may be collected |
| Pickup rules | Whether the filter decides what enters your inventory |
| Rendering rules | Whether filtered drops are drawn differently |

Interactic Renewed separates pickup from rendering, so a filter can hide clutter from view without changing what you actually collect. Set it before a mining trip, not after your inventory is full of stone.

The mod is also what makes dropped items easier to see and grab. A filter that hides an item from rendering does not stop you collecting it.

***

## The trash slot is not storage

| Setting in this pack | Value |
| --- | --- |
| Instant deletion | Off, so items wait in the slot |
| Delete while slot is hidden | Off |
| Deny list | Empty, so nothing is protected by default |
| Hints | On |

Instant deletion being off is the setting that matters. An item in the trash slot is not gone until the slot is cleared, which gives you one chance to take it back. Turning instant deletion on removes that chance for every item at once.

The deny list is empty, so TrashSlot protects nothing on its own. If a valuable item keeps ending up there, add it to the deny list rather than relying on care.

Current bindings for the carry key and the handbook are in [Controls](help.controls.md).


***

## Related mods

| Mod or content | Purpose | Item search |
| --- | --- | --- |
| ![Interactic Renewed](images/catalog-bm12h14f.png) [Interactic Renewed](storage.handling.md) | Improves interaction with dropped items in the world. | <EmiSearch query="@interactic" /> |
| ![Mouse Tweaks](images/catalog-ac3cm3vq.png) [Mouse Tweaks](storage.handling.md) | Adds mouse-drag and scrolling shortcuts for moving inventory stacks. | No separate item search |
| ![Sophisticated Inventory Interactions](images/catalog-orgy0jio.png) [Sophisticated Inventory Interactions](storage.handling.md) | Adds sorting, searching and transfer controls to supported inventory screens. | No separate item search |
| ![TrashSlot](images/catalog-vryk0bv7.png) [TrashSlot](storage.handling.md) | Adds an inventory trash slot for discarding unwanted items. | No separate item search |
