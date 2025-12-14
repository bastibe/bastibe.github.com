---
title: Blogging with org-static-blog (Updated)
date: 2018-03-22 08:37
filetags: blog
---

A while ago, I scratched an old itch and wrote my own static site generator, called [org-static-blog](https://github.com/bastibe/org-static-blog). It is a simple thing: You hand it a directory full of *.org files with a `#+title:` and `#+date:`, and it assembles a bunch of HTML pages and an RSS feed from them. There are no external dependencies beyond Emacs.

Today, I [released](http://melpa-stable.milkbox.net/#/org-static-blog) version 1.1.0 of org-static-blog, which introduces two new features: [speed](http://bastibe.de/2018-03-17-speeding-up-org-static-blog.html), and tags. You can now—optionally—add `#+filetags:` to your *.org files, `(setq org-static-blog-enable-tags t)`, and org-static-blog will add tag links to every blog post, create tag indices, and add `<category>` tags to the RSS feed.

*Update:*

As [Kaushal Modi](https://github.com/kaushalmodi) pointed out in the comments, org-mode uses `#+filetags:` to set tags for entire files. My first implementation used `#+tags:`. This is now deprecated. `#+tags:` still works, but issues a warning, and will be removed in the future. Sorry for the inconvenience.
