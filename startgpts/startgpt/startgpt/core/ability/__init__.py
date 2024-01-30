"""The command system provides a way to extend the functionality of the AI agent."""
from startgpt.core.ability.base import Ability, AbilityConfiguration, AbilityRegistry
from startgpt.core.ability.schema import AbilityResult
from startgpt.core.ability.simple import (
    AbilityRegistryConfiguration,
    AbilityRegistrySettings,
    SimpleAbilityRegistry,
)

__all__ = [
    "Ability",
    "AbilityConfiguration",
    "AbilityRegistry",
    "AbilityResult",
    "AbilityRegistryConfiguration",
    "AbilityRegistrySettings",
    "SimpleAbilityRegistry",
]
