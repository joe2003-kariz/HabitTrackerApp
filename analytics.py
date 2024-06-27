def list_current_habits(manager):
    """
    List all current habits.

    :param manager: HabitManager object.
    :return: List of all habits.
    """
    return manager.list_habits()

def list_habits_by_periodicity(manager, periodicity):
    """
    List habits by periodicity.

    :param manager: HabitManager object.
    :param periodicity: The periodicity to filter by.
    :return: List of habits with the specified periodicity.
    """
    return [habit for habit in manager.list_habits() if habit.periodicity == periodicity]

def longest_run_streak(manager):
    """
    Find the longest run streak among all habits.

    :param manager: HabitManager object.
    :return: The longest streak count.
    """
    return max((habit.longest_streak() for habit in manager.list_habits()), default=0)

def longest_run_streak_for_habit(manager, habit_name):
    """
    Find the longest run streak for a specific habit.

    :param manager: HabitManager object.
    :param habit_name: The name of the habit.
    :return: The longest streak count for the habit.
    """
    habit = manager.get_habit(habit_name)
    if habit:
        return habit.longest_streak()
    return 0

def longest_streak_per_periodicity(manager):
    """
    Find the longest streak for each periodicity.

    :param manager: HabitManager object.
    :return: Dictionary with the longest streak for each periodicity.
    """
    return manager.longest_streak_per_periodicity()

