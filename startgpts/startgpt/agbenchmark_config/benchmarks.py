import sys
from pathlib import Path

from startgpt.agents import Agent
from startgpt.app.main import run_interaction_loop
from startgpt.commands import COMMAND_CATEGORIES
from startgpt.config import AIConfig, ConfigBuilder
from startgpt.logs.config import configure_logging
from startgpt.memory.vector import get_memory
from startgpt.models.command_registry import CommandRegistry
from startgpt.prompts.prompt import DEFAULT_TRIGGERING_PROMPT
from startgpt.workspace import Workspace

PROJECT_DIR = Path().resolve()
LOG_DIR = Path(__file__).parent / "logs"


def run_specific_agent(task: str, continuous_mode: bool = False) -> None:
    agent = bootstrap_agent(task, continuous_mode)
    run_interaction_loop(agent)


def bootstrap_agent(task: str, continuous_mode: bool) -> Agent:
    config = ConfigBuilder.build_config_from_env(workdir=PROJECT_DIR)
    config.debug_mode = False
    config.continuous_mode = continuous_mode
    config.continuous_limit = 20
    config.temperature = 0
    config.noninteractive_mode = True
    config.plain_output = True
    config.memory_backend = "no_memory"
    config.workspace_path = Workspace.init_workspace_directory(config)
    config.file_logger_path = Workspace.build_file_logger_path(config.workspace_path)

    configure_logging(config, LOG_DIR)

    command_registry = CommandRegistry.with_command_modules(COMMAND_CATEGORIES, config)

    ai_config = AIConfig(
        ai_name="Start-GPT",
        ai_role="a multi-purpose AI assistant.",
        ai_goals=[task],
    )
    return Agent(
        memory=get_memory(config),
        command_registry=command_registry,
        ai_config=ai_config,
        config=config,
        triggering_prompt=DEFAULT_TRIGGERING_PROMPT,
    )


if __name__ == "__main__":
    # The first argument is the script name itself, second is the task
    if len(sys.argv) != 2:
        print("Usage: python script.py <task>")
        sys.exit(1)
    task = sys.argv[1]
    run_specific_agent(task, continuous_mode=True)
