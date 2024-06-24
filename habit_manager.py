from habit import Habit

class HabitManager:
    def __init__(self):
        self.habits = []

    def add_habit(self, name, periodicity):
        habit = Habit(name, periodicity)
        self.habits.append(habit)

    def delete_habit(self, name):
        self.habits = [habit for habit in self.habits if habit.name != name]

    def list_habits(self):
        return self.habits

    def get_habit(self, name):
        for habit in self.habits:
            if habit.name == name:
                return habit
        return None

    def analyze_habits(self):
        analysis = {}
        analysis['longest_streak'] = max((habit.longest_streak() for habit in self.habits), default=0)
        return analysis
