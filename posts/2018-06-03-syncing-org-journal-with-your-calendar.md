---
title: Syncing Org-Journal with your Calendar
date: 2018-06-03 10:28
filetags: org-journal
---

[A month ago](https://bastibe.de/2018-04-02-scheduling-future-todos-in-org-journal.html), org-journal learned to deal with future journal entries. I use future journal entries for appointments or not-yet-actionable tasks that I don't want in my current TODO list just yet. This works really well while I am at my computer, and really does not work at all when I am not ([Orgzly](http:_www.orgzly.com_) does _not_ work with my 1k-file journal directory).

But, as I keep re-discovering, org-mode already has a solution for this: org-mode can export your agenda to an iCalendar file! Most calendar applications can then subscribe to that file, and show your future journal entries right in your calendar. And if you set it up right, this will even sync changes to your calendar!

First, you need to set up some kind of regular export job. I use a cron job that regularly runs an Emacs batch job `emacs --batch --script ~/bin/calendar_init.el` with the following code in _calendar​_init.el_:

```elisp
;; no init file is loaded, so provide everything here:
(add-to-list 'load-path "~/etc/org-journal/")
(setq org-journal-dir "~/journal/"            ; where my journal files are
      org-journal-file-format "%Y-%m-%d.org"  ; their file names
      org-journal-enable-agenda-integration t ; so entries are on the agenda
      org-icalendar-store-UID t               ; so changes sync correctly
      org-icalendar-include-todo "all"        ; include TODOs and DONEs
      org-icalendar-combined-agenda-file "~/calendar/org-journal.ics")

(require 'org-journal)
(org-journal-update-org-agenda-files) ; put future entries on the agenda
(org-icalendar-combine-agenda-files)  ; export the ICS file
(save-buffers-kill-emacs t)           ; save all modified files and exit
```

It is important to set `org-icalendar-store-UID`, as otherwise every change to a future entry would result in a duplicated calendar entry. It will clutter up your journal entries with an `UID` property, though.

I do this on my web server, with my journal files [syncthing](https:_syncthing.net_)ed from my other computers. With that, I can subscribe to the calendar file from any internet-connected computer or mobile phone (using [ICSdroid](https:_icsdroid.bitfire.at_)). But you could just as well sync only the ICS file, or just subscribe to the local file, if you don't want to upload your complete yournal to a web server.

(Incidentally, I first implemented my own ICS export, before realizing that this functionality already existed in org-mode. It was a fun little project, and I learned a lot about org-mode's internal data structures and the weirdness that are iCalendar files.)
