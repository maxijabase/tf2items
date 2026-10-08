# TF2Items

SourceMod extension that lets a plugin replace the item Team Fortress 2 gives a player. Maintained by [mge.tf](https://mge.tf).

This tree is [nosoop/SMExt-TF2Items](https://github.com/nosoop/SMExt-TF2Items), which adds `TF2Items_OnGetLoadoutItem` on top of [asherkin/TF2Items](https://github.com/asherkin/TF2Items). nosoop archived that repository. Releases are published from here.

## Releases

Push a tag such as `v1.6.4`. The Action compiles Linux and Windows, 32-bit and 64-bit, stamps that tag into the extension, and attaches:

- `tf2items-<tag>-linux.tar.gz`
- `tf2items-<tag>-windows.zip`

The current release is [v1.6.4](https://github.com/mgetf/tf2items/releases/tag/v1.6.4).

## Install

Unpack the archive into the server's `tf/` directory. On a 32-bit Linux server the extension is `addons/sourcemod/extensions/tf2items.ext.2.ep2v.so`. The empty `tf2items.autoload` next to it makes SourceMod load it on startup.

`tf2items_manager.smx` is installed under `plugins/optional` and stays unloaded. Move it to `plugins/` only if you want the bundled per-player weapon config. Plugins such as MGE-Whitelist talk to the extension directly and do not need the manager.

## Gamedata

Both files are installed under `addons/sourcemod/gamedata/`.

`tf2.items.txt` is the `GiveNamedItem` vtable offset. SourceMod's Automatic Updater rewrites this filename. The copy in this repository has Linux at 494.

`tf2.items.nosoop.txt` holds the `GetLoadoutItem` signature used by `TF2Items_OnGetLoadoutItem`. The second name is what keeps the updater from replacing that signature. Plugins that only use `TF2Items_OnGiveNamedItem` and `TF2Items_GiveNamedItem` do not call that forward.

## Build

`.github/workflows/build-on-push.yml` is the build. It checks out SourceMod 1.12-dev, Metamod:Source 1.12-dev, and the TF2 HL2SDK, then runs AMBuild. A tag push is enough. There is no separate local build script.
