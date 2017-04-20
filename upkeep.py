import datetime
import re

import holidays

penn_holidays = {
    'Independence Day',
    'Labor Day',
    'Thanksgiving',
    'Christmas Day',
    "New Year's Day",
    'Martin Luther King, Jr. Day',
    'Memorial Day',
}

us_holidays = holidays.UnitedStates()


def is_holiday(date):
    """
    Return True or False for whether a date is a holiday
    """
    name = us_holidays.get(date)
    if not name:
        return False
    name = name.replace(' (Observed)', '')
    return name in penn_holidays


def is_workday(date):
    """
    Return boolean for whether a date is a workday.
    """
    if date.weekday() in holidays.WEEKEND:
        return False
    if is_holiday(date):
        return False
    return True


def issue_title_to_date(title):
    """
    Return a datetime.date object from a Scrum issue title.
    """
    pattern = re.compile(r'([0-9]{4})-([0-9]{2})-([0-9]{2}):')
    match = pattern.match(title)
    if not match:
        return None
    return datetime.date(*map(int, match.groups()))
