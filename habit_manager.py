from habit import Habit

class HabitManager:
    def __init__(self):
        """
        Initialize a new HabitManager.
        """
        self.habits = []

    def add_habit(self, name, periodicity):
        """
        Add a new habit.

        :param name: The name of the habit.
        :param periodicity: The frequency of the habit ('daily', 'weekly', 'monthly').
        """
        habit = Habit(name, periodicity)
        self.habits.append(habit)

    def delete_habit(self, name):
        """
        Delete a habit by name.

        :param name: The name of the habit to be deleted.
        """
        self.habits = [habit for habit in self.habits if habit.name != name]

    def list_habits(self):
        """
        List all habits.

        :return: List of all habits.
        """
        return self.habits

    def get_habit(self, name):
        """
        Get a habit by name.

        :param name: The name of the habit.
        :return: The habit object if found, otherwise None.
        """
        for habit in self.habits:
            if habit.name == name:
                return habit
        return None

    def analyze_habits(self):
        """
        Analyze habits to find the longest streak.

        :return: Analysis dictionary containing the longest streak.
        """
        analysis = {}
        analysis['longest_streak'] = max((habit.longest_streak() for habit in self.habits), default=0)
        return analysis

    def longest_streak_per_periodicity(self):
        """
        Find the longest streak per periodicity.

        :return: Dictionary with the longest streak for each periodicity.
        """
        streaks = {'daily': 0, 'weekly': 0, 'monthly': 0}
        for habit in self.habits:
            streak = habit.longest_streak()
            if streak > streaks[habit.periodicity]:
                streaks[habit.periodicity] = streak
        return streaks


    def analyze_habits(self):
        analysis = {}
        analysis['longest_streak'] = max((habit.longest_streak() for habit in self.habits), default=0)
        return analysis
