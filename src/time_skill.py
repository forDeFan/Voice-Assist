from datetime import datetime
import locale


class Time_Skill():

    def __init__(self) -> None:
        locale.setlocale(locale.LC_ALL, '')
        self._today = datetime.today()

    def get_date(self) -> str:
        date = self._today.strftime('%A, %-d %B')
        return date

    def get_week_number(self) -> str:
        week = self._today.strftime('%-W')
        return week

    def get_time(self) -> str:
        hour = self._today.strftime('%-H')
        return hour
