# -*- coding: utf-8 -*-

"""Console script for keylayers."""
import sys
import click
import fcntl
from .service import run_state_machine, ExistingProcess


@click.group()
def main(args=None):
    """Console script for keylayers."""
    click.echo("Replace this message by putting your code into " "keylayers.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    try:
        run_state_machine()
    except ExistingProcess


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
