import re

from sales.helpers.exceptions import HMoneyException

millnames = {'K': 6, 'M': 9, 'B': 12}


def abbreviate_to_decimal(value):
    """
    Format abbreviate value to decimal
    Eg: $739K -> 739000.0
        $233.7M -> 233700000.0
        $23.3B -> 23300000000.0
    """
    validate_patter = r"(['$']{1})([\d]+)([\.]{1})?([\d]+)?(['M','K','B']{1})"
    if re.match(pattern=validate_patter, string=value):
        # Extract number of string
        v, nx = (re.findall(r'(\d+)\.?([\d]+)?', value)), value[-1]

        if nx == 'K':
            v = ''.join(v[0])
            right_zeros = ['0' for z in range(millnames[nx] - (len(v)+(3-len(v))))]
            return float(v+(''.join(right_zeros)))
        elif nx =='M' or nx == 'B':
            vx = ''.join(v[0])
            right_zeros = ['0' for z in range((millnames[nx] - (len(vx)+(3-len(v[0][0])))))]  # noqa
            return float(vx+(''.join(right_zeros)))

    raise HMoneyException("{} is not valid.".format(value))


def decimal_to_abbreviate(value):
    # TODO: its necessary implement convert decimal to abbreviate
    pass