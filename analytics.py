def list_current_habits(manager):
    return manager.list_habits()

def list_habits_by_periodicity(manager, periodicity):
    return [habit for habit in manager.list_habits() if habit.periodicity == periodicity]

def longest_run_streak(manager):
    return max((habit.longest_streak() for habit in manager.list_habits()), default=0)

def longest_run_streak_for_habit(manager, habit_name):
    habit = manager.get_habit(habit_name)
    if habit:
        return habit.longest_streak()
    return 0
