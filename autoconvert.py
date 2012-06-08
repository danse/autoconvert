import re
from datetime import datetime

def datetime_conversion(v):
    '''
    >>> datetime_conversion('2012-06-08T20:23:54.340079')
    datetime.datetime(2012, 6, 8, 20, 23, 54)
    >>> d = datetime_conversion('2002-12-25T00:00:00')
    >>> d
    datetime.datetime(2002, 12, 25, 0, 0)
    >>> datetime_conversion(d.isoformat())
    datetime.datetime(2002, 12, 25, 0, 0)
    '''
    format = '%Y-%m-%dT%H:%M:%S'
    v = re.sub('\.\d*', '', v)
    return datetime.strptime(v, format)

def bool_conversion(v):
    '''
    >>> b = bool_conversion
    >>> b('True'), b('False')
    (True, False)
    >>> b('true'), b('false')
    (True, False)
    >>> b('foo')
    Traceback (most recent call last):
    ...
    ValueError: invalid literal for bool_conversion(): 'foo'
    '''
    if v.title() == 'True': return True
    if v.title() == 'False': return False
    raise ValueError('invalid literal for bool_conversion(): {0!r}'.format(v))

def from_string(value):
    '''
    Convert a string to a builtin type trying to guess the type.
    >>> a = from_string
    >>> a('1')
    1
    >>> a('a')
    'a'
    >>> a('False')
    False
    '''
    for conversion in (
            int,
            float,
            bool_conversion,
            datetime_conversion,
            str):
        try: return conversion(value)
        except ValueError: pass

def to_string(value):
    '''
    >>> to_string(False)
    'False'
    '''
    if   type(value) == datetime:
        return value.isoformat()
    else:
        return str(value)
