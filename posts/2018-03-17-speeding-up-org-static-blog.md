---
title: Speeding up org-static-blog
date: 2018-03-17 00:00
filetags: org-mode emacs blog
---

Three years ago, I had enough of all the static site generators out there. Over the life of this blog, I had used [Octopress, then Pelican](http://bastibe.de/2012-07-18-blogging-with-pelican.html), then [Coleslaw](http://bastibe.de/2013-11-13-blogging-with-emacs.html), then [org-mode](http://bastibe.de/2014-05-07-speeding-up-org-publishing.html), and then wrote my own static site generator, [org-static-blog](https://github.com/bastibe/org-static-blog). Above all, org-static-blog is _simple_. It iterates over all *.org files in `org-static-blog-posts-directory`, and then exports all of these files to HTML. Simple is good. Simple is reliable. Simple means I can fix things.

However, simple can also mean inefficient. Most glaringly, org-static-blog exports every single blog post three times every time you publish: Once to render the HTML, then once to render the RSS feed, then once to render the Index and Archive pages.

Today, I finally tackled this problem: Now, org-static-blog only exports each post once, when the *.org file changes. The RSS feed, the Index page, and the Archive page simply read the already-rendered HTML instead of exporting again.

Thus, a full rebuild of this blog and all of its 85 posts used to take 2:12 min, and now takes 42 s. More importantly, if only one org file changed, the rebuild used to take 1:08 min, and now takes 1.5 s. Things like this are hugely satisfying to me!
