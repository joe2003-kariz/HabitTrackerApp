# Habit Tracker App

## Introduction
The Habit Tracker App is a Python-based command-line application designed to help users build and maintain productive habits. It allows users to create habits, mark them as completed, and analyze their progress over time.

## Features
- **Habit Creation**: Create new habits with a specified periodicity (daily, weekly, monthly).
- **Habit Completion**: Mark habits as completed on specific dates.
- **Habit Deletion**: Remove habits that are no longer needed.
- **Analytics**: Analyze habits to determine the longest streaks and overall performance.

## Installation
1. Clone the repository:
    ```bash
    git clone [https://github.com/yourusername/habit-tracker.git](https://github.com/joe2003-kariz/HabitTrackerApp.git)
    cd habit-tracker
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Initialize the database:
    ```bash
    python initialize_db.py
    ```

## Usage
### Command-Line Interface (CLI) Commands
- **Create a Habit**: Define a new habit with a name and periodicity.
    ```bash
    python cli.py create_habit "Drink Water" daily
    ```
- **List Habits**: View all existing habits.
    ```bash
    python cli.py list_habits
    ```
- **Delete a Habit**: Remove a habit by its name.
    ```bash
    python cli.py delete_habit "Drink Water"
    ```
- **Complete a Habit**: Mark a habit as completed on the current date.
    ```bash
    python cli.py check_off "Drink Water"
    ```
- **Analyze Habits**: Get insights into habit performance.
    ```bash
    python cli.py analyze_habits
    ```


