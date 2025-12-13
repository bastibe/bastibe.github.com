---
title: Kindle.app not starting on a case-sensitive file system
date: 2012-09-13 20:19
filetags: macos
---

So Kindle.app was updated through the App Store and did not start any more. It just crashed and the crash reporter came up.

A quick look at Console.app turns up a link to the actual crash report. And the crash report starts with

```
    Dyld Error Message:
      Library not loaded: @executable_path/../Frameworks/libWEbCoreKRF.dylib
      Referenced from: /Applications/Kindle.app/Contents/Frameworks/libWebCoreViewer.dylib
      Reason: image not found
```

 `libWEbCoreKRF.dylib` with a capitalized E? That looks very much like a spelling error. So, point your terminal to `/Applications/Kindle.app/Contents/Frameworks/`, type

```sh
    sudo ln -s libWebCoreKRF.dylib libWEbCoreKRF.dylib
```

to create a symlink with the misspelled name. Done.

Kindle works again.

Spelling is hard, it seems.
