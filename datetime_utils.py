"""Date and time reporting (FR-03, FR-04) using the datetime module."""

from datetime import datetime


def get_current_time():
    """Return the current time, e.g. "It's currently 3:45 PM"."""
    now = datetime.now()
    hour_12 = now.hour % 12 or 12  # convert 0 -> 12 for a 12-hour clock
    suffix = "AM" if now.hour < 12 else "PM"
    return f"It's currently {hour_12}:{now.minute:02d} {suffix}."


def get_current_date():
    """Return today's date, e.g. "Today is Thursday, November 05, 2026"."""
    return f"Today is {datetime.now().strftime('%A, %B %d, %Y')}."
