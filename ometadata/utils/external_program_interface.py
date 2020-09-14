
from shlex import quote
from shutil import which
from subprocess import run

from ometadata.utils.custom_types import CLIargs


def kwargs_to_cli_args(**arg_dict: str) -> CLIargs:
    args = [f"--{key}={quote(val)}" for key, val in arg_dict.items()]
    return args


def is_on_path(name: str) -> bool:
    """Check if name is on PATH and is executable."""
    return which(name) is not None


def run_command(command_line: CLIargs) -> str:
    """Return program text output. Raise error if non-zero retcode."""
    proc = run(command_line, capture_output=True, check=True, text=True)
    if proc.stdout  is None:
        return ""
    return proc.stdout
