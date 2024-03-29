""" MacOS TTS Voice. """
from __future__ import annotations

import os
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from startgpt.config import Config

from startgpt.speech.base import VoiceBase


class MacOSTTS(VoiceBase):
    """MacOS TTS Voice."""

    def _setup(self, config: Config) -> None:
        pass

    def _speech(self, text: str, voice_index: int = 0) -> bool:
        """Play the given text."""
        if voice_index == 0:
            os.system(f'say "{text}"')
        elif voice_index == 1:
            os.system(f'say -v "Ava (Premium)" "{text}"')
        else:
            os.system(f'say -v Samantha "{text}"')
        return True
