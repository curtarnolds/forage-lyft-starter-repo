from engine_abc import Engine


class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on: False):
        """Initialize a SternmanEngine.

        Args:
        warning_light_is_on (bool): Indicates whether or not
        warning light is on
        """
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self) -> bool:
        if self.warning_light_is_on:
            return True
        else:
            return False
