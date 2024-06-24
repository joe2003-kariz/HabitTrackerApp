from datetime import datetime

class Habit:
    def __init__(self, name, periodicity):
        self.name = name
        self.periodicity = periodicity
        self.creation_date = datetime.now()
        self.completion_dates = []

    def check_off(self, date):
        self.completion_dates.append(date)

    def is_broken(self):
        if not self.completion_dates:
            return True
        return (datetime.now() - max(self.completion_dates)).days > self.get_period_days()

    def streak(self):
        return self._calculate_streak(self.completion_dates)

    def longest_streak(self):
        return self._calculate_longest_streak(self.completion_dates)

    def get_period_days(self):
        if self.periodicity == 'daily':
            return 1
        elif self.periodicity == 'weekly':
            return 7
        else:
            return 30

    def _calculate_streak(self, dates):
        streak = 0
        today = datetime.now().date()
        for date in sorted(dates, reverse=True):
            if (today - date.date()).days == streak:
                streak += 1
            else:
                break
        return streak

    def _calculate_longest_streak(self, dates):
        longest_streak = 0
        current_streak = 0
        previous_date = None
        for date in sorted(dates):
            if previous_date and (date.date() - previous_date).days == self.get_period_days():
                current_streak += 1
            else:
                current_streak = 1
            if current_streak > longest_streak:
                longest_streak = current_streak
            previous_date = date.date()
        return longest_streak
