# -*- coding: utf-8 -*-

"""Console script for keylayers."""
import sys
import click
import fcntl
from .service import run_state_machine, ExistingProcess


@click.group()
def cli(args=None):
    """Tool for creating keyboard layers in *nix systems"""


@cli.command(help="Start the keylayers service if it has not yet been started.")
def run():
    """Start the keylayer service."""
    try:
        run_state_machine()
    except ExistingProcess:
        click.echo("keylayers is already running.")
        return 0


if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover
