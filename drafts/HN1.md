There are really really great Git GUIs out there. Tower is the one example everyone is citing. That said, Tower is a largely transparent wrapper around the git command line. Pretty much every button corresponds to one and only one command in the terminal. All it really does is to give you visual feedback and meta-information on what you are doing.
This works really well. You have to understand Git in order to use it efficiently, but once you do it is in many cases just a more convenient way of using Git. Well, and then it knows to do a `stash/pull --rebase/stash pop` instead of a simple pull if you want to.
On the very other end of the spectrum is Github for Windows, which literally only has one button "Sync" for all that is pull, push, fetch, rebase etc. It is a giant PITA. Also, it does have an interactive commit view with files and checkboxes BUT IT DOES NOT STAGE STUFF WHEN YOU CHECK THE BOXES. This drives me nuts! Also, it trips up and dies if you stage stuff externally. I die a little every time that app breaks something.
Thus, I don't have anything against VC GUIs at all as long as they stay true to the command line. But any kind of abstraction is bound to leak at some point. This might be OK in some places, but your VC is not the right place to store leaked Git abstractions.
In many other places though, command line abstractions work just fine. Maybe this is more a comment about Git being hard to abstract than an argument against abstracting command line tools in general. And maybe that does not say anything good about Git.