import shlex

from alarm_clock.service import AlarmService


class AlarmCLI:
    def __init__(self, service: AlarmService):
        self.service = service

    def run(self) -> None:
        print("Alarm Clock")
        print("Type 'help' to see available commands.")

        while True:
            try:
                command = input("alarm> ").strip()

                if not command:
                    continue

                if command == "quit":
                    print("Goodbye!")
                    break

                self.handle_command(command)

            except (ValueError, IndexError) as error:
                print(f"Error: {error}")
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break

    def handle_command(self, command: str) -> None:
        parts = shlex.split(command)
        action = parts[0].lower()

        if action == "help":
            self.show_help()

        elif action == "add":
            self.add_alarm(parts)

        elif action == "list":
            self.list_alarms()

        elif action == "delete":
            self.delete_alarm(parts)

        elif action == "enable":
            self.enable_alarm(parts)

        elif action == "disable":
            self.disable_alarm(parts)

        else:
            print(f"Unknown command: {action}")
            print("Type 'help' to see available commands.")

    def add_alarm(self, parts: list[str]) -> None:
        if len(parts) < 2:
            raise ValueError("Usage: add HH:MM [label]")

        alarm_time = parts[1]
        label = " ".join(parts[2:])

        alarm = self.service.add_alarm(alarm_time, label)

        print(
            f"Alarm added: {alarm.id} "
            f"at {alarm.alarm_time.strftime('%H:%M')}"
        )

    def list_alarms(self) -> None:
        alarms = self.service.list_alarms()

        if not alarms:
            print("No alarms.")
            return

        print("\nID   TIME   STATUS   LABEL")

        for alarm in alarms:
            status = "ON" if alarm.enabled else "OFF"
            label = alarm.label or "-"
            print(
                f"{alarm.id:<4} "
                f"{alarm.alarm_time.strftime('%H:%M'):<7} "
                f"{status:<8} "
                f"{label}"
            )

    def delete_alarm(self, parts: list[str]) -> None:
        alarm_id = self._get_id(parts, "delete")
        self.service.delete_alarm(alarm_id)
        print(f"Alarm {alarm_id} deleted.")

    def enable_alarm(self, parts: list[str]) -> None:
        alarm_id = self._get_id(parts, "enable")
        self.service.enable_alarm(alarm_id)
        print(f"Alarm {alarm_id} enabled.")

    def disable_alarm(self, parts: list[str]) -> None:
        alarm_id = self._get_id(parts, "disable")
        self.service.disable_alarm(alarm_id)
        print(f"Alarm {alarm_id} disabled.")

    @staticmethod
    def _get_id(parts: list[str], command: str) -> int:
        if len(parts) != 2:
            raise ValueError(f"Usage: {command} <alarm_id>")

        try:
            return int(parts[1])
        except ValueError:
            raise ValueError("Alarm ID must be a number.")

    @staticmethod
    def show_help() -> None:
        print(
            """
Available commands:

  add HH:MM [label]    Add an alarm
  list                 List all alarms
  enable <id>          Enable an alarm
  disable <id>         Disable an alarm
  delete <id>          Delete an alarm
  help                 Show this help
  quit                 Exit the application
"""
        )