from dataclasses import dataclass, field
import uuid
import datetime


@dataclass(frozen=True)  # this decoration means once a TestRecord instance is created, it can not be changed again.
class TestRecord:
    # when apply @dataclass, Python itself will take care of __init__(), so no need to add one

    test_name: str
    start_time: datetime.datetime
    end_time: datetime.datetime
    duration: datetime.timedelta
    measurement: int | float
    outcome: str

    error: str | None

    # One dataclass rule states that fields without a default value cannot follow fields with a default value.

    # as mentioned earlier, there's no __init__() so we can not use it to generate a unique id for every instance, so
    # we utilize field(default_factory=...)
    test_id: uuid.UUID = field(default_factory=uuid.uuid4)


