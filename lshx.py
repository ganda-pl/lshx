#!/usr/bin/env python3

from typing import Any, List, Type

import click

from lib.formatters.plain import PlainFormatter
from lib.targets.detector import TargetDetector
from lib.targets.utils import split_targets


@click.command()
@click.argument("files", nargs=-1)
def lshx(files: Type[List[Any]] = list) -> None:
    paths: list[str] = [str(path) for path in files]  # type:ignore
    formatter = PlainFormatter()

    targets = TargetDetector().detect(paths=paths)

    # split targets to single entries (files) vs containers (eg. directories)
    non_containers, containers = split_targets(targets)

    # display non-containers
    for target in sorted(non_containers, key=lambda x: x.path.name):
        print(formatter.format(target), end="")

    print()


if __name__ == "__main__":
    lshx()
