# Timezone

Often deadlines are announced in a time zone that differs from your local time
zone.

`timezone.py` is a simple script that solves this problem. It allows the
conversion of a target date, given in a specific time zone, to the
corresponding date in the local time zone.

Additionally, an .ics file for the event is created for the local time zone.


## Setup

First, download the repository:

```
git clone https://github.com/akellne/timezone.git
cd timezone
```

Then, create a virtual environment and install the required dependencies:

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```


## Example

```
./timezone.py --tzname "Pacific/Samoa" --date "Monday April 29, 2019 11:59 p.m." --event-name "ESORICS 19 Deadline"
```
