from alarm_clock.models import Alarm


class AlarmRepository:
    def __init__(self):
        self.alarms: dict[int, Alarm] = {}

    def add(self, alarm: Alarm) -> None:
        self.alarms[alarm.id] = alarm

    def get(self, alarm_id: int) -> Alarm | None:
        return self.alarms.get(alarm_id)

    def get_all(self) -> list[Alarm]:
        return list(self.alarms.values())

    def delete(self, alarm_id: int) -> bool:
        if alarm_id not in self.alarms:
            return False

        del self.alarms[alarm_id]
        return True