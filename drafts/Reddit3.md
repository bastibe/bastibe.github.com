I could.

The key to it all is `ido-mode`. Ido-mode behaves much like CMD-T in Textmate or all the searchable lists in Sublime Text, that is, it narrows down a list by fuzzy-matching every entry of it with what you typed. (There are similar plugins for Vim if I am not mistaken).

First up: opening files. By default, Emacs opens files with `C-x C-f`. It thus presents you with a list of files in the current directory. With `ido-mode` you now have a nice way to open files in the current directory. The genius however is that if Emacs does not find a match in the current directory, it will start searching the history, across all files you opened recently. That means that in almost all cases, I hit `C-x C-f`, type some part of the file name and immediately get the file I want, regardless of its path or project dependency. This is pure gold for me.

Next, source code browsing. Admittedly, my solution here is comparatively crude, but it works for me. The idea is that I invoke a list of tags in the current file and use `ido-mode` to drill down to the place I am looking for. This works well if semantic knows how to parse the file (i.e. C++ and some others) and less so if it doesn't. In practice, it works well enough for most languages I use, including C++, Python and Lua. I am not quite sure why though, since Semantic certainly does not know Lua.
Anyway, to be able to do that, you need ido-goto-symbol, which I invoke using `C-c i`

If I don't know the code I am browsing, I use ECB to get a quick overview over all the functions etc. it declares. ECB is fairly awesome, but I tend to do use it less the more I know the code.

The great thing about all of this is that it works in pure elisp, without depending on ctags or etags. Thus, it knows to re-parse a file when I save it or when I updated it from magit. Also, it works "out of the box" on Windows.

Relevant .emacs section:

    ;; enable ido mode and fuzzy matching
    (ido-mode t)
    (setq ido-enable-flex-matching t)
    (load "ido-goto-symbol")
    (global-set-key "\C-ci" 'ido-goto-symbol) 