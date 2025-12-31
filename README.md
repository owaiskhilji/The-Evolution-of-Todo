# Todo App

A CLI-based Todo application built with Python 3.13.

## Features

- Add new todo tasks
- View all todo tasks
- Mark tasks as completed
- Update tasks
- Delete tasks
- Data persists between sessions (stored in todo_data.json)

## Installation

1. Make sure you have Python 3.13 and `uv` installed
2. Clone this repository
3. Run `uv sync` to install dependencies
4. Run the application with `uv run src.cli.main` or `python -m src.cli.main`

## Usage

```bash
# Add a new task
python -m src.cli.main add "Buy groceries"

# View all tasks
python -m src.cli.main view

# Complete a task (with ID 1)
python -m src.cli.main complete 1

# Update a task (with ID 1)
python -m src.cli.main update 1 "update task"

# Delete a task (with ID 1)
python -m src.cli.main delete 1
```

## Data Storage

Task data is persisted in a `todo_data.json` file in the current directory. The file is automatically created when you add your first task and updated with each operation.
