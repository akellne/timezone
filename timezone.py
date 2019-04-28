#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import datetime

import pytz
import click
from tzlocal import get_localzone
from dateutil.parser import parse
from ics import Calendar, Event


@click.command(
    help="Converts a target date that is in the given timezone to "
         "the local timezone."
)
@click.option(
    "--date", required=True,
    help="Target date that should be parsed."
)
@click.option(
    "--tzname", required=True,
    help="Name of the timezone of the target date."
)
@click.option(
    "--event-name", default="Event", show_default=True,
    help="Name of the event."
)
@click.option(
    "--date-format", default="%a, %d %b %Y %H:%Mh", show_default=True,
    help="Format of the output date."
)
@click.option(
    "--create-ics", default=True, type=bool, show_default=True,
    help="Creates a corresponding .ics file for the local timezone."
)
def convert(date, tzname, date_format, create_ics, event_name):
    if tzname not in pytz.all_timezones:
        sys.exit(
            "Please use one of the following timezones: {}".format(
                ", ".join(pytz.all_timezones)
            )
        )

    # get
    tz = pytz.timezone(tzname)

    # get parse the date for the provided timezone
    dt = tz.localize(parse(date))

    # get localtimezone and convert the date
    local_tz = get_localzone()
    local_dt = dt.astimezone(local_tz)

    # compute time diff in hours
    today = datetime.datetime.today()
    hours = (local_tz.utcoffset(today) - tz.utcoffset(today)).seconds // 3600

    # simple output of target time and local time
    print("=== {} ===".format(event_name))
    print(
        "    target time: {} ({})  [{} hours]".format(
            dt.strftime(date_format), tz,
            "+{}".format(hours) if hours > 0 else hours
        )
    )
    print(
        ">>>  local time: {} ({})".format(
            local_dt.strftime(date_format), local_tz
        )
    )

    if create_ics is True:
        # create .ics file
        c = Calendar()
        c.events.add(Event(name=event_name, begin=local_dt))
        print("creating 'event.ics' file...")
        with open("event.ics", "w") as f:
            f.writelines(c)


if __name__ == "__main__":
    convert()
