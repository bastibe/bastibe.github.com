---
title: Blogging with Pelican (and not Octopress)
date: 2012-07-18 21:11
filetags: blog
---

For a while now, I have been moving more and more services I use off Google. The reasons for that are manyfold, and few of them have anything to do with Google being evil or not--just to get that out of the way.

One of the last holdouts has been [my neglected Blogspot blog](http://web.archive.org/web/20210122194927/http://www.daskrachen.com/). And one of the reasons for it being neglected is that it was hosted on Blogspot. Now don't get me wrong here, Blogspot is a terriffic blogging platform. You have this very nice nearly-WYSIWYG text editor right in your browser, you can upload images, you can publish instantly to your blog... Basically everything is taken care of for you conveniently right there in your browser. Google Style.

Its just that I don't like to work that way. I like plain text. I like typing stuff into a plain text editor. I like to be in control. And Blogspot might be convenient, but it did not make me feel like I was in control. In fact, I lost at least one article to Blogspot for unknown reasons.

Enter static site generators. The idea is that instead of writing rich text into some website, you create you content however you want on your own computer, then use a static generator which converts it into a set of static HTML pages and upload those to your website. Now all of the creation process is happening on your computer. You are in control. Probably the most popular program to do that is [Jekyll](https://github.com/mojombo/jekyll).

The second part of the equation is some kind of publishing platform. With these static site generators, really any web server does that trick. Just push your generated HTML files to the server and be done with it. Even cooler is Github. Using [Github pages](http://pages.github.com/), you can use your existing Github account and infrastructure to publish your blog just by pushing the HTML to Github. This is seriously cool!

So, I set out and tried [Octopress](http://octopress.org/), which combines these two things into a nice blogging platform. Honestly though, I don't know much Ruby and all that `rake` workflow did not make me much more comfortable than pushing stuff into Blogspot.

Hence, I looked for alternatives. What I ended up with is [Pelican](http://pelican.notmyidea.org/), a very simple static site generator written in Python. Finally, this is a codebase that is easy enough for me to understand and modify. If there is any trouble with my blog, I will be (and have been) able to just look at the source code and figure out what is going wrong. I like this!

To publish a new blog post, I will start by writing the post in [Markdown](http://daringfireball.net/projects/markdown/) (a format I understand), process it using the very simple command line `pelican -s my_config_file.py posts/`, and push the result to GitHub. Easy as pie. And I feel like I am in control again!

Actually, if this is just a bit too technical for you, check out [Calepin](http://calepin.co/) instead. It uses the very same Pelican engine, but instead of fiddling with Git, you just put your markdown files into your Dropbox, and--poof--you magically have a Blog!

If you want to see my blog as a repo on Github, just [go have a look](https://github.com/bastibe/bastibe.github.com/) (the `master` branch contains the HTML, the `source` branch contains the configuration and Markdown).
