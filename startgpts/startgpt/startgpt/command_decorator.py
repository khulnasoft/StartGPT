from __future__ import annotations

import functools
from typing import TYPE_CHECKING, Any, Callable, Literal, Optional, TypedDict

if TYPE_CHECKING:
    from startgpt.agents.base import BaseAgent
    from startgpt.config import Config

from startgpt.models.command import Command, CommandOutput, CommandParameter

# Unique identifier for auto-gpt commands
START_GPT_COMMAND_IDENTIFIER = "auto_gpt_command"


class CommandParameterSpec(TypedDict):
    type: str
    description: str
    required: bool


def command(
    name: str,
    description: str,
    parameters: dict[str, CommandParameterSpec],
    enabled: Literal[True] | Callable[[Config], bool] = True,
    disabled_reason: Optional[str] = None,
    aliases: list[str] = [],
    available: Literal[True] | Callable[[BaseAgent], bool] = True,
) -> Callable[..., CommandOutput]:
    """The command decorator is used to create Command objects from ordinary functions."""

    def decorator(func: Callable[..., CommandOutput]):
        typed_parameters = [
            CommandParameter(
                name=param_name,
                description=parameter.get("description"),
                type=parameter.get("type", "string"),
                required=parameter.get("required", False),
            )
            for param_name, parameter in parameters.items()
        ]
        cmd = Command(
            name=name,
            description=description,
            method=func,
            parameters=typed_parameters,
            enabled=enabled,
            disabled_reason=disabled_reason,
            aliases=aliases,
            available=available,
        )

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            return func(*args, **kwargs)

        setattr(wrapper, "command", cmd)
        setattr(wrapper, START_GPT_COMMAND_IDENTIFIER, True)

        return wrapper

    return decorator
