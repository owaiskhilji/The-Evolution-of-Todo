"""
Task data model for the Todo application.
"""

from dataclasses import dataclass
from typing import Literal

TaskStatus = Literal["Pending", "Completed"]


@dataclass
class Task:
    """
    Represents a single todo item with id, title, and status.

    Attributes:
        id: A unique integer identifier for the task
        title: A string representing the task description
        status: A string indicating the task's state ('Pending' or 'Completed')
    """

    id: int
    title: str
    status: TaskStatus = "Pending"

    def __post_init__(self):
        """Validate the task after initialization."""
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError(f"Task ID must be a positive integer, got {self.id}")

        if not isinstance(self.title, str) or not self.title.strip():
            raise ValueError(f"Task title must be a non-empty string, got {self.title}")

        if self.status not in ["Pending", "Completed"]:
            raise ValueError(f"Task status must be 'Pending' or 'Completed', got {self.status}")

    def complete(self) -> None:
        """Mark the task as completed."""
        self.status = "Completed"

    def to_dict(self) -> dict:
        """Convert the task to a dictionary representation."""
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status
        }