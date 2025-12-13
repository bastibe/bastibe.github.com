---
title: Multi-Font Themes in Emacs
date: 2017-09-19 00:00
filetags: emacs
---

Traditionally, text editor themes are all about colors, right? In programming, we use color to tell variables from type declarations, comments, or strings. However, any other text document uses typography instead of color to distinguish between headlines, list items, and keywords. I think that our current approach to highlighting code is misguided.

I think that color themes are an accident of history. Terminal text editors are unable to switch fonts. All they can do is switch colors, so colors is all we use. But in todays graphical world, we are no longer bound by the shackles of terminals, and Emacs can switch fonts just as easily as colors[^editors].

It all started about a year ago, when I fell in love with a font called [PragmataPro](https://www.fsd.it/shop/fonts/pragmatapro/). One of the coolest features of Pragmata was its native bold and italic letters, and its wide support for unicode symbols. I had to find a use for these features! And so, down the rabbit hole I went. **Keywords** should be bold! _# Comments_ should be italic! And while we're at it, why not add some _underlines_? And so on.

The logical next step was then to get rid of colors altogether. At first, as an experiment. Do I really _need_ colors in code? The very pretty [eink theme](https://github.com/maio/eink-emacs) seemed to claim otherwise. After a few months of this lunacy, I realized that while I didn't strictly _need_ colors, the stylistic variations of just one font aren't quite sufficient for source code. In particular, it wasn't always easy to distinguish between italic and roman type in PragmataPro, which lead to some confusion.

But then, inspiration hit me: Who says that I could only use one single font? No one!

![color%20theme](http://bastibe.de/static/2017-09/color%20theme.png)

The tricky bit is to find fonts that work well together. In this example, I'm using PragmataPro for all regular code, [Iosevka](https://be5invis.github.io/Iosevka/) Slab[^slab] for strings, and oblique[^obl] Iosevka for comments. [Ubuntu Mono](http:_font.ubuntu.com_) and [InputCompressed](http:_input.fontbureau.com_) work well, too. You can find my current theme [on Github](https://github.com/bastibe/.emacs.d/blob/master/lisp/my-eink-theme.el). The only downside is that while these fonts share the character width, the heights differ slightly, which sometimes leads to uneven line heights.

Still, I love the look of this! (Of course it won't work in a terminal, or most other text editors.)

[^editors]: Can other text editors do this? I honestly have no idea.
[^slab]: I just love the look of the slab-serif characters in Iosevka! Look at the beautiful `"}"` in the screenshot!
[^obl]: not to be confused with _italic_, which changes glyphs in addition to slanting.
