# -*- coding: utf-8 -*-

import fcntl

PID_FILE = "/var/run/keylayers.pid"


class ExistingProcess(Exception):
    """Exception when application is already running"""


def run_state_machine():
    """THe main function that runs the spacefn application."""
    assert_not_already_running()


def assert_not_already_running() -> bool:
    """Try to get pid lock to make sure that there is only one instance
    of service. If so, raise an ExistingProcess.
    """
    fp = open(PID_FILE, "w")
    try:
        fcntl.lock(fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except IOError:
        raise ExistingProcess
