from sales.helpers.exceptions import Dict_Exception


def count_dict(dict_):
    """
    Count how many levels the dict has
    """
    if not isinstance(dict_, dict):
        raise Dict_Exception("dict_ must be a dict")
    return max(count_dict(v) if isinstance(v, dict) else 0 for v in dict_.values()) + 1  # noqa