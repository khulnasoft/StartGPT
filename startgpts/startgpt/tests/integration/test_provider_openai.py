from unittest.mock import MagicMock, patch

import pytest

from startgpt.llm.api_manager import ApiManager
from startgpt.llm.providers import openai

api_manager = ApiManager()


@pytest.fixture(autouse=True)
def reset_api_manager():
    api_manager.reset()
    yield


def test_create_chat_completion_empty_messages():
    """Test if empty messages result in zero tokens and cost."""
    messages = []
    model = "gpt-3.5-turbo"

    with patch("openai.ChatCompletion.create") as mock_create:
        mock_response = MagicMock()
        del mock_response.error
        mock_response.usage.prompt_tokens = 0
        mock_response.usage.completion_tokens = 0
        mock_create.return_value = mock_response

        openai.create_chat_completion(messages, model=model)

        assert api_manager.get_total_prompt_tokens() == 0
        assert api_manager.get_total_completion_tokens() == 0
        assert api_manager.get_total_cost() == 0
