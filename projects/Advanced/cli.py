# FIXME: Use shared logger with values set from CLI
"""
record the command line arguments
record the start and end of the program
"""

import argparse
import sys

from typing import Optional
from main import main as menu
def create_parser() -> argparse.ArgumentParser:
    """process the command line for dspBonus the BonusParser"""

    # set up parser
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()

    parser.add_argument(
        "--debug",
        action="store_true",
        help="log information about the internals of dspBonus",
    )

    # either -q or -v can be used, but not both
    group.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="suppress all messages about what is happening",
    )

    group.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="provide detailed messages about what is happening",
    )

    return parser

def parse_cli_arguments(argv) -> Optional[argparse.Namespace]:
    # parse the command line
    args = create_parser().parse_args(argv[1:])

    return args

def main(argv: Optional[list[str]] = None) -> int:
    """Main entry point for dspBonus the BonusParser"""

    if argv is None:
        argv = sys.argv

    # parse the command line
    args = create_parser().parse_args(argv[1:])
    menu()

    return 0


if __name__ == "__main__":

    sys.exit(main(sys.argv))