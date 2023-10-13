# -*- coding: utf-8 -*-

"""
This file is part of the Mini Format Pack add-on for Anki.

Global variables

Copyright: (c) 2018 Glutanimate <https://glutanimate.com/>
License: GNU AGPLv3 <https://www.gnu.org/licenses/agpl.html>
"""

import re
import sys
import os
from anki import version

version_re = re.compile(r"^(?P<year>\d*)\.(?P<month>\d*)(\.(?P<patch>\d*))?$")
mo = version_re.search(version)
anki21 = version.startswith("2.1.") or int(mo.group("year")) >= 23
sys_encoding = sys.getfilesystemencoding()

if anki21:
    addon_path = os.path.dirname(__file__)
else:
    addon_path = os.path.dirname(__file__).decode(sys_encoding)
