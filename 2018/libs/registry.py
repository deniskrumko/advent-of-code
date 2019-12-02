registry = {}


def register(day, part, is_test=False):
    """Add solution or test class to registry."""

    def wrapper(cls):
        key = f'{day}.{part}'
        registry.setdefault(key, {})

        if is_test:
            registry[key]['test'] = cls
        else:
            registry[key]['solution'] = cls

        cls.key = key
        return cls

    return wrapper
