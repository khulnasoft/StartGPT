from __future__ import annotations

import logging
import os
from typing import TYPE_CHECKING

import requests
from playsound import playsound

if TYPE_CHECKING:
    from startgpt.config import Config

from startgpt.speech.base import VoiceBase

logger = logging.getLogger(__name__)


class StreamElementsSpeech(VoiceBase):
    """Streamelements speech module for startgpt"""

    def _setup(self, config: Config) -> None:
        """Setup the voices, API key, etc."""
        self.config = config

    def _speech(self, text: str, voice: str, _: int = 0) -> bool:
        voice = self.config.streamelements_voice
        """Speak text using the streamelements API

        Args:
            text (str): The text to speak
            voice (str): The voice to use

        Returns:
            bool: True if the request was successful, False otherwise
        """
        tts_url = (
            f"https://api.streamelements.com/kappa/v2/speech?voice={voice}&text={text}"
        )
        response = requests.get(tts_url)

        if response.status_code == 200:
            with open("speech.mp3", "wb") as f:
                f.write(response.content)
            playsound("speech.mp3")
            os.remove("speech.mp3")
            return True
        else:
            logger.error(
                "Request failed with status code: %s, response content: %s",
                response.status_code,
                response.content,
            )
            return False
