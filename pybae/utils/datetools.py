"""
Collection of utility functions datetime related.
"""

import datetime as dt

__all__ = ["utc_now"]

def utc_now() -> dt.datetime:
    """Get the current UTC datetime.

    Returns:
        datetime: The current UTC datetime.

    """
    return dt.datetime.now(dt.UTC)
