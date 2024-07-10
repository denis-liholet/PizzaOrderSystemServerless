from datetime import datetime


def get_current_ts() -> int:
    """
    Function returns current UTC timestamp in milliseconds
    as an integer
    """
    return int(datetime.utcnow().timestamp() * 1000)


def get_today_date() -> str:
    """
    Function returns current date as a string.
    Return string template is "YEAR-MONTH-DAY"
    """
    dt = datetime.utcnow()
    return dt.strftime("%Y-%m-%d")


def get_beginning_of_the_day_ts() -> int:
    """
    Function return timestamp of the beginning of
    the current day in milliseconds
    """
    dt = datetime.utcnow()
    start = datetime(dt.year, dt.month, dt.day).timestamp()
    return int(start * 1000)
