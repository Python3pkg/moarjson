import moarjson as json


def test_load():
    json_dump = json.dumps('SomeString')
    assert json_dump == '"SomeString"'
    assert json.loads(json_dump) == 'SomeString'
