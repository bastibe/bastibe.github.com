---
title: Printing Photos
date: 2026-04-19
description: where I share my knowledge about printing photos.
filetags: photography
---

About a year ago I got a fancy Canon Pro 200 photo printer. Since then, I've been learning how to print photos at home. Here's an unstructured list of things I learned:

Make sure your screen isn’t too bright. There’s no hard and fast rule for screen brightness (contrary to popular belief[^1]). If the screen is too bright, everything looks more saturated and contrasty; thus, you’ll edit with reduced contrast and saturation, and your prints will look flat. So, if your prints look too flat, lower your screen brightness. Conversely, if your prints look too contrasty, raise your screen brightness.

[^1]: there are standards for cinema, video, and retouching, which define appropriate screen brightness for different room illuminations. But these are meant for dark rooms. For looking at prints (and office ergonomics), however, you need a bright room, so the standards do not apply. What matters is appropriate contrast reproduction, which is possible in any illumination. As a rule of thumb, make the screen a bit less bright than you'd think.

Avoid stray light onto your screen, as this produces glare, which raises the screen’s black point. If that happens, you’ll compensate by lowering your blacks in the edit, leading to prints with crushed blacks. If your prints have muddy, crushed blacks, check your screen for stray light. Better screens often come with much better antireflective coatings, which makes a big difference.

Avoid colorful objects within your field of vision while editing, these will bias your color perception. If your prints come out with an unexpected color cast, check if there is too much color in your field of vision while editing. This may include moody lighting or colored furniture. A colorful desktop background on your secondary screen can also be a problem.

See that your screen uses a neutral color temperature of 5000-6500K, use room lighting with a similar color temperature (4000-5000K), use a screen with decent colors, or calibrate your screen. But frankly, calibration is only relevant if you fixed everything else first, and only makes a small difference on a decent screen. Beware of old screen calibrators, though, as some models can age and drift over time[^2].

[^2]: In particular, the ColorMunki Smile and Spyder <= 5 are known to drift with age.

Make sure to edit with full-black and full-white. Prints have very limited dynamic range. Off-black blacks and off-white whites tend to look flat and broken. Use Darktable’s color assessment mode or a white editing background to get a feel for what white should be, and look at your histogram or waveform to ensure deep blacks. Off-white is immediately obvious in a print, off-black just looks muddy.

Prints need to be sharpened specifically for the intended print size. It’s not sufficient for details to be sharp at a pixel level. In fact, the pixel level is often entirely meaningless, as it’s way too small to be visible (corollary: noise doesn’t matter). So resize your image for the intended print size, and sharpen that file. Or use your printer driver’s sharpening option if there is one (“contrast reproduction” in Canon’s driver). Alternatively, dedicated printing software such as QImage often includes dedicated sharpening options for printing.

When experimenting with different papers, be aware that ICC profiles correct for the paper's tint. A print on a warm stock will be printed with cooler colors to compensate. This can look very silly. Especially for black-and-white prints, you're often better off to use the printer's black-and-white mode that doesn't introduce a color cast. In general, I've seen a few rather poor ICC profiles. Unless you're truly committed to hit a particular hue (often required in commercial work), it's worth experimenting with using just the paper profile, but no ICC.

Different papers and formats have a big influence on the appearance of a print. It's good fun and very instructive to experiment with various options. I like to have at least a glossy, a lustre, and a smooth fine art stock at hand. You can use a more structured paper to hide a slight softness in the image. The paper size also plays a big role. I particularly like 10x15 card stock, and double-A4 panoramic paper. A4/letter is too common in our world, and often looks boring, so go bigger or smaller, or leave a white margin. I didn't see any big differences between similar papers of different manufacturers, so it's safe to buy affordable and local options for common papers[^3].

[^3]: of course make sure the paper is appropriately coated for inkjet printing, and provides ICC profiles for your printer.

Lastly, it all depends on how the print will be presented. The print will look different depending on the illumination and surroundings. So whatever you do, make a small test print first, hold it up where it’s supposed to go, and adjust from there. It's quite common that prints change character as the illumination in the room changes throughout the day. In particular, make sure the print receives light from bulbs with a good CRI, or all your color corrections will be in vain.
