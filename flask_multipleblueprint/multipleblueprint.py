decorators = set(["route", "endpoint", "app_template_filter", "app_template_test", "app_template_global", "app_errorhandler", "errorhandler"])

class MultipleBlueprint(object):
    def __init__(self, *blueprints):
        self.blueprints = blueprints

    def __getattribute__(self, name):
        if name not in decorators:
            return object.__getattribute__(self, name)

        def mass_decorator(*args, **options):
            def decorator(f):
                for blueprint in self.blueprints:
                    f = blueprint.__getattribute__(name)(*args, **options)(f)
                return f
            return decorator

        return mass_decorator
