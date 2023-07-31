def is_context_manager(obj):
    try:
        with obj:
            return True
    except AttributeError:
        return False


# TEST_5:
class ContextManager:
    def __enter__(self):
        return 'beegeek'

    def __exit__(self, exc_type, exc_value, exc_tb):
        return True


print(is_context_manager(ContextManager()))