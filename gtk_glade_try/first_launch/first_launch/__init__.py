#

import sys
import os

if os.name == "nt":
    # To prevent us loading DLLs in the system directory which clash
    # with the ones we ship.
    from ctypes import windll

    windll.kernel32.SetDllDirectoryW(os.path.dirname(sys.executable))

import gettext
from .i18n import get_languages

__version_info__ = (0, 1, 0)
__version__ = ".".join(str(x) for x in __version_info__)

PkgDir = os.path.dirname(os.path.abspath(__file__))
localedir = os.path.join(PkgDir, "locale")
langs = get_languages()
translate = gettext.translation("first_launch", localedir, langs, fallback=True)
_ = translate.gettext
