from datetime import datetime

from sales.helpers.exceptions import HDateException


def format_date(date, input_pattern='%m/%d/%Y', output_pattern='%Y-%m-%d',
                string=True):
    """
    This function will help you to manipulate date
    :param date: string
    :param input_pattern: date input pattern
    :param output_pattern: date output patter
    :param string: True if you wanna string output
    :return: formated date if strint is True or datetime object
    """
    if not date:
        return None
    try:
        dt = datetime.strptime(date, input_pattern)
        if string:
            return dt.strftime(output_pattern)
        return dt
    except Exception as e:
        raise HDateException(e)
