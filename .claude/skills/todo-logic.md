# Todo Logic Skill

## Goal
The objective is to define the logic for a basic CLI Todo application for Phase 1, using Python 3.13 and In-memory storage.

## Core Functions
1. **add_task(title)**: Saves a new task to the list.
2. **view_tasks()**: Displays all tasks, including their unique ID and Status.
3. **delete_task(id)**: Removes a specific task using its unique ID.
4. **complete_task(id)**: Updates a task's status from 'Pending' to 'Completed' using its unique ID.

## Data Structure
Tasks will be stored as a list of dictionaries with the following schema:
- `id`: A unique integer for identification.
- `title`: A string representing the task description.
- `status`: A string indicating the task's state (Pending or Completed).

## Rules
- Always write modular code by separating logic into distinct functions.
- Use the `uv` package manager for dependency and environment management.
- For Phase 1, do not use a persistent database (like SQL); store data exclusively in memory.