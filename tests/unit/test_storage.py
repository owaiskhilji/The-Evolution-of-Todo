"""
Unit tests for the InMemoryStorage class.
"""

import pytest
from src.lib.storage import InMemoryStorage
from src.models.task import Task


def test_storage_initialization():
    """Test that storage is initialized correctly."""
    storage = InMemoryStorage()

    assert storage.get_all_tasks() == []
    assert storage._next_id == 1


def test_add_task():
    """Test adding a task to storage."""
    storage = InMemoryStorage()

    task = storage.add_task("Test task")

    assert task.id == 1
    assert task.title == "Test task"
    assert task.status == "Pending"
    assert len(storage.get_all_tasks()) == 1
    assert storage.get_all_tasks()[0] == task


def test_get_task_by_id():
    """Test retrieving a task by ID."""
    storage = InMemoryStorage()

    task = storage.add_task("Test task")

    retrieved_task = storage.get_task_by_id(task.id)

    assert retrieved_task is not None
    assert retrieved_task.id == task.id
    assert retrieved_task.title == task.title


def test_get_task_by_id_not_found():
    """Test retrieving a non-existent task returns None."""
    storage = InMemoryStorage()

    retrieved_task = storage.get_task_by_id(999)

    assert retrieved_task is None


def test_update_task():
    """Test updating a task."""
    storage = InMemoryStorage()

    task = storage.add_task("Test task")
    result = storage.update_task(task.id, status="Completed")

    assert result is True
    updated_task = storage.get_task_by_id(task.id)
    assert updated_task is not None
    assert updated_task.status == "Completed"


def test_update_task_not_found():
    """Test updating a non-existent task returns False."""
    storage = InMemoryStorage()

    result = storage.update_task(999, status="Completed")

    assert result is False


def test_delete_task():
    """Test deleting a task."""
    storage = InMemoryStorage()

    task = storage.add_task("Test task")
    result = storage.delete_task(task.id)

    assert result is True
    assert storage.get_all_tasks() == []
    assert storage.get_task_by_id(task.id) is None


def test_delete_task_not_found():
    """Test deleting a non-existent task returns False."""
    storage = InMemoryStorage()

    result = storage.delete_task(999)

    assert result is False


def test_multiple_tasks_unique_ids():
    """Test that multiple tasks get unique IDs."""
    storage = InMemoryStorage()

    task1 = storage.add_task("First task")
    task2 = storage.add_task("Second task")
    task3 = storage.add_task("Third task")

    assert task1.id == 1
    assert task2.id == 2
    assert task3.id == 3
    assert len(storage.get_all_tasks()) == 3


def test_clear_all():
    """Test clearing all tasks."""
    storage = InMemoryStorage()

    storage.add_task("Test task")
    storage.add_task("Another task")

    assert len(storage.get_all_tasks()) == 2

    storage.clear_all()

    assert storage.get_all_tasks() == []
    assert storage._next_id == 1  # Should reset to 1