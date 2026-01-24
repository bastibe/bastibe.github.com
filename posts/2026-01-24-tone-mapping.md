---
title: On Tone Mapping
date: 2026-01-24
description: foo
filetags: photography
---

When we render a photo, we mimic the psychovisual effects of image brightness. I recently realized that we do this to trick our brain into a perception of brightness, even though the image is not actually very bright. Here's my current understanding of this aspect of image formation:

A camera records brightnesses up to ~30,000 nits of e.g. sunlit snow. Your computer screen, however, displays only ~300 nits, and a print on your living room wall is probably lit at ~100 nits. Due to the Hunt Effect and Stevens Effect, this greatly diminishes our perception of brightness and saturation. You know this, from how everything looks dull after the sun goes down. Thus when displaying or printing a photo, we need to boost contrast and saturation to achieve a realistic perception of the scene we photographed. If we had a 30,000 nit display, this would not be necessary. 

Increasing contrast means pushing bright pixels brighter, and dark pixels darker. However, the brightest and darkest possible colors for our displays and printers are *white* and *black*, therefore increasing contrast eventually desaturates highlights and shadows. This is odd, since bright colored lights in reality do not appear to desaturate: Cars' brake lights stay red, and neon signs stay colorful. But the desaturation is necessary for rendering realistic contrast on a display or print. 

<div class="lightbox" style="height: 200px">
    <figure>
        <img src="/static/2026-01/lightsabre.jpg">
        <figcaption>Neon lights: A bright core, with red shine</figcaption>
    </figure>
    <figure>
        <img src="/static/2026-01/pinlights.jpg">
        <figcaption>Bright LEDs: A bright core, with colorful shine</figcaption>
    </figure>
</div>

So what can we do to retain a perception of saturation in bright colored lights? We trick our brain: When our eyes are dark-adapted, and suddenly a bright colored stimulus hits our retina, the cone cells momentarily max out, and we see something approaching white. Then the cells adapt, and color comes back. We simulate this effect with a white core, and a colorful shine, which fools our vision system into a perception of “bright colored light”, even though our display isn’t actually all that bright, and the light isn't actually colored. And thus a light sabre looks red, even though it actually is white.

Additionally, our hue perception changes as colors go very bright: the Bezold–Brücke effect shifts hues as they go bright, and the Abney effect changes hue with the addition of white light. Thus when we push contrast, we not only need to fade the brightest colors to white, but also twist their hue to create a realistic perception of brightness. 

<div class="lightbox" style="height: 200px">
    <figure>
      <img src="/static/2026-01/fire_dt.jpg">
      <figcaption>An appropriate rendition of fire, in darktable<br>(AgX smooth, preserve hue 30%)</figcaption>
    </figure>
    <figure>
      <img src="/static/2026-01/fire_c1.jpg">
      <figcaption>An appropriate rendition of fire, in Capture One</figcaption>
    </figure>
    <figure>
      <img src="/static/2026-01/fire_dxo.jpg">
      <figcaption>An appropriate rendition of fire, in DxO Photo Lab</figcaption>
    </figure>
    <figure>
      <img src="/static/2026-01/fire_physical.jpg">
      <figcaption>A "physically correct" rendition of fire<br>(AgX none, preserve hue 100%)</figcaption>
    </figure>
</div>

We do all this to mimic the psychovisual effects of very bright light, even though the light from the display or print isn't actually particularly bright. But with a good psychovisual simulation, we fool our brain into a perception of brightness way beyond the capabilities of the display medium. Fascinating stuff!
