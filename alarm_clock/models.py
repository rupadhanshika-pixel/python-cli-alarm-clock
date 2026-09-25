from dataclasses import dataclass
from datetime import date, time


@dataclass
class Alarm:
    id: int
    alarm_time: time
    label: str = ""
    enabled: bool = True
    last_triggered_date: date | None = None