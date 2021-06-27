"""
A swimmer object that can be compared and interacted with. It contains a name,
time, and event title.
"""

class Swimmer:
    def __init__(self, event, time, standard, name, age, time_date):
        # Time info
        self.event = event
        self.time = self.str_time_to_seconds(time)
        self.standard = standard
        self.time_date = time_date

        # Swimmer info
        self.name = name
        self.age = age

    def str_time_to_seconds(self, time):
        if ":" in time:
            minutes = int(time.split(":")[0])
            rest = float(time.split(":")[1])

            return rest + minutes * 60

        else:
            return float(time)

    def __str__(self):
        return f"Swimmer(event='{self.event}', time='{self.time}', name='{self.name}')"

    def __le__(self, other):
        return self.time <= other.time
