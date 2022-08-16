#!/usr/bin/env python3

from typing import Any, List, Type

import click

from lib.formatters.base import BaseFormatter
from lib.formatters.plain import PlainFormatter
from lib.formatters.plain_newline import PlainNewlineFormatter
from lib.targets.detector import TargetDetector
from lib.targets.utils import split_targets


def get_formatter(one_per_line: bool) -> Type[BaseFormatter]:
    """
    Selects correct output formatter based on provided commandline flags
    """
    if one_per_line:
        return PlainNewlineFormatter
    else:
        return PlainFormatter


@click.command()
@click.argument("files", nargs=-1)
@click.option("-1", "--one-per-line", is_flag=True, default=False)
def lshx(files: Type[List[Any]] = list, one_per_line: bool = False) -> None:
    paths: list[str] = [str(path) for path in files]  # type:ignore
    formatter = get_formatter(one_per_line=one_per_line)()

    # detect targets to display
    targets = TargetDetector().detect(paths=paths)

    # split targets to single entries (files) vs containers (eg. directories)
    non_containers, containers = split_targets(targets)

    # display non-containers
    for target in sorted(non_containers, key=lambda x: x.path.name):
        print(formatter.format(target), end="")
    print()

    # display containers
    display_target_names = len(containers) > 1 or len(non_containers) > 0
    for target in containers:
        print()
        if display_target_names:
            print(f"{target.path.name}:")
    print()


if __name__ == "__main__":
    lshx()
