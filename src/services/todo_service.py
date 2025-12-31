"""
Core business logic for the Todo application.
"""

from typing import List
from src.models.task import Task
from src.lib.file_storage import FileStorage
from src.lib.errors import TaskNotFoundError


class TodoService:
    """
    Service class that handles the core business logic for the Todo application.
    """

    def __init__(self, storage_file: str = "todo_data.json") -> None:
        """Initialize the service with file-based storage."""
        self.storage = FileStorage(storage_file)

    def add_task(self, title: str) -> Task:
        """
        Add a new task to the todo list.

        Args:
            title: The title of the task to add

        Returns:
            The newly created Task object with a unique ID
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")

        return self.storage.add_task(title.strip())

    def view_tasks(self) -> List[Task]:
        """
        View all tasks in the todo list.

        Returns:
            A list of all tasks
        """
        return self.storage.get_all_tasks()

    def complete_task(self, task_id: int) -> bool:
        """
        Mark a task as completed.

        Args:
            task_id: The ID of the task to mark as completed

        Returns:
            True if the task was found and updated, False otherwise
        """
        task = self.storage.get_task_by_id(task_id)
        if task is None:
            return False

        return self.storage.update_task(task_id, status="Completed")

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task from the todo list.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if the task was found and deleted, False otherwise
        """
        return self.storage.delete_task(task_id)