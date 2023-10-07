class EnvironmentNotFound(KeyError):
    pass


class EnvironmentValueError(ValueError):
    pass


class EnvironmentProductionError(Exception):
    pass


class ExplicitURLError(ValueError):
    pass
