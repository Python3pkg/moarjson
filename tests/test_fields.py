import moarjson as json


class User(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)


json.register_with_fields(User, ('first_name', 'last_name', 'full_name',))


def test_fields():
    user = User('James', 'Bond')
    assert user.full_name() == 'James Bond'
    test_dict = {'first_name': 'James',
                 'last_name': 'Bond',
                 'full_name': 'James Bond'}
    json_dict = json.loads(json.dumps(user))
    assert json_dict == test_dict
