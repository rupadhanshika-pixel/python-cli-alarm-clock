from alarm_clock.cli import AlarmCLI
from alarm_clock.repository import AlarmRepository
from alarm_clock.scheduler import AlarmScheduler
from alarm_clock.service import AlarmService


def main():
    repository = AlarmRepository()
    service = AlarmService(repository)
    cli = AlarmCLI(service)

    print("Starting Alarm Clock...")
    print("Note: The scheduler runs in the background.")

    scheduler = AlarmScheduler(service)

    import threading

    scheduler_thread = threading.Thread(
        target=scheduler.run,
        daemon=True,
    )
    scheduler_thread.start()

    cli.run()


if __name__ == "__main__":
    main()