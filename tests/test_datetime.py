import datetime

import pytest
from moarjson import dumps, json, Moarjson, register


register(datetime.datetime, str)
# register == json.register
json.register(datetime.date, lambda s: 'DATE')


@register(datetime.time)
def convert(time_obj):
    return str(time_obj)


def test_global():
    assert json.dumps(datetime.datetime(2014, 1, 5)) == '"2014-01-05 00:00:00"'
    assert dumps(datetime.date(2014, 1, 5)) == '"DATE"'
    assert dumps(datetime.time(12, 0, 0)) == '"12:00:00"'


def test_class():
    # Create new json instance
    json = Moarjson('test_class_moarjson')

    # Acts as a normal json dump
    with pytest.raises(TypeError):
        json.dumps(datetime.datetime(2014, 1, 5))

    # Convert date type to string
    json.register(datetime.date, str)
    assert json.dumps(datetime.date(2014, 1, 5)) == '"2014-01-05"'

    # Overwrite date type
    json.register(datetime.date, lambda x: 'DATE')
    assert json.dumps(datetime.date(2014, 1, 5)) == '"DATE"'

    # datetime is subclass of date
    assert json.dumps(datetime.datetime(2014, 1, 5, 12, 34, 56)) == '"DATE"'
