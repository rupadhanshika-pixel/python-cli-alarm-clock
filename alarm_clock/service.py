from datetime import datetime
from alarm_clock.models import Alarm
from alarm_clock.repository import AlarmRepository


class AlarmService:
    def __init__(self, repository: AlarmRepository):
        self.repository = repository
        self.next_id = 1

    def add_alarm(self, time_text: str, label: str = "") -> Alarm:
        try:
            alarm_time = datetime.strptime(time_text, "%H:%M").time()
        except ValueError:
            raise ValueError("Invalid time. Use HH:MM format, for example 08:30.")

        alarm = Alarm(
            id=self.next_id,
            alarm_time=alarm_time,
            label=label,
        )

        self.repository.add(alarm)
        self.next_id += 1

        return alarm

    def list_alarms(self) -> list[Alarm]:
        return self.repository.get_all()

    def delete_alarm(self, alarm_id: int) -> None:
        if not self.repository.delete(alarm_id):
            raise ValueError(f"Alarm with ID {alarm_id} does not exist.")

    def enable_alarm(self, alarm_id: int) -> None:
        alarm = self._get_alarm(alarm_id)

        if alarm.enabled:
            raise ValueError(f"Alarm {alarm_id} is already enabled.")

        alarm.enabled = True

    def disable_alarm(self, alarm_id: int) -> None:
        alarm = self._get_alarm(alarm_id)

        if not alarm.enabled:
            raise ValueError(f"Alarm {alarm_id} is already disabled.")

        alarm.enabled = False

    def check_alarms(self, now: datetime | None = None) -> list[Alarm]:
        now = now or datetime.now()
        triggered = []

        for alarm in self.repository.get_all():
            if not alarm.enabled:
                continue

            if alarm.alarm_time.hour != now.hour:
                continue

            if alarm.alarm_time.minute != now.minute:
                continue

            if alarm.last_triggered_date == now.date():
                continue

            alarm.last_triggered_date = now.date()
            triggered.append(alarm)

        return triggered

    def _get_alarm(self, alarm_id: int) -> Alarm:
        alarm = self.repository.get(alarm_id)

        if alarm is None:
            raise ValueError(f"Alarm with ID {alarm_id} does not exist.")

        return alarm