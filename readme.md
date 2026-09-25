# Python CLI Alarm Clock

A simple command-line alarm clock built with Python.

## Features

- Add an alarm with time and optional label
- List alarms
- Enable and disable alarms
- Delete alarms
- Trigger alarms at the scheduled time
- Audible notification on Windows
- Input validation
- Unit tests
- In-memory storage

## Requirements

- Python 3.10+
- Windows for the built-in beep notification

## Run the application

```bash
python main.py

add HH:MM [label]
list
enable <id>
disable <id>
delete <id>
help
quit

alarm> add 18:30 "Team Meeting"
Alarm added: 1 at 18:30

alarm> list

ID   TIME   STATUS   LABEL
1    18:30  ON       Team Meeting

alarm> disable 1
Alarm 1 disabled.

alarm> enable 1
Alarm 1 enabled.

alarm> delete 1
Alarm 1 deleted.

Design decisions

The application uses an in-memory repository because a database was explicitly excluded from the requirements.

Business logic is separated from the CLI so that it can be tested independently.

The scheduler runs in a background thread so the CLI remains available for user commands.

The alarm trigger prevents the same alarm from firing multiple times on the same day.

Limitations
Alarms are not persisted after the application exits.
The audible notification currently uses Windows winsound.
The scheduler checks the time once per second.
The application is intended as a simple coding-exercise MVP.
AI-assisted development

AI was used during requirements refinement, architecture planning, implementation assistance, and code review.

Generated suggestions were reviewed and simplified based on the 30-minute time constraint and the required scope.

## Validation

The application was manually and automatically validated against the core requirements.

### Manual Validation

The following scenarios were tested:

* **Add alarm** — verified that alarms can be created using `HH:MM` format with an optional label.
* **List alarms** — verified that ID, time, status, and label are displayed correctly.
* **Invalid time input** — verified that invalid values such as `25:99` and `abc` are rejected with a clear error message.
* **Enable alarm** — verified that a disabled alarm can be enabled.
* **Disable alarm** — verified that an enabled alarm can be disabled.
* **Delete alarm** — verified that an existing alarm can be deleted.
* **Invalid alarm ID** — verified that operations on non-existent IDs return a clear error.
* **Alarm triggering** — verified that an enabled alarm triggers when the scheduled time is reached.
* **Disabled alarm** — verified that a disabled alarm does not trigger.
* **Duplicate triggering** — verified that the same alarm does not trigger repeatedly during the same day.
* **Empty alarm list** — verified that the application displays an appropriate message when no alarms exist.

### Automated Tests

Unit tests cover the main business logic:

* Adding an alarm
* Validating invalid time input
* Deleting an alarm
* Enabling and disabling an alarm
* Triggering an alarm only once per day

Run the tests with:

```bash
pytest
```

Expected result:

```text
5 passed
```

### Validation Approach

The application was validated incrementally during development rather than only at the end. Business logic was tested independently from the CLI, which makes the core alarm behavior easier to verify and maintain.
