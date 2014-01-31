moarjson
========

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

Contribution
------------

### Code validation

The code is valid if it passes **flake8**.
Imports are sorted with **isort**.

### Testing

For testing **py.test** is used.
