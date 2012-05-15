Sublime Translate package
=========================

This packages replaces a set of characters with another set of characters or
strings.

How to install
--------------

**With Git**: Clone the repository in your Sublime Text 2 Packages folder.

	git clone git://github.com/avataru/Sublime-Translate.git

**Without Git**: Download the latest
[source from GitHub](https://github.com/avataru/Sublime-Translate) and copy the
whole Sublime-Translate folder into Sublime Text 2 Packages folder.

The easiest way to find the Sublime Text 2 Packages folder is to open Sublime
and go to Preferences > Browse Packages...

How to use
----------

Translate uses maps of characters that are "translated" to other characters or
strings. These maps are set in `Translate.sublime-settings`. Each set must have
a unique id. You can copy the settings file to the `Packages/User/` folder so
it won't be overwritten when you update the package.

To "translate" a piece of text, select it and then either right-click or go to
the Edit menu, "Translation maps" entry and select a set.

Default maps
------------

**Remove Romanian**: Removes Romanian characters.

**Romanian (dec)**: Converts Romanian characters to decimal HTML entities.

**Romanian (hex)**: Converts Romanian characters to hexadecimal HTML entities.

**Symbols**: Converts basic special characters to their HTML entities.

----------------------------------

License: [CC BY-NC-SA 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/)