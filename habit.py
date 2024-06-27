from datetime import datetime, timedelta

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
        """
        Calculate the current streak of the habit based on completion dates.

        Args:
        - dates (list): List of datetime objects representing completion dates.

        Returns:
        - int: The current streak count.
        """
        streak = 0
        today = datetime.now().date()
        period_days = self.get_period_days()

        # Sort completion dates in descending order
        sorted_dates = sorted(dates, reverse=True)

        for i, date in enumerate(sorted_dates):
            if i == 0:
                streak += 1  # Always count the most recent completion

            elif (sorted_dates[i - 1] - date).days <= period_days:
                streak += 1  # Increment streak if within period days

            else:
                break  # Streak broken if gap is larger than period days

        return streak

    def _calculate_longest_streak(self, dates):
        """
        Calculate the longest streak of the habit based on completion dates.

        Args:
        - dates (list): List of datetime objects representing completion dates.

        Returns:
        - int: The longest streak count.
        """
        longest_streak = 0
        current_streak = 0
        previous_date = None
        period_days = self.get_period_days()

        # Sort completion dates in ascending order
        sorted_dates = sorted(dates)

        for date in sorted_dates:
            if previous_date and (date - previous_date).days <= period_days:
                current_streak += 1
            else:
                current_streak = 1

            if current_streak > longest_streak:
                longest_streak = current_streak

            previous_date = date

        return longest_streak
