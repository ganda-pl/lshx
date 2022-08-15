#!/usr/bin/env python3

from typing import Any, List, Type

import click

from lib.targets.detector import TargetDetector


@click.command()
@click.argument("files", nargs=-1)
def lshx(files: Type[List[Any]] = list):
    paths: list[str] = [str(path) for path in files]  # type:ignore
    targets = TargetDetector().detect(paths=paths)

    for target in targets:
        print(f"would display {target=}")


if __name__ == "__main__":
    lshx()
