import json
import functools


def jsonify(funk):
    @functools.wraps(funk)
    def wrapper(*args, **kwargs):
        return json.dumps(funk(*args, **kwargs))
    return wrapper


# TEST_7:
@jsonify
def make_tuple():
    """JSON-Tuple object"""
    return (1, '2', 3.0, None, False, {'1': True})


print(make_tuple())
print(make_tuple.__name__)
print(make_tuple.__doc__)