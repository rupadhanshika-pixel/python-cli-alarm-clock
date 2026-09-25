# import time

# from alarm_clock.service import AlarmService


# class AlarmScheduler:
#     def __init__(self, service: AlarmService):
#         self.service = service
#         self.running = True

#     def run(self) -> None:
#         print("Alarm scheduler started. Press Ctrl+C to stop.")

#         try:
#             while self.running:
#                 triggered_alarms = self.service.check_alarms()

#                 for alarm in triggered_alarms:
#                     label = f" - {alarm.label}" if alarm.label else ""
#                     print(
#                         f"\n🔔 ALARM {alarm.id}: "
#                         f"{alarm.alarm_time.strftime('%H:%M')}{label}"
#                     )

#                 time.sleep(1)

#         except KeyboardInterrupt:
#             self.running = False
#             print("\nScheduler stopped.")

import time
import winsound

from alarm_clock.service import AlarmService


class AlarmScheduler:
    def __init__(self, service: AlarmService):
        self.service = service
        self.running = True

    def run(self) -> None:
        print("Alarm scheduler started. Press Ctrl+C to stop.")

        try:
            while self.running:
                triggered_alarms = self.service.check_alarms()

                for alarm in triggered_alarms:
                    label = f" - {alarm.label}" if alarm.label else ""

                    print(
                        f"\n🔔 ALARM {alarm.id}: "
                        f"{alarm.alarm_time.strftime('%H:%M')}{label}"
                    )

                    # Beep 3 times
                    for _ in range(3):
                        winsound.Beep(1000, 500)
                        time.sleep(0.2)

                time.sleep(1)

        except KeyboardInterrupt:
            self.running = False
            print("\nScheduler stopped.")