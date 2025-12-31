# Quickstart Guide: Phase 1 Todo App

## Prerequisites
- Python 3.13 installed
- `uv` package manager installed

## Setup
1. Clone the repository
2. Navigate to the project directory
3. Install dependencies using `uv sync`

## Running the Application
Execute the CLI application:
```bash
python -m src.cli.main
```

## Basic Usage
1. **Add a task**: Use the add command with a task title
2. **View tasks**: Use the view command to see all tasks
3. **Complete a task**: Use the complete command with a task ID
4. **Delete a task**: Use the delete command with a task ID

## Example Commands
```bash
# Add a new task
python -m src.cli.main add "Buy groceries"

# View all tasks
python -m src.cli.main view

# Complete a task (with ID 1)
python -m src.cli.main complete 1

# Delete a task (with ID 1)
python -m src.cli.main delete 1
```

## Architecture Overview
- **Models**: Task data model in `src/models/task.py`
- **Services**: Business logic in `src/services/todo_service.py`
- **CLI**: User interface in `src/cli/main.py`
- **Storage**: In-memory storage in `src/lib/storage.py`