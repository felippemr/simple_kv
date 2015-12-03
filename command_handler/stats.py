from settings import STATS_DICT


def handle_stats():
    """Return a tuple containing True and the contents of the STATS dict."""
    return (True, str(STATS_DICT))
