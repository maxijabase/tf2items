# TF2Items

SourceMod extension that lets a plugin replace the item Team Fortress 2 gives a player.

Fork of [nosoop/SMExt-TF2Items](https://github.com/nosoop/SMExt-TF2Items), which adds `TF2Items_OnGetLoadoutItem` on top of [asherkin/TF2Items](https://github.com/asherkin/TF2Items).

## Install

Unpack the archive into the server's `tf/` directory. On a 32-bit Linux server the extension is `addons/sourcemod/extensions/tf2items.ext.2.ep2v.so`. The empty `tf2items.autoload` next to it makes SourceMod load it on startup.

`tf2items_manager.smx` is installed under `plugins/optional` and stays unloaded. Move it to `plugins/` only if you want the bundled per-player weapon config.
