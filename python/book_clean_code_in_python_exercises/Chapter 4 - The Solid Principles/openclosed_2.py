class Event:
    def __init__(self, rawdata):
        self.rawdata = rawdata

    @staticmethod
    def meets_condition(event_data: dict):
        return False


class UnkownEvent(Event):
    """A type of event that cannot be identified from its data"""


class LoginEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict):
        return (
            event_data["before"]["session"] == 0 and event_data["after"]["session"] == 1
        )


class LogoutEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict):
        return (
            event_data["before"]["session"] == 1 and event_data["after"]["session"] == 0
        )


class SystemMonitor:
    """Identify events that ocurred in the system."""

    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        for event_cls in Event.__subclasses__():
            try:
                if event_cls.meets_condition(self.event_data):
                    return event_cls(self.event_data)
            except KeyError:
                continue
        return UnkownEvent(self.event_data)


# l1 = SystemMonitor({"before": {"session": 0}, "after": {"session": 1}})
# print(l1.identify_event().__class__.__name__)
# l2 = SystemMonitor({"before": {"session": 1}, "after": {"session": 0}})
# print(l2.identify_event().__class__.__name__)
# l3 = SystemMonitor({"before": {"session": 1}, "after": {"session": 1}})
# print(l3.identify_event().__class__.__name__)
