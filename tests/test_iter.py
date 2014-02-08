import collections

import moarjson as json


json.register(collections.Iterable, list)


def test_iter():
    a_list = ['a', 'b', 'c']
    an_iterable = iter(a_list)
    assert json.dumps(an_iterable) == json.dumps(a_list)
