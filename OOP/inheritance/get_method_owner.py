def get_method_owner(cls, method):
    for item in cls.mro():
        if method in item.__dict__:
            return item
