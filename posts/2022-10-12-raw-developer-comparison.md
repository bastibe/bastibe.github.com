---
title: RAW Developer Comparison 2
date: 2022-10-11 19:15
filetags: photography
---

It's that time of the year again when all image editing programs come out with new versions. This comes at an inopportune time, as I feel restless of late. So, naturally, I had to try them all. Or maybe I just wanted a justification for buying DxO PhotoLab, because people on the internet speak so well of it 🙄.

For the following comparison I downloaded trial versions of [ACDSee Photo Studio Ultimate 2023](https:_www.acdsee.com) (€155), [Capture One 22](https:__www.captureone.com_) (€350 or €220/a), [Darktable 4.0](https:_www.darktable.org_) (free), [DxO Photolab 6](https:_www.dxo.com_) (€220 + €140 for FilmPack 6 + €99 for ViewPoint), [Adobe Lightroom Classic 11.5](https://www.adobe.com/products/photoshop-lightroom-classic.html) (€142/a), [ON1 Photo Raw 2023](https:_www.on1.com_) (€126), [RawTherapee 5.8](https:_rawtherapee.com_) (free), [Silkypix Developer Studio Pro 11](https://silkypix.isl.co.jp/en/) (€155), [Exposure X7](https:_exposure.software_) (€165), and [Zoner Photo Studio X Fall 2022](https:_www.zoner.com_) (€60/a). I also installed [Luminar Neo](https://skylum.com/luminar) (€120 or €80/a) and [Radiant Photo](https:_radiantimaginglabs.com_) (€140) but I disliked them so immediately and viscerally that I didn't include them in the comparison below.

In order to put them through their paces, I took a random smattering of images from the last few years that I found difficult to work with for one reason or another, and checked how each of the programs dealt with them. Of course I am no expert in any of them except Darktable and Capture One, so my results are probably flawed. I tried to inject some objectivity by limiting my edits to the most obvious sliders wherever possible, especially in the programs I know better. Regardless, my comparison is probably less scientific than [last time](https://bastibe.de/2020-05-01-raw-developer-comparison.html), because my brain sort of broke after staring at too many renderings of the same images for too long. Don't try this at home, folks!

## Test Case One: Fire

Fire is notoriously difficult to deal with, because it covers a large dynamic range, and we have strong associations of certain colors with heat. Thus a more yellow rendering usually suits fire very well, whereas a more neutral rendering quickly looks unnatural. In particular, we seem to expect highlights to twist to yellow, and midtones to remain orange.

My editing goals for this picture are simple: raise _shadows_ or _blacks_ until the pan becomes faintly visible, and reign in highlights if necessary to prevent excessive clipping.

<br>
  <div class="lightbox" style="height: 200px">
    <figure>
      <img src="/static/2022-10/DSCF9359_acd.thumb.jpg">
      <figcaption>ACDSee Photo Studio<br>
      highlights turn strongly yellow</figcaption>
    </figure>
    <figure>
      <img src="/static/2022-10/DSCF9359_c1.thumb.jpg">
      <figcaption>Capture One<br>
      highlights turn yellow<br>
      shadows adjusts unusally far into midtones</figcaption>
    </figure>
    <figure>
      <img src="/static/2022-10/DSCF9359_dt_v6.thumb.jpg">
      <figcaption>Darktable (filmic v6)<br>
      highlights turn desaturate<br>
      weirdly salmon color<br>
      filmic v6, zero latitude, no color preservation<br>
      tone EQ very unusual re: shadows/blacks sliders</figcaption>
    </figure>
    <figure>
      <img src="/static/2022-10/DSCF9359_dt_v5.thumb.jpg">
      <figcaption>Darktable (filmic v5)<br>
      highlights turn yellow<br>
      filmic v5, zero latitude, no color preservation<br>
      tone EQ very unusual re: shadows/blacks sliders</figcaption>
    </figure>
    <figure>
      <img src="/static/2022-10/DSCF9359_dxo.thumb.jpg">
      <figcaption>DxO PhotoLab<br>
      highlights desaturate</figcaption>
    </figure>
    <figure>
      <img src="/static/2022-10/DSCF9359_lr.thumb.jpg">
      <figcaption>Lightroom Classic<br>
      highlights desaturate</figcaption>
    </figure>
    <figure>
      <img src="/static/2022-10/DSCF9359_on1.thumb.jpg">
      <figcaption>ON1 Photo RAW<br>
      highlights turn very yellow<br>
      pan immediately visible without adjustments</figcaption>
    </figure>
    <figure>
      <img src="/static/2022-10/DSCF9359_rt.thumb.jpg">
      <figcaption>RawTherapee<br>
      highlights desaturate</figcaption>
    </figure>
    <figure>
      <img src="/static/2022-10/DSCF9359_sp.thumb.jpg">
      <figcaption>Silkypix Developer<br>
      highlights turn yellow, but lose all definition<br>
      shadows slider not strong enough to show pan</figcaption>
    </figure>
    <figure>
      <img src="/static/2022-10/DSCF9359_x7.thumb.jpg">
      <figcaption>Exposure X7<br>
      highlights turn unpleasant white<br>
      raising shadows turns background off-black</figcaption>
    </figure>
    <figure>
      <img src="/static/2022-10/DSCF9359_zp.thumb.jpg">
      <figcaption>Zoner Photo Studio<br>
      highlights desaturate<br>
      weird, clarity-like effect</figcaption>
    </figure>
  </div>
<p>Fujifilm X-Pro2 with XF35mmF1.4 R 1/1000s f/2.2 ISO400<br><a href="/static/2022-10/DSCF9359.RAF">&#x1f4c2; DSCF9359.RAF</a> (23.0 MB) <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/80x15.png" /></a></p>

There's a difficult tradeoff to be made here: Fire highlights physically don't change hue much compared to the fire body, but we visibly expect "hotter" fire to twist yellow. So a balance has to be struck between merely desaturating highlights, and twisting them yellow. You can see Darktable v6, DxO PhotoLab, RawTherapee, Exposure, and Zoner leaning towards desaturation, while the others render yellow color twists of some form or another. ACDSee and ON1 probably take the yellow a bit too far.

However, there's a flip side to this: Every program that renders yellow highlights in fire, does the same for overexposed skin, twists overexposed skies cyan, and red flowers magenta. It's a difficult tradeoff to get right. This is especially tricky since color shifts in highlights are often baked deeply into the programs' color science, and hard to get rid off where they're unwanted.

Anyway, to my eyes, the only fire-like renderings here come from Capture One, Darktable v5, PhotoLab, and Lightroom.

## A Hazy Mountain

This lovely scene is a deep crop into an image taken at long distance on a hazy day. The challenge is therefore _dehazing_ the mountains, chiseling out the contours with _clarity_ and _texture_ and _contrast_, and removing any extraneous noise.

This is a difficult task, as emphasizing local contrast tends to produce halos near the horizon, dehazing tends to introduce unpleasant color shifts, and the deep crop necessitates a subtle balance between denoising and detail retention.

<br>
  <div class="lightbox" style="height: 200px">
    <figure>
      <img src="/static/2022-10/DSF4442_acd.thumb.jpg">
      <figcaption>ACDSee Photo Studio<br>
      strong halos from clarity/texture<br>
      very inefficient/smeary denoising</figcaption>
    </figure>
    <figure>
      <img src="/static/2022-10/DSF4442_c1.thumb.jpg">
      <figcaption>Capture One<br>
      very little dehaze used, as higher settings break tonality<br>
      little definition in shadows</figcaption>
    </figure>
    <figure>
      <img src="/static/2022-10/DSF4442_dt.thumb.jpg">
      <figcaption>Darktable<br>
      very little default saturation, easy to fix<br>
      outstandingly subtle rendering to my eye</figcaption>
    </figure>
    <figure>
      <img src="/static/2022-10/DSF4442_dxo.thumb.jpg">
      <figcaption>DxO PhotoLab<br>
      dehaze ("ClearView") produces strong hue shift<br>
      clarity ("Microcontrast") is very slow<br>
      contrast not enough editing range, added tone curve to help<br>
      denoise ("DeepPrime") annoyingly only visible in mini viewer</figcaption>
    </figure>
    <figure>
      <img src="/static/2022-10/DSF4442_lr.thumb.jpg">
      <figcaption>Lightroom Classic<br>
      dehaze works perfectly!<br>
      denoise not very effective and slightly wormy<br>
      tends to strong halos from clarity</figcaption>
    </figure>
    <figure>
      <img src="/static/2022-10/DSF4442_on1.thumb.jpg">
      <figcaption>ON1 Photo RAW<br>
      dehaze produces strong hue shift<br>
      strong halos on the horizon<br>
      highlights tend to blow to pure white somehow</figcaption>
    </figure>
    <figure>
      <img src="/static/2022-10/DSF4442_rt.thumb.jpg">
      <figcaption>RawTherapee<br>
      dehaze produces hue shift that is hard to fix<br>
      does not hide cropped-out image?</figcaption>
    </figure>
    <figure>
      <img src="/static/2022-10/DSF4442_sp.thumb.jpg">
      <figcaption>Silkypix Developer<br>
      pleasant rendering, but not very detailed<br>
      there does not seem to be a clarity-like slider?</figcaption>
    </figure>
    <figure>
      <img src="/static/2022-10/DSF4442_x7.thumb.jpg">
      <figcaption>Exposure X7<br>
      works very well in this image</figcaption>
    </figure>
    <figure>
      <img src="/static/2022-10/DSF4442_zp.thumb.jpg">
      <figcaption>Zoner Photo Studio<br>
      weirdly ineffective dehaze<br>
      contrast introduces strong saturation<br>
      ineffective and wormy denoising</figcaption>
    </figure>
  </div>
<p>Fujifilm X-T2 with XF70-300 @ 231mm 1/400s f/5.7 ISO200<br><a href="/static/2022-10/DSF4442.RAF">&#x1f4c2; DSF4442.RAF</a> (23.0 MB) <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/80x15.png" /></a></p>

Overall, most of these renderings turned out fine. But there are pretty substantial differences in denoising, haloing, and detail retention of the shadows specifically. Halos especially are a personal bug-bear of mine, where the sky above the horizon line brightens and (worse) the mountains below the horizon line darken. This is especially visible in ACDSee, ON1, and Zoner, and to a lesser extent in DxO, Lightroom, and RawTherapee.

There were also significant differences in noise removal. Especially ACDSee, Exposure, and Zoner had weirdly ineffective denoising, and were unusually difficult to balance against smearing and worms in Lightroom, ON1, and Silkypix. Colors were a bit difficult to control in ACDSee, ON1, and RawTherapee.

The most pleasant renderings to my eye are DxO, Exposure, and Darktable in this round, although many of the others are very usable as well.

## High Key Rendering

Contrary to the popular style at moment, I sometimes like my highlights a little blown. I especially like a smooth, desaturated, film-like drop-off in my highlights, which seems strangely difficult to replicate in digital photography.

So instead of turning the following picture into an HDR hellscape, I want to compress the bright background into the highlights, while expanding the dark foreground to fill the midtones. The capture actually has all highlight information intact, so I don't want to blow anything out completely, just gracefully fade it into pastels.

<br>
  <div class="lightbox" style="height: 200px">
    <figure>
      <img src="/static/2022-10/DSCF0190_acd_safe.thumb.jpg">
      <figcaption>ACDSee Photo Studio<br>
      nice highlight rendering<br>
      very blotchy noise reduction in the shadows</figcaption>
    </figure>
    <figure>
      <img src="/static/2022-10/DSCF0190_c1_safe.thumb.jpg">
      <figcaption>Capture One<br>
      weirdly saturated trees<br>
      very noisy foreground</figcaption>
    </figure>
    <figure>
      <img src="/static/2022-10/DSCF0190_dt_safe.thumb.jpg">
      <figcaption>Darktable<br>
      default rendering horrendous<br>
      setting color preservation to luminance helps<br>
      weirdly saturated trees<br>
      very noisy foreground</figcaption>
    </figure>
    <figure>
      <img src="/static/2022-10/DSCF0190_dxo_safe.thumb.jpg">
      <figcaption>DxO PhotoLab<br>
      oversaturated by default (easy to fix)<br>
      good foreground brightness by default<br>
      strangly contrasty highlights</figcaption>
    </figure>
    <figure>
      <img src="/static/2022-10/DSCF0190_lr_safe.thumb.jpg">
      <figcaption>Lightroom Classic<br>
      trees remain unrealistically dark<br>
      noisy foreground</figcaption>
    </figure>
    <figure>
      <img src="/static/2022-10/DSCF0190_on1_safe.thumb.jpg">
      <figcaption>ON1 Photo RAW<br>
      trees remain unrealistically dark<br>
      unsightly HDR look</figcaption>
    </figure>
    <figure>
      <img src="/static/2022-10/DSCF0190_rt_safe.thumb.jpg">
      <figcaption>RawTherapee<br>
      terribly oversaturated trees</figcaption>
    </figure>
    <figure>
      <img src="/static/2022-10/DSCF0190_sp_safe.thumb.jpg">
      <figcaption>Silkypix Developer<br>
      shadows does not raise black point, remains dark<br>
      weird color areas in the sky</figcaption>
    </figure>
    <figure>
      <img src="/static/2022-10/DSCF0190_x7_safe.thumb.jpg">
      <figcaption>Exposure X7<br>
      strange color fringes on trees<br>
      highlights hard to deal with</figcaption>
    </figure>
    <figure>
      <img src="/static/2022-10/DSCF0190_zp_safe.thumb.jpg">
      <figcaption>Zoner Photo Studio<br>
      noisy foreground</figcaption>
    </figure>
  </div>
<p>Fujifilm X-Pro2 with XF16-80mm @ 16mm 1/400s f/9 ISO400<br>(no raw, for privacy reasons)</p>

The different renderings of this image are more of a matter of preference than any of the previous ones. To my eyes, I like the versions drawn by ACDSee, Capture One, Zoner Photo, and DxO PhotoLab best, and I recon that many of the other versions could have been improved with a little more manual tuning. The only problematic versions of this image were the strange HDR-like ON1 render, and the Silkypix variant with its lost black point.

## Summary

Overall, all of these programs seem reasonable tools for image editing. Most of their differences can probably be overcome if you learn them better. That said, this comparison has left me with a few clear favorites. To be clear, the above comparison only showed the most decisive images of a much larger set which informs my opinion. It should also be noted that my tastes in image editing do not focus on detail recovery, detailed masking, nontrivial retouching, or scene-changing edits such as wholesale sky swapping.

One area I am particularly interested in, however, is the inherent complexity of the editing tools: For example, I like my _saturation_ slider to only change saturation and leave lightness alone. Similarly, _contrast_ adjustments should not affect saturation. Another interesting part is the behavior of _highlights_ adjustments. Ideally, I'd like _highlights_ to be able to counteract _exposure_ adjustments so I can balance them against one another. Better yet if the same can be done with the _tone curve_.

|         Name        |    Editing is   | Export takes | Saturation changes overexposure? | Contrast changes lightness? | Highlights rescues overexposure? | Tonecurve rescues overexposure? |
| ------------------- | --------------- | ------------ | ------------------ | ---------------- | ------------------ | ----------------- |
| ACDSee Photo Studio | realtime        | 25s          | yes                | yes              | yes                | no                |
| Capture On          | realtime        | 15s          | a little           | no               | yes                | no                |
| Darktable           | delayed         | 15s          | no                 | no               | yes                | yes               |
| DxO PhotoLab        | delayed         | 45s          | yes                | a little         | yes                | a little          |
| Lightroom Classic   | realtime        | 15s          | a little           | a little         | yes                | a little          |
| ON1 Photo RAW       | realtime        | 30s          | yes                | a little         | no                 | no                |
| RawTherapee         | wait and see    | 30s          | a little           | yes              | no                 | no                |
| Silkypix Developer  | lo-res wait/see | 80s          | no                 | a little         | no                 | no                |
| Exposure X7         | realtime        | 30s          | yes                | strongly         | yes                | a little          |
| Zoner Photo Studio  | lo-res realtime | 30s          | yes                | yes              | yes                | a little          |

If _saturation_ changes lightness and _contrast_ changes saturation, editing can become rather more difficult, as the effect tends to be hard to counteract without complex luminosity masking. This is a reason for me to dislike my experience with ACDSee, ON1, Exposure, and Zoner particularly. The _highlights_ slider issue also has a big influence on how you edit images. If highlights can be recovered after exposure adjustments, you can use _exposure_ mostly for image brightness, and recover highlights later if needed. On the other hand, if highlights can't be recovered, then the _exposure_ slider must instead be used to protect highlights, and image brightness has to be relegated to the tone curve or shadows/midtones sliders. This feels weirdly backwards to me, and is a reason for me to disregard ON1, RawTherapee, and Silkypix.

The gold standard here is of course Darktable, where saturation ("chroma") is completely decoupled from lightness. And, as a particular point of pride, any module whatsoever can edit highlights without any risk of them blowing irretrievably. In practice, this actually simplifies development noticeably. The former is a bit of a double-edged sword, though, as _chroma_ of bright colors can only be pushed so far without going out of gamut; Darktable therefore provides a second _saturation_ control that additionally lowers brightness to keep bright colors in gamut, much like other tools.

You may also have noticed that the three examples pictures above were taken with Fujifilm cameras. These cameras are highly acclaimed for their film simulations. Of the tested software, Lightroom Classic, Silkypix Developer, Capture One, and ON1 Photo RAW natively support these film simulations. DxO PhotoLab can add them for an additional €139 [FilmPack](https://www.dxo.com/dxo-filmpack/). And ACDSee Photo Studio, RawTherapee, Darktable, and Exposure X7 at least support third-party LUTs which can retrofit film simulations. Funny how programs _either_ charge money for native film simulations, _or_ support generic LUTs. What a _coincidence_! (Only ON1 Photo RAW supports both film simulations and (ICC) LUTs, and only Zoner Photo Studio supports neither).

So, after spending a few evenings with these programs, what is my verdict?

### ACDSee Photo Studio Ultimate 2023 ★★★☆☆
Overall a rather good package. Fantastic organizational features, too. Even sports an API for extending its functionality! And pixel editing, a mobile app, and just a ton more.

However, it does not suit my tastes. Something about the UI and some tools seems a bit unpolished. Particularly, _clarity_ and _dehaze_ produce too strong halos for me, and the denoising is unpleasantly ineffective and smeary. Panning sometimes breaks the image into a pixelated mess, and there's no Fuji film sim support. Still, when it works, it produced some of my favorite renders in this comparison!

As another weird point, it's Windows only, and behaves oddly windowsy, too. For example, the library view by default shows all files and folders, not just images, and you actually need to reinstall the entire software if you want to change its language.

### Capture One 22 ★★★★★
A product I know well, and own a license for. This comparison has reinforced that choice. Capture One's image editing tools are somewhat basic, but they seem refined and flexible. There's a strong focus on workflow efficiency, too, with its [speed edit](https://learn.captureone.com/tutorials/speed-edit/) shortcuts and [style brushes](https://learn.captureone.com/tutorials/style-brushes/).

If there is a criticism to be leveled at Capture One, it's the high price and the somewhat slow pace of development. Many a competitors' feature is only included in Capture One years after they have become widespread. And many new features focus on the needs of working professional photographer instead of amateurs like me.

Regardless, Capture One will remain my one-of-two raw developer of choice. And it runs on my rather slow Surface tablet for emergency vacation edits!

### Darktable 4.0 ★★★★☆
Darktable is the other raw developer I know intimately. In a sense, it is the polar opposite of Capture One: all the algorithms, parameters, and details are laid bare; nothing is hidden or automated. Its editing tools are also by far the most unusual of this bunch, which must no doubt be bewildering to newcomers. But if you're interested in deep control and alternative editing workflows, there's just nothing like it. Personally, I have [scripted it](https://github.com/bastibe/Fujifilm-Auto-Settings-for-Darktable) and [molded it](https://bastibe.de/2022-05-04-customizing-darktable-for-fujifilm-cameras.html) extensively, which has made my Darktable similarly efficient and fast as Capture One. Such flexibility is actually rather rare in image editing software.

But I seriously hope they fix that horrendous highlights rendering of filmic v6 in the next revision. That's currently a constant pain point to work around.

Darktable will remain my one-of-two raw developer of choice. And it runs on Linux!

### DxO PhotoLab 6 ★★★★☆
This program really is what prompted this entire ordeal. I heard so many good things about DxO PhotoLab, and was planning on replacing Capture One with it after this comparison.

There truly is a lot to like about DxO PhotoLab. Its tools seem robust, its default rendering is often very close to a finished image, and its denoising is rather remarkable. However, the program just felt clunky to use. Things are organized inefficiently, some operations take annoyingly long to process, and some effects are only visible in a tiny preview window or indeed the exported file. The local adjustments also seemed unnecessarily cumbersome to use, with that weird radial menu and those awkwardly imprecise "Control Points".

And what's with the weirdly branded sliders all over the program? Why is it "DxO Smart Lighting" instead of shadows, "DxO ClearView Plus" instead of dehaze, and "Microcontrast" instead of clarity, and "DxO DeepPrime XD" instead of denoising?

Truthfully, I might still have bought a license for this program as it is powerful and fun to use, despite my complaints. But €220 for the main program _plus_ €140 for the FilmPack (for Fujifilm film simulations, but also basics such as a vignette tool) _plus_ €100 for ViewPoint (for cool distortion stuff, but also the keystone tool) is just a bit too much, thank you very much.

### Lightroom Classic 11.5 ★★★★☆
People like this program, and for good reason. Robust tools, a pleasant rendering, and just a staggering amount of tutorials and help online due to its popularity.

Nevertheless, Lightroom does not appeal to me. I don't like how Lightroom seems to takes undue possession of my images on import, I am repelled by the weird old-fashioned UI with its bonkers conventions (hold Alt to show masks, crop moves image instead of rectangle, etc.). I don't like its yearly-subscription-only pricing structure, either, although the price and terms are actually rather reasonable. And I don't like that Adobe Creative Cloud mothership that's necessary to install and maintain Lightroom.

But I do realize that this is actually good software. It's just not my favorite.

### ON1 Photo RAW 2023 ★★☆☆☆
The new AI denoising and sharpening produced only artifacts, the new AI masking completely missed my subjects, there were algorithm artifacts everywhere, such as halos, hue shifts, and clipping. Perhaps something about my version was broken, being a very recent release. Additionally, one time I wanted to do a 1:2 crop, which you have to create a new crop preset for. However, the preset will not be saved with a ":" in the name. It took me a few tries to figure out that that's what prevented me from cropping. It doesn't help that the UI is surprisingly slow, often taking a second or so to redraw a tool change. And the installer is 2.7 GB, three times the size of any other tool in this list!

On the other hand, there are some cool tools in the effects panel, and some renders actually didn't look half bad. Perhaps it just needs a few bugfixes or more polish. But as it stands, I can not recommend this software.

### RawTherapee 5.8 ★★★☆☆
I suppose RawTherapee should be regarded like Darktable, a killer program that requires deep study to wield well. I did not wield it well, but that probably says more about me than RawTherapee.

Still, I don't like the somewhat busy program layout, and how some operations take a long time to process. The export workflow is also strangely unusual, but I'm sure that that's something I could get used to. And I hear the next version will come with local adjustments.

Perhaps it is better-suited for a detail-oriented user than me. There's a lot to like here, but it's not what I'm looking for.

### Silkypix Developer Studio Pro 11 ★☆☆☆☆
Something about this program is endearing to me. But in this comparison, it was just more cumbersome than useful. Many of its tools simply were not up to the task (can't raise shadows far enough, denoising produces only artifacts). And at some point, it slowed down to the point where it would take several seconds to see the effects of a single slider movement. This program did not work for me.

### Exposure X7 ★★☆☆☆
Another strangely unpolished program on this list. Somehow, fonts everywhere are huge for no apparent reason, and sliders uncomfortably short. And I struggled preventing it from blowing highlights and clipping shadows. I don't see the appeal of this program.

### Zoner Photo Studio X Fall 2022 ★★★★☆
As of the most recent version, Zoner Photo finally added native support for some Fujifilm cameras. Not all of my cameras are included yet, but to their credit, Zoner Photo can still open the missing files through ACR, albeit a bit more slowly.

Really, there is a lot to like about this program. Most tools work as advertised, with few issues (no local white balance, somewhat ineffective denoising), and a strong automatic mode. I also enjoy how it is unapologetically Windows-only, and uniquely feels _native_ to Windows in a pleasant way.

It's a somewhat basic program compared to some of these others, but it's appropriately affordable, and fast. Not exactly what I'm looking for, but highly recommended for what it is!