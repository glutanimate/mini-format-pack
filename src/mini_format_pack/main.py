# -*- coding: utf-8 -*-

"""
This file is part of the Mini Format Pack add-on for Anki.

Main Module, hooks add-on methods into Anki.

Copyright: (c) 2014-2018 Stefan van den Akker <neftas@protonmail.com>
           (c) 2017-2018 Damien Elmes <http://ichi2.net/contact.html>
           (c) 2018 Glutanimate <https://glutanimate.com/>
License: GNU AGPLv3 <https://www.gnu.org/licenses/agpl.html>
"""


from aqt import mw
from aqt.qt import *
from anki.hooks import addHook
from anki.utils import isWin, isMac

from .consts import addon_path

# Config


def getConfig():
    return mw.addonManager.getConfig(__name__)


# Format Functions

def insertOrderedList(editor):
    editor.web.eval("setFormat('insertOrderedList')")


def insertUnorderedList(editor):
    editor.web.eval("setFormat('insertUnorderedList')")


def strikeThrough(editor):
    editor.web.eval("setFormat('strikeThrough')")


def indent(editor):
    editor.web.eval("setFormat('indent')")


def outdent(editor):
    editor.web.eval("setFormat('outdent')")


def formatBlockPre(editor):
    editor.web.eval("setFormat('formatBlock', 'pre')")


def insertHorizontalRule(editor):
    editor.web.eval("setFormat('insertHorizontalRule')")


def justifyCenter(editor):
    editor.web.eval("setFormat('justifyCenter');")


def justifyLeft(editor):
    editor.web.eval("setFormat('justifyLeft');")


def justifyRight(editor):
    editor.web.eval("setFormat('justifyRight');")


def justifyFull(editor):
    editor.web.eval("setFormat('justifyFull');")


# Special format functions

# Background colour
######################################################################

def setupBackgroundButton(editor):
    editor.bcolour = editor.mw.pm.profile.get("lastBgColor", "#00f")
    onBgColourChanged(editor)

# use last colour


def onBackground(editor):
    _wrapWithBgColour(editor, editor.bcolour)

# choose new colour


def onChangeBgCol(editor):
    new = QColorDialog.getColor(QColor(editor.bcolour), None)
    # native dialog doesn't refocus us for some reason
    editor.parentWindow.activateWindow()
    if new.isValid():
        editor.bcolour = new.name()
        onBgColourChanged(editor)
        _wrapWithBgColour(editor, editor.bcolour)


def _updateBackgroundButton(editor):
    editor.web.eval(
        """$("#backcolor")[0].style.backgroundColor = '%s'""" % editor.bcolour)


def onBgColourChanged(editor):
    _updateBackgroundButton(editor)
    editor.mw.pm.profile['lastBgColor'] = editor.bcolour


def _wrapWithBgColour(editor, color):
    """
    Wrap the selected text in an appropriate tag with a background color.
    """
    # On Linux, the standard 'hiliteColor' method works. On Windows and OSX
    # the formatting seems to get filtered out

    editor.web.eval("""
        if (!setFormat('hiliteColor', '%s')) {
            setFormat('backcolor', '%s');
        }
        """ % (color, color))

    if isWin or isMac:
        # remove all Apple style classes, which is needed for
        # text highlighting on platforms other than Linux
        editor.web.eval("""
            var matches = document.querySelectorAll(".Apple-style-span");
            for (var i = 0; i < matches.length; i++) {
                matches[i].removeAttribute("class");
            }
        """)


# UI element creation

def createCustomButton(editor, name, tooltip, hotkey, method):
    if name == "onBackground":
        editor._links[name] = method
        QShortcut(QKeySequence(hotkey), editor.widget,
                  activated=lambda s=editor: method(s))
        return '''<button tabindex=-1 class=linkb title="{}"
                    type="button" onclick="pycmd('{}');return false;">
                    <div id=backcolor style="display:inline-block; background: #000;border-radius: 5px;"
                    class=topbut></div></button>'''.format("{} ({})".format(tooltip, hotkey), name)
    return ""


# Hooks

def onLoadNote(editor):
    setupBackgroundButton(editor)


def onSetupButtons(buttons, editor):
    """Add buttons to Editor for Anki 2.1.x"""

    actions = getConfig().get("actions", None)

    if not actions:
        return buttons

    for action in actions:
        try:
            name = action["name"]
            tooltip = action["tooltip"]
            label = action.get("label", "")
            hotkey = action["hotkey"]
            method = globals().get(name)
        except KeyError:
            print("Simple Format Pack: Action not configured properly:", action)
            continue

        icon_path = os.path.join(addon_path, "icons", "{}.png".format(name))
        if not os.path.exists(icon_path):
            icon_path = ""

        if action.get("custom", False):
            b = createCustomButton(editor, name, tooltip, hotkey, method)
        else:
            b = editor.addButton(icon_path, name, method,
                                 tip="{} ({})".format(tooltip, hotkey),
                                 label="" if icon_path else label,
                                 keys=hotkey)

        buttons.append(b)

    return buttons


addHook("loadNote", onLoadNote)
addHook("setupEditorButtons", onSetupButtons)
