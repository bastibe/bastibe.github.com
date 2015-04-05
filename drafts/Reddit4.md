Well, for one it is a capable outliner.

That is, you have a document with a hierarchically organized tree of headlines with associated paragraphs (and formatting, and code blocks, tables and whatnot, but that is not the point). Think Markdown to get the basic idea. Basically, you can fold away every headline, at every level, thus only seeing an outline or part of a document. You can do similar things in Vim easily with folding. In org-mode, folding is bound simply to tab, because you use it constantly. The second part of being an outliner is, you can reorder the headlines and their associated paragraphs. Using Alt and one of the direction keys moves a headline up/down the hierarchy or up/down within items of the same level. Moving a headline moves all the children of the headline, too (other headlines, paragraphs of text...)

These two features sound trivial, but they in themselves are already surprisingly powerful. So far, this is little more than a fancy markdown-mode that can reorder hierarchical lists. (Of course reordering will re-number numbered lists, too, and it will work with folded-away trees etc.).

Next, you can assign each headline a status. On the most simple level, a status will be either TODO or DONE, but you can implement any kind of status workflow you like. A key combination toggles the status. Thus, you have a pretty fancy todo list. Additionally, every item can have a tag and a date. Use tags for people and dates for due-dates and you have quite a capable bug tracker. Emacs/org-mode also includes a calendar and fancy searching functions to view entries by tag or by date or in any way you would want.

So far, the text format is not much fancier than

~~~~
    * My Todo list
    ** TODO evil bug :tag:tag2:
       Long, arduous description of the bug.
    ** DONE check mail :tag:
~~~~

Next, org-mode has these cool checklists.

~~~~
    * A checklist [1/2] [50%]
       - [ ] this item is not done yet
       - [x] this item is done
~~~~	   

Whenever you update one of the check boxes or add new items, the summary updates. This can be combined with TODO statuses and all the other stuff. Handy.

And then there are all the other features such as the ability to insert links to any kind of resource, like other files (link to a line in a source file), links to another heading in the same file, link to websites, links to documents that open in external applications, scripts that should be executed... Anything, really. For example, I keep a list of TED talks I want to watch and I can simply go to the website by clicking the link in Emacs. I also keep some tabular data in Emacs. Basically, you write an ASCII-art table, but edit it just as you would edit an Excel spreadsheet. Org-Mode keeps everything tidied and all the lines aligned etc.. You can even do actual spreadsheet calculations in there, with functions and references and auto-updating dependencies and whatnot. Frankly though, I love the tables but if I need a spreadsheet, I use Excel.

Lastly, you can export these files to any amount of formats. This includes support for literate programming if you fancy that. There are people who have written their thesis in org-mode. And keep in mind that all this is done with simple text files.

I hope this gives you a rough idea of why org-mode can be crazy useful. I think that org-mode is something everybody would find useful if it were implemented in more places.
