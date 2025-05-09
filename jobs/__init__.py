"""Nautobot Jobs."""

from .dyanamic_inputs import Example

from nautobot.apps.jobs import register_jobs

jobs = [Example]

register_jobs(*jobs)
