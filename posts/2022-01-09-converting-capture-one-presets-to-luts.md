---
title: Converting Capture one Presets to LUTs
date: 2022-01-09 14:37
filetags: photography
---

A while ago, I bought an [RNI film pack](https:_www.reallyniceimages.com_) for Capture One. That's a set of presets that makes your digital photos look similar to analog film scans. However, since then my _other_ image editor, [Darktable](https:_www.darktable.org_) just released a new version, I'm now back to using Darktable instead of Capture One, thus without access to those presets.

Here's how to export Capture One presets to LUTs, to make them accessable to other programs.

The fun thing is, LUTs are just PNG files that contain a table of colors. You know, a "Look Up Table", of sorts. So, in order convert a preset to a LUT, all we need to do is apply the preset to a pristine "identity" LUT, and export it as a new PNG.

1. Get yourself an identity LUT.   
  For example, the one included in [Stuart Sowerby's Fuji Film Simulation Profiles](https://blog.sowerby.me/fuji-film-simulation-profiles/). Choose the sRGB PNG LUTs, for RawTherapee and Affinity Photo.
2. Open the LUT PNG in Capture One.
3. Apply the preset you want.   
   Optionally lower _saturation_ by -15, see below.
4. Export as PNG.   
   Make sure the color space is sRGB, just like the original file.

As easy as that.

A few more adjustments: many Capture One presets expect to be working on raw data, which is less saturated than Darktable's default. So I export with -15 _saturation_. Also, many presets include spacial adjustments such as Highlights or Shadows that are bound to not play well with the LUT PNG. To disable them, delete the offending lines from the *.costyle files[^1], or compensate the values with opposite slider movements.

[^1]: don't do this for RNI LUTs, it's forbidden by the User License Agreement that is hidden quite well in dark-grey-on-black at the very bottom of their website

When applying the LUTs in Darktable's _lut 3D_ module, there are a few more things you can do to fit them into your workflow. For example, you can lower the opacity of the _lut 3D_ module to vary their effect. Or you can choose _chromaticity_ as blend more to only apply their color transformation, but keep Darktable's tonal rendering. In _normal_ blend mode, some LUTs prefer a flat rendering as their input, so lower _contrast_ in _filmic rgb_ to zero and use the auto-pickers to set the image black and white point.
