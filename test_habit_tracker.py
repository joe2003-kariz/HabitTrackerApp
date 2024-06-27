import pytest
from habit import Habit
from habit_manager import HabitManager

def test_habit_creation():
    """
    Test the creation of a new habit.
    """
    habit = Habit('Test Habit', 'daily')
    assert habit.name == 'Test Habit'
    assert habit.periodicity == 'daily'

def test_add_habit():
    """
    Test adding a habit to the HabitManager.
    """
    manager = HabitManager()
    manager.add_habit('Test Habit', 'daily')
    assert len(manager.habits) == 1

def test_delete_habit():
    """
    Test deleting a habit from the HabitManager.
    """
    manager = HabitManager()
    manager.add_habit('Test Habit', 'daily')
    manager.delete_habit('Test Habit')
    assert len(manager.habits) == 0

def test_list_habits():
    """
    Test listing all habits in the HabitManager.
    """
    manager = HabitManager()
    manager.add_habit('Test Habit', 'daily')
    habits = manager.list_habits()
    assert len(habits) == 1
    assert habits[0].name == 'Test Habit'

def test_longest_streak():
    """
    Test calculating the longest streak for a habit.
    """
    habit = Habit('Test Habit', 'daily')
    habit.check_off(datetime.now())
    assert habit.longest_streak() == 1
