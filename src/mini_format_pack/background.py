# -*- coding: utf-8 -*-

# Mini Format Pack Add-on for Anki
#
# Copyright: (c) 2014-2018 Stefan van den Akker <neftas@protonmail.com>
#            (c) 2017-2018 Damien Elmes <http://ichi2.net/contact.html>
#            (c) 2018-2023 Glutanimate and contributors <https://glutanimate.com/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version, with the additions
# listed at the end of the license file that accompanied this program.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# NOTE: This program is subject to certain additional terms pursuant to
# Section 7 of the GNU Affero General Public License.  You should have
# received a copy of these additional terms immediately following the
# terms and conditions of the GNU Affero General Public License that
# accompanied this program.
#
# If not, please request a copy through one of the means of contact
# listed here: <https://glutanimate.com/contact/>.
#
# Any modifications to this file must keep this entire header intact.

from typing import TYPE_CHECKING

from aqt.qt import QColor, QColorDialog

from .anki import get_anki_profile, is_mac, is_win

if TYPE_CHECKING:
    from aqt.editor import Editor, EditorWebView


# Formatters


def highlight_with_existing_color(editor: "Editor", editor_webview: "EditorWebView"):
    current_color = get_background_color(editor)
    wrap_selection_with_background_color(editor_webview, current_color)


def pick_color_and_highlight(editor):
    editor_webview = editor.web
    if editor_webview is None:
        print("Mini Format Pack: No webview found. Aborting.")
        return

    current_color = get_background_color(editor)
    new_qcolor = QColorDialog.getColor(QColor(current_color), None)

    # native dialog doesn't refocus us for some reason
    editor.parentWindow.activateWindow()

    if not new_qcolor.isValid():
        return

    new_color = new_qcolor.name()

    set_background_color(editor, new_color)
    update_background_color_ui(editor)

    wrap_selection_with_background_color(editor_webview, new_color)


# UI updates


def update_background_color_ui(editor: "Editor"):
    current_color = get_background_color(editor)
    editor_webview = editor.web
    if editor_webview is None:
        return
    editor_webview.eval(f"""\
require("anki/ui").loaded.then(() => {{
document.getElementById("backcolor").style.backgroundColor = '{current_color}'
}});""")


# Utility


def get_background_color(editor: "Editor"):
    main_window = editor.mw
    return get_anki_profile(main_window).get("lastBgColor", "#00f")


def set_background_color(editor: "Editor", color: str):
    main_window = editor.mw
    get_anki_profile(main_window)["lastBgColor"] = color


def wrap_selection_with_background_color(editor_webview: "EditorWebView", color: str):
    """
    Wrap the selected text in an appropriate tag with a background color.
    """
    # On Linux, the standard 'hiliteColor' method works. On Windows and OSX
    # the formatting seems to get filtered out

    editor_webview.eval("""
        if (!setFormat('hiliteColor', '%s')) {
            setFormat('backcolor', '%s');
        }
        """ % (color, color))

    if is_win or is_mac:
        # remove all Apple style classes, which is needed for
        # text highlighting on platforms other than Linux
        editor_webview.eval("""
            var matches = document.querySelectorAll(".Apple-style-span");
            for (var i = 0; i < matches.length; i++) {
                matches[i].removeAttribute("class");
            }
        """)
