import pytest
from git.exc import GitCommandError
from git.repo.base import Repo

from startgpt.agents.agent import Agent
from startgpt.agents.utils.exceptions import CommandExecutionError
from startgpt.commands.git_operations import clone_repository


@pytest.fixture
def mock_clone_from(mocker):
    return mocker.patch.object(Repo, "clone_from")


def test_clone_auto_gpt_repository(workspace, mock_clone_from, agent: Agent):
    mock_clone_from.return_value = None

    repo = "github.com/khulnasoft/Start-GPT.git"
    scheme = "https://"
    url = scheme + repo
    clone_path = workspace.get_path("auto-gpt-repo")

    expected_output = f"Cloned {url} to {clone_path}"

    clone_result = clone_repository(url=url, clone_path=clone_path, agent=agent)

    assert clone_result == expected_output
    mock_clone_from.assert_called_once_with(
        url=f"{scheme}{agent.config.github_username}:{agent.config.github_api_key}@{repo}",
        to_path=clone_path,
    )


def test_clone_repository_error(workspace, mock_clone_from, agent: Agent):
    url = "https://github.com/this-repository/does-not-exist.git"
    clone_path = workspace.get_path("does-not-exist")

    mock_clone_from.side_effect = GitCommandError(
        "clone", "fatal: repository not found", ""
    )

    with pytest.raises(CommandExecutionError):
        clone_repository(url=url, clone_path=clone_path, agent=agent)
