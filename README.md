moarjson
========

[![Build Status](https://travis-ci.org/bulv1ne/moarjson.png?branch=master)](https://travis-ci.org/bulv1ne/moarjson)

Install
-------

```
pip install moarjson
```

Basic usage
-----------

```python
import moarjson as json

from datetime import datetime

json.dumps(datetime.now()) # Fails

# Tell json to convert datetime objects to str first
json.register(datetime, str)

json.dumps(datetime.now()) # Success
```

moarjson keeps track of all the types you want to encode to json.

```python
import moarjson as json

from datetime import datetime

# Also available as decorator
@json.register(datetime)
def convert_datetime(obj):
    return obj.strftime(format='%Y-%m-%d %H:%M')

# OR with lambda
json.register(datetime, lambda x: x.strftime(format='%Y-%m-%d %H:%M'))
```


Django models
-------------

Django user model field:

```python
from django.contrib.auth.models import User

@json.register(User)
def convert_user(user):
  return {
     'id': user.id,
     'username': user.username
  }

def user_view(request):
  # Json encoded user object
  json_dump = json.dumps(User.objects.get(pk=1))

  return HttpResponse(json_dump, content_type='application/json')
```

User.objects.all() is an iterable, so register iterables that first.
Convert any iterable to a list::

```python
import collections
json.register(collections.Iterable, list)

def user_list_view(request):
  # List of users
  json_dump = json.dumps(User.objects.all())

  return HttpResponse(json_dump, content_type='application/json')
```


Contribution
------------

### Code validation

The code is valid if it passes **flake8**.
Imports are sorted with **isort**.

### Testing

For testing **py.test** is used.
