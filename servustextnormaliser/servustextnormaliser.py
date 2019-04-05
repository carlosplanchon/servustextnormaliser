#!/usr/bin/env python3

from removeurl import remove_url
from removeaccents import remove_accents

from servussimplifytext import simplify_text, simplify_text_no_symbols

from contractions import fix


class TextNormaliser:
    def __init__(self) -> None:
        self.remove_accents = True
        self.remove_links = True
        self.remove_contractions = True
        self.no_symbols = True
        self.remove_non_ascii_characters = True

    def normalise(self, text: str) -> str:
        # We remove tildes before strange symbols.
        if self.remove_accents:
            text = remove_accents(text)

        if self.remove_links:
            text = remove_url(text)

        if self.remove_contractions:
            text = fix(text)

        if self.remove_non_ascii_characters:
            if self.no_symbols:
                text = simplify_text_no_symbols(text)
            else:
                text = simplify_text(text)

        return text
