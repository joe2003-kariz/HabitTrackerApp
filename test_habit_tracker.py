import pytest
from habit import Habit
from habit_manager import HabitManager

def test_habit_creation():
    habit = Habit('Test Habit', 'daily')
    assert habit.name == 'Test Habit'
    assert habit.periodicity == 'daily'

def test_add_habit():
    manager = HabitManager()
    manager.add_habit('Test Habit', 'daily')
    assert len(manager.habits) == 1

def test_delete_habit():
    manager = HabitManager()
    manager.add_habit('Test Habit', 'daily')
    manager.delete_habit('Test Habit')
    assert len(manager.habits) == 0

if __name__ == '__main__':
    pytest.main()
