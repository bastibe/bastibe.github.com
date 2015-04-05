Alright, i have put this off too long.

I believe that I have been in pretty much your situation about a year ago. I was very happy with my Vim. I felt good in it, I was efficient, I had a few years of experience, a sophisticated setup, I was happy. That said, I was always wondering how they did it on the other side of the fence. Of course, I had tried Emacs some years earlier, but it did not stick back then. (Also, Textmate, Gedit, Sublime Text, Eclipse, Visual Studio, XCode)

So one day, I decided to give Emacs a serious shot. To cut this story short, I stuck with it to this day and would not want to go back. Here is what I think about that.

The thing is, Vim really *is* the better text editor. In terms of just editing text, I don't think Emacs can compete really. Vims mnemonics are better, they are more readily available and more combinable. 

But besides editing, Vim never really excels at managing buffers ("open files") or at finding files. Source code navigation is workable if you remember to rebuild your tags regularly, but that can be kind of a hassle. So there are fancy plugins like tagbar or nerdtree that give you an overview over files or folders. And they work well enough. Also, you can compile stuff and interact with source control systems, but these things are rarely more than thin wrappers around the command line. Really, I was usually more comfortable to just do these things in the command line itself and have an instance of Vim running alongside. All this usually made me prefer some Vim emulator within an IDE to just Vim for complex projects. I would loathe the IDE, but it just feels more effective.

Fast forward a year. Now I am using Emacs. I still use the IDE for compiling and debugging, but I code in Emacs. I am not quite as fast at editing as I was in my Vim days. But thanks to ido-mode, I jump between files at the speed of thought regardless of whether they are already opened, in the same directory or whatever. Also, I use split views constantly, while I used them sparingly in Vim.
And when I am done coding some feature, I have a quick glance at magit to commit my changes to git. Magit is this magical tool that wraps git in an amazing, visceral way. Honestly, it is the best interface to git I have ever seen (including the CLI, Tower and Github). Magit is unbelievable.
Once I am done with that, I go back to my org-mode file and mark the feature/bug I was working on as done. Again, org-mode has to be seen to be believaed. At its base it is an outliner, but it is also my bug tracker, my project planner, my organizer, my agenda, my todo list, and much more. Org is unbelievable.
Of course, I regularly update all my installed plugins using the built-in package manager. I used to have a similar setup using Vundle in Vim (If you don't know that, *do* check it out, it is great), but having a searchable list of available plugins makes all the difference to me. As an aside, you know what I do when I have to install Emacs on a new machine? I copy my `.emacs` file there and on the first run, Emacs will take care of the rest.

Lastly, I used to be wary of running Windows, because Vims dependance on external tools made it kind of hard to set up on Windows. I never quite managed to get a really great cross-platform setup going with Vim. With Emacs, I frankly don't care any more. Emacs works just fine on Windows, Linux and OSX. I don't even need an external shell because the built-in terminal emulator takes care of almost all I need.

Other tidbits:

* My Markdown files have different font sizes for headers and text.
* I use Emacs for iPython notebooks, complete with plotted graphs interspersed with my source code
* I sometimes use Emacs to render LaTeX, complete with inline figures and correctly typeset formulae and headlines.
* I occasionally use Emacs as an IRC client
* I occasionally use Emacs as a graphical debugger (friggin amazing, that!)
* I regularly use Emacs as a diff/merge program and it ROCKS!
* Sometimes I do some spreadsheet work in org-mode (astonishingly practical)
* Every once in a while, I open some PDFs or SVGs or images in Emacs
* As far as text editing goes, Emacs does pretty much everything that Vim does, but with slightly worse key bindings
* Once, I opened a shell in Emacs, then opened Emacs in that shell, then opened a shell in that Emacs, then... INCEPTION!

But keep in mind when reading this that this is only my particular setup. Other people use Emacs quite differently. Basically, Emacs can be pretty much anything you want it to be. This is the great difference to Vim: Vim is an awesome text editor, Emacs can be anything at all--including an awesome text editor. 