import pathlib

import click
import yaml
from agent_protocol import Agent as AgentProtocol

from startgpt.core.runner.cli_web_app.server.api import task_handler
from startgpt.core.runner.client_lib.shared_click_commands import (
    DEFAULT_SETTINGS_FILE,
    make_settings,
)
from startgpt.core.runner.client_lib.utils import coroutine


@click.group()
def startgpt():
    """Temporary command group for v2 commands."""
    pass


startgpt.add_command(make_settings)


@startgpt.command()
@click.option(
    "port",
    "--port",
    default=8080,
    help="The port of the webserver.",
    type=click.INT,
)
def server(port: int) -> None:
    """Run the StartGPT runner httpserver."""
    click.echo("Running StartGPT runner httpserver...")
    AgentProtocol.handle_task(task_handler).start(port)


@startgpt.command()
@click.option(
    "--settings-file",
    type=click.Path(),
    default=DEFAULT_SETTINGS_FILE,
)
@coroutine
async def client(settings_file) -> None:
    """Run the StartGPT runner client."""
    settings_file = pathlib.Path(settings_file)
    settings = {}
    if settings_file.exists():
        settings = yaml.safe_load(settings_file.read_text())

    settings
    # TODO: Call the API server with the settings and task,
    #   using the Python API client for agent protocol.


if __name__ == "__main__":
    startgpt()
