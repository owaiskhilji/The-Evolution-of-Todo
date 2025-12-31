"""
Unit tests for the Task model.
"""

import pytest
from src.models.task import Task


def test_task_creation_valid():
    """Test creating a valid task."""
    task = Task(id=1, title="Test task", status="Pending")

    assert task.id == 1
    assert task.title == "Test task"
    assert task.status == "Pending"


def test_task_creation_defaults():
    """Test creating a task with default status."""
    task = Task(id=1, title="Test task")

    assert task.id == 1
    assert task.title == "Test task"
    assert task.status == "Pending"


def test_task_complete_method():
    """Test the complete method."""
    task = Task(id=1, title="Test task", status="Pending")

    task.complete()

    assert task.status == "Completed"


def test_task_to_dict():
    """Test converting task to dictionary."""
    task = Task(id=1, title="Test task", status="Pending")
    task_dict = task.to_dict()

    assert task_dict == {
        "id": 1,
        "title": "Test task",
        "status": "Pending"
    }


def test_task_id_validation():
    """Test that task ID must be positive."""
    with pytest.raises(ValueError):
        Task(id=0, title="Test task")

    with pytest.raises(ValueError):
        Task(id=-1, title="Test task")


def test_task_title_validation():
    """Test that task title cannot be empty."""
    with pytest.raises(ValueError):
        Task(id=1, title="")

    with pytest.raises(ValueError):
        Task(id=1, title="   ")

    # Valid title should work
    task = Task(id=1, title="Valid title")
    assert task.title == "Valid title"


def test_task_status_validation():
    """Test that task status must be valid."""
    with pytest.raises(ValueError):
        Task(id=1, title="Test task", status="InvalidStatus")  # type: ignore

    # Valid statuses should work
    pending_task = Task(id=1, title="Test task", status="Pending")
    assert pending_task.status == "Pending"

    completed_task = Task(id=2, title="Test task", status="Completed")
    assert completed_task.status == "Completed"