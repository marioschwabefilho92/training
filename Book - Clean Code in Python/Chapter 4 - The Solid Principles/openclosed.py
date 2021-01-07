class Event:
    def __init__(self, rawdata):
        self.rawdata = rawdata


class UnkownEvent(Event):
    """A type of event that cannot be identified from its data."""


class LoginEvent(Event):
    """A event representing a user that has just entered the system."""


class LogoutEvent(Event):
    """Än event representing a user that has just left the system."""


class SystemMonitor:
    """Identify events that ocurred in the system"""

    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        if (
            self.event_data["before"]["session"] == 0
            and self.event_data["after"]["session"] == 1
        ):
            return LoginEvent(self.event_data)
        elif (
            self.event_data["before"]["session"] == 1
            and self.event_data["after"]["session"] == 0
        ):
            return LogoutEvent(self.event_data)

        return UnkownEvent(self.event_data)


# l1 = SystemMonitor({"before": {"session": 0}, "after": {"session": 1}})
# print(l1.identify_event().__class__.__name__)
# l2 = SystemMonitor({"before": {"session": 1}, "after": {"session": 0}})
# print(l2.identify_event().__class__.__name__)
# l3 = SystemMonitor({"before": {"session": 1}, "after": {"session": 1}})
# print(l3.identify_event().__class__.__name__)
