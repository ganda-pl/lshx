from lib.targets.base import BaseTarget, TargetTypes


def split_targets(
    targets: list[BaseTarget],
) -> tuple[list[BaseTarget], list[BaseTarget]]:
    """
    Splits an iterable of targets into 2 collections: container types (eg. directories) and non-container types (eg.
    files, symlinks, etc)
    """
    containers: list[BaseTarget] = []
    non_containers: list[BaseTarget] = []
    for target in targets:
        if target.type == TargetTypes.DIRECTORY:
            containers.append(target)
        else:
            non_containers.append(target)

    return non_containers, containers
