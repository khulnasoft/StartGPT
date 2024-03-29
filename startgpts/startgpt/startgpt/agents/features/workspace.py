from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..base import BaseAgent

from startgpt.config import Config
from startgpt.workspace import Workspace


class WorkspaceMixin:
    """Mixin that adds workspace support to a class"""

    workspace: Workspace
    """Workspace that the agent has access to, e.g. for reading/writing files."""

    def __init__(self, **kwargs):
        # Initialize other bases first, because we need the config from BaseAgent
        super(WorkspaceMixin, self).__init__(**kwargs)

        config: Config = getattr(self, "config")
        if not isinstance(config, Config):
            raise ValueError(f"Cannot initialize Workspace for Agent without Config")
        if not config.workspace_path:
            raise ValueError(f"Cannot set up Workspace: no WORKSPACE_PATH in config")

        self.workspace = Workspace(config.workspace_path, config.restrict_to_workspace)


def get_agent_workspace(agent: BaseAgent) -> Workspace | None:
    if isinstance(agent, WorkspaceMixin):
        return agent.workspace

    return None
