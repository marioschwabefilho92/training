from datetime import datetime


def hide_field(field) -> str:
    return "**redacted**"


def format_time(field_timestamp: datetime) -> str:
    return field_timestamp.strftime("%Y-%m-%d %H:%M")


def show_orginal(event_field):
    return event_field


class EventSerializer:
    def __init__(self, serialization_fields: dict) -> None:
        self.serialization_fields = serialization_fields

    def serialize(self, event) -> dict:
        return {
            field: transformation(getattr(event, field))
            for field, transformation in
            self.serialization_fields.items()
        }


class Serialization:
    def __init__(self, **transformations):
        self.serializer = EventSerializer(transformations)

    def __call__(self, event_class):
        def serialize_method(event_instance):
            return self.serializer.serialize(event_instance)
        event_class.serialize = serialize_method
        return event_class


@Serialization(
    username=show_orginal,
    password=hide_field,
    ip=show_orginal,
    timestamp=format_time,
)
class LoginEvent:
    def __init__(self, usarname, password, ip, timestamp):
        self.username = usarname
        self.password = password
        self.ip = ip
        self.timestamp = timestamp
