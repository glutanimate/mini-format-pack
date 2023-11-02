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


import os
from typing import TYPE_CHECKING, List

from aqt import mw
from aqt.gui_hooks import editor_did_init_buttons
from aqt.qt import QKeySequence, QShortcut

from .anki import config_getter_factory
from .consts import addon_path
from .formatters import FORMATTERS

if TYPE_CHECKING:
    assert mw is not None
    from aqt.editor import Editor

# Config


get_config = config_getter_factory(mw.addonManager, __name__)


# UI element creation


def create_custom_button(editor, name, tooltip, hotkey, method):
    if name == "onBackground":
        editor._links[name] = method
        shortcut = QShortcut(QKeySequence(hotkey), editor.widget)
        shortcut.activated.connect(lambda editor=editor: method(editor))
        return """<button tabindex=-1 class=linkb title="{}"
                    type="button" onclick="pycmd('{}');return false;">
                    <div id=backcolor style="display:inline-block; background: #000;border-radius: 5px;"
                    class=topbut></div></button>""".format(
            "{} ({})".format(tooltip, hotkey), name
        )
    return ""


# Hooks


def on_setup_buttons(buttons: List[str], editor: "Editor"):
    """Add buttons to Editor for Anki 2.1.x"""

    if editor.web is None:
        return

    actions = get_config().get("actions", None)

    if not actions:
        return

    for action in actions:
        try:
            name = action["name"]
            tooltip = action["tooltip"]
            label = action.get("label", "")
            hotkey = action["hotkey"]
        except KeyError:
            print("Mini Format Pack: Action not configured properly:", action)
            continue

        formatter = FORMATTERS.get(name)

        if formatter is None or not callable(formatter):
            print("Mini Format Pack: Method not found:", name)
            continue

        def wrapper(editor=editor, formatter=formatter):
            if editor.web is None:
                print("Mini Format Pack: Editor webview not properly initialized")
                return
            formatter(editor, editor.web)

        icon_path = os.path.join(addon_path, "icons", "{}.png".format(name))
        if not os.path.exists(icon_path):
            icon_path = ""

        if action.get("custom", False):
            button = create_custom_button(editor, name, tooltip, hotkey, wrapper)
        else:
            button = editor.addButton(
                icon_path,
                name,
                wrapper,
                tip="{} ({})".format(tooltip, hotkey),
                label="" if icon_path else label,
                keys=hotkey,
            )

        buttons.append(button)


editor_did_init_buttons.append(on_setup_buttons)
