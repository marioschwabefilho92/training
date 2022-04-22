#!/usr/bin/env python

import os
import locale


def get_languages():
    """
    Return a list of languages as a substitute
    for the LANGUAGE environment variable.
    On Posix systems or if no language setting
    can be determined, return None.
    """

    if os.name == "nt":
        from .winapi import GetUserDefaultUILanguage, GetSystemDefaultUILanguage

        langs = list(
            filter(
                None,
                map(
                    locale.windows_locale.get,
                    [GetUserDefaultUILanguage(), GetSystemDefaultUILanguage()],
                ),
            )
        )
        if langs:
            if not os.getenv("LANG"):
                os.putenv("LANG", langs[0])
            if os.getenv("LANGUAGE"):
                return
            # Üblicherweise fehlt eine explizite Übersetzung
            # von 'en'. gettext() nimmt dann aber nicht den
            # unübersetzten Text, sondern geht zum Nächsten
            # in der Liste. Wir lassen deshalb auf jedes 'en'
            # ein 'C' folgen, das (undokumentiert) 'unüber-
            # setzt' auswählt.
            nlangs = []
            for lang in langs:
                nlangs.append(lang)
                if lang.startswith("en"):
                    nlangs.append("C")
            return nlangs
    return None
