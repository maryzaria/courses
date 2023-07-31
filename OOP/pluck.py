def pluck(data: dict, path: str, default=None):
    if len(path.split('.')) == 1:
        return data.get(path, default)
    else:
        i = path.find('.')
        return pluck(data[path[:i]], path[i + 1:], default)


def pluck2(data: dict, path: str, default=None):
    for key in path.split('.'):
        try:
            data = data[key]
        except KeyError:
            return default
    return data

d = {'a': {'b': {'c': {'d': {'e': 4}}}}}

print(pluck2(d, 'a.b.c'))
