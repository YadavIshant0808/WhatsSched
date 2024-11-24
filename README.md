# WhatsApp message Scheduler

`WhatsSched` is a Python module that allows you to schedule and send WhatsApp messages programmatically using the `pywhatkit` library.

## Features
- Schedule messages for specific dates and times.
- Automatic retries in case of message delivery failures.
- Simple and reusable function for scheduling messages.

## Installation

```bash
pip install WhatsSched 
```

## Usage
### Import the Module
```python
from .WhatsSched import send_whatsapp_message
```
### Send a Scheduled Message
```python
send_whatsapp_message(
    day=24,
    month=11,
    year=2024,
    hour=10,
    minute=32,
    second=0,
    message="Hello! This is a scheduled message.",
    phone_number="+918568xxxxxx"
)
```
### Parameters
1. day: Day of the month (1-31).
2. month: Month of the year (1-12).
3. year: Year (e.g., 2024).
4. hour: Hour of the day (24-hour format).
5. minute: Minute of the hour.
6. second: Second of the minute (not used for scheduling).
7. message: The message to send.
8. phone_number: Recipient's WhatsApp number in "+<country_code><number>" format.

#### Example
```python
from .WhatsSched import send_whatsapp_message

if __name__ == "__main__":
    send_whatsapp_message(
        day=24,
        month=11,
        year=2024,
        hour=10,
        minute=30,
        second=0,
        message="Hello from WhatsApp Scheduler!",
        phone_number="+918568xxxxxx"
    )
```
## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
