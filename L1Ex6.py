class Time:
    def __init__(self, hour: int = 0, minute: int = 0, second: int = 0):
        self.set_time(hour, minute, second)

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, value: int):
        if isinstance(value, int) and 0 <= value <= 23:
            self._hour = value
        else:
            print(
                "Provided hour is outside of allowed values (0-23)\n"
                "Setting hour to 0"
            )
            self._hour = 0

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, value: int):
        if 0 <= value <= 59:
            self._minute = value
        else:
            self._minute = 0
            print(
                "Provided minute is outside of allowed values (0-59)\n"
                "Setting minute to 0"
            )

    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, value: int):
        if 0 <= value <= 59:
            self._second = value
        else:
            self._second = 0
            print(
                "Provided second is outside of allowed values (0-59)\n"
                "Setting second to 0"
            )

    def set_time(self, h: int = 0, m: int = 0, s: int = 0):
        self.hour = h
        self.minute = m
        self.second = s

    def __repr__(self):
        return f"Time({self.hour}, {self.minute}, {self.second})"

    def __str__(self):
        return (
            f"{self.hour if self.hour <= 12 else self.hour - 12}:"
            f"{self.minute}:{self.second} "
            f"{'AM' if self.hour <= 11 else 'PM'}"
        )
