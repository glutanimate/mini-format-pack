# -*- coding: utf-8 -*-

# Mini Format Pack Add-on for Anki
#
# Copyright: (c) 2018-2023 Glutanimate and contributors
#                <https://glutanimate.com/>
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


from typing import TYPE_CHECKING, Dict, Any, Optional


if TYPE_CHECKING:
    from aqt.addons import AddonManager
    from aqt.main import AnkiQt

IMPORT_ERRORS = (ImportError, ModuleNotFoundError)

__all__ = ["is_mac", "is_win"]

try:
    from anki.utils import is_mac, is_win
except IMPORT_ERRORS:
    from anki.utils import isMac as is_mac  # type: ignore[attr-defined, no-redef]
    from anki.utils import isWin as is_win  # type: ignore[attr-defined, no-redef]


def config_getter_factory(addon_manager: "AddonManager", package_name: str):
    """Factory function for getting add-on config"""

    def get_config() -> Dict[str, Any]:
        """Get add-on config"""
        return addon_manager.getConfig(package_name) or {}

    return get_config


def get_anki_profile(main_window: "AnkiQt") -> Dict[str, Any]:
    """Get Anki profile name"""
    return main_window.pm.profile or {}
