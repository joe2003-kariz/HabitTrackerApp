import unittest
from datetime import datetime, timedelta
from habit import Habit
from habit_manager import HabitManager

class TestHabitTracker(unittest.TestCase):

    def setUp(self):
        """
        Set up the test case by initializing the HabitManager and adding predefined habits.
        """
        self.habit_manager = HabitManager()
        # Predefined habits
        self.habit_manager.add_habit("Drink Water", "daily")
        self.habit_manager.add_habit("Exercise", "weekly")

    def test_habit_creation(self):
        """
        Test habit creation by verifying the number of habits and their attributes.
        """
        self.assertEqual(len(self.habit_manager.list_habits()), 2)
        habit = self.habit_manager.get_habit("Drink Water")
        self.assertEqual(habit.name, "Drink Water")
        self.assertEqual(habit.periodicity, "daily")

    def test_habit_deletion(self):
        """
        Test habit deletion and verify the number of habits after deletion.
        """
        self.habit_manager.delete_habit("Drink Water")
        self.assertEqual(len(self.habit_manager.list_habits()), 1)
        habit = self.habit_manager.get_habit("Drink Water")
        self.assertIsNone(habit)

    def test_habit_editing(self):
        """
        Test habit editing by changing the habit's name and verifying the change.
        """
        habit = self.habit_manager.get_habit("Drink Water")
        habit.name = "Drink More Water"
        self.assertEqual(habit.name, "Drink More Water")

    def test_habit_completion(self):
        """
        Test habit completion by checking off the habit for the current date and verifying the completion.
        """
        habit = self.habit_manager.get_habit("Drink Water")
        habit.check_off(datetime.now())
        self.assertEqual(len(habit.completion_dates), 1)

    def test_daily_streak_calculation(self):
        """
        Test daily streak calculation by simulating habit completions for 28 days and verifying streak counts.
        """
        habit = self.habit_manager.get_habit("Drink Water")
        # Simulate habit completion for 4 weeks (28 days)
        today = datetime.now().date()
        for i in range(28):
            habit.check_off(today - timedelta(days=i))
        self.assertEqual(habit.streak(), 28)
        self.assertEqual(habit.longest_streak(), 28)

    def test_weekly_streak_calculation(self):
        """
        Test weekly streak calculation by simulating habit completions for 4 weeks (4 completions) and verifying streak counts.
        """
        habit = self.habit_manager.get_habit("Exercise")
        # Simulate habit completion for 4 weeks (4 completions)
        today = datetime.now().date()
        for i in range(4):
            habit.check_off(today - timedelta(weeks=i))
        self.assertEqual(habit.streak(), 4)
        self.assertEqual(habit.longest_streak(), 4)

    def test_analytics_longest_streak(self):
        """
        Test analytics for the longest streak by completing a habit for 4 weeks and verifying the analysis result.
        """
        habit = self.habit_manager.get_habit("Drink Water")
        today = datetime.now().date()
        # Simulate habit completion for 4 weeks (28 days)
        for i in range(28):
            habit.check_off(today - timedelta(days=i))
        analysis = self.habit_manager.analyze_habits()
        self.assertEqual(analysis['longest_streak'], 28)

    def test_analytics_habit_list(self):
        """
        Test analytics for the habit list by verifying the number of habits in the HabitManager.
        """
        habits = self.habit_manager.list_habits()
        self.assertEqual(len(habits), 2)

if __name__ == '__main__':
    unittest.main()
