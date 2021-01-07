class Event:
    def __init__(self, rawdata):
        self.rawdata = rawdata

    @staticmethod
    def meets_condition(event_data: dict):
        return False
    
    @staticmethod
    def meets_condition_pre(event_data: dict):
        """Precondition of the contract of this interface.
        
        Validate that the ''event_data'' parameter is properly formed
        """
        assert isinstance(event_data, dict), f"{event_data} is not a dict"
        for moment in ("before", "after"):
            assert moment in event_data, f"{moment} not in {event_data}"
            assert isinstance(event_data[moment], dict)

class UnkownEvent:
    pass

class SystemMonitor:
    """Identify events that ocurred in the system."""

    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        Event.meets_condition_pre(self.event_data)
        event_cls = next(
            (
                event_cls
                for event_cls in Event.__subclasses__()
                if event_cls.meets_condition(self.event_data)
            ),
            UnkownEvent,
        )
        return event_cls(self.event_data)