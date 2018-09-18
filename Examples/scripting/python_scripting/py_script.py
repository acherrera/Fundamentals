#!/usr/bin/env python3

# imports here
import psutil       # Needed for kill process


def kill_process(pidfile_path=Path("example.pid")):
    try:
        pid = int(pidfile_path.read_text())
    except:

def make_output_dir():
    pass


def run_analytics():
    pass


def copy_to_current():
    pass


if __name__ == "__main__":
    kill_process()
    make_output_dir()
    run_analytics()
    copy_to_current()
