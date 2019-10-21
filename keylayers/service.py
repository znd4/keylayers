# -*- coding: utf-8 -*-

import fcntl

PID_FILE = "/var/run/keylayers.pid"


class ExistingProcess(Exception):
    """Exception when application is already running"""


def run_state_machine():
    """THe main function that runs the spacefn application."""
    is_already_running()


def is_already_running() -> bool:
    """Try to get pid lock to make sure that there is only one instance
    of service.
    """
    fp = open(PID_FILE, "w")
    try:
        fcntl.lock(fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except IOError:
        raise ExistingProcess
