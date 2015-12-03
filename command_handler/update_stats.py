from settings import STATS_DICT


def update_stats(command, success):
    """Update the STATS dict with info about if executing
    *command* was a *success*."""
    if success:
        STATS_DICT[command]['success'] += 1
    else:
        STATS_DICT[command]['error'] += 1
