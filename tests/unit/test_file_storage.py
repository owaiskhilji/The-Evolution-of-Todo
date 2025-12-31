"""
Unit tests for the FileStorage class.
"""

import os
import tempfile
import json
import pytest
from src.lib.file_storage import FileStorage
from src.models.task import Task


def test_storage_initialization():
    """Test that storage is initialized correctly."""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = tmp.name

    try:
        storage = FileStorage(tmp_path)

        assert storage.get_all_tasks() == []
        assert storage._next_id == 1
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)


def test_add_task():
    """Test adding a task to storage."""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = tmp.name

    try:
        storage = FileStorage(tmp_path)

        task = storage.add_task("Test task")

        assert task.id == 1
        assert task.title == "Test task"
        assert task.status == "Pending"
        assert len(storage.get_all_tasks()) == 1
        assert storage.get_all_tasks()[0] == task

        # Check that the task was saved to file
        with open(tmp_path, 'r') as f:
            data = json.load(f)
            assert len(data['tasks']) == 1
            assert data['tasks'][0]['id'] == 1
            assert data['tasks'][0]['title'] == "Test task"
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)


def test_get_task_by_id():
    """Test retrieving a task by ID."""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = tmp.name

    try:
        storage = FileStorage(tmp_path)

        task = storage.add_task("Test task")

        retrieved_task = storage.get_task_by_id(task.id)

        assert retrieved_task is not None
        assert retrieved_task.id == task.id
        assert retrieved_task.title == task.title
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)


def test_get_task_by_id_not_found():
    """Test retrieving a non-existent task returns None."""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = tmp.name

    try:
        storage = FileStorage(tmp_path)

        retrieved_task = storage.get_task_by_id(999)

        assert retrieved_task is None
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)


def test_update_task():
    """Test updating a task."""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = tmp.name

    try:
        storage = FileStorage(tmp_path)

        task = storage.add_task("Test task")
        result = storage.update_task(task.id, status="Completed")

        assert result is True
        updated_task = storage.get_task_by_id(task.id)
        assert updated_task is not None
        assert updated_task.status == "Completed"

        # Check that the update was saved to file
        with open(tmp_path, 'r') as f:
            data = json.load(f)
            assert data['tasks'][0]['status'] == "Completed"
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)


def test_update_task_not_found():
    """Test updating a non-existent task returns False."""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = tmp.name

    try:
        storage = FileStorage(tmp_path)

        result = storage.update_task(999, status="Completed")

        assert result is False
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)


def test_delete_task():
    """Test deleting a task."""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = tmp.name

    try:
        storage = FileStorage(tmp_path)

        task = storage.add_task("Test task")
        result = storage.delete_task(task.id)

        assert result is True
        assert storage.get_all_tasks() == []
        assert storage.get_task_by_id(task.id) is None

        # Check that the deletion was saved to file
        with open(tmp_path, 'r') as f:
            data = json.load(f)
            assert len(data['tasks']) == 0
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)


def test_delete_task_not_found():
    """Test deleting a non-existent task returns False."""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = tmp.name

    try:
        storage = FileStorage(tmp_path)

        result = storage.delete_task(999)

        assert result is False
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)


def test_multiple_tasks_unique_ids():
    """Test that multiple tasks get unique IDs."""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = tmp.name

    try:
        storage = FileStorage(tmp_path)

        task1 = storage.add_task("First task")
        task2 = storage.add_task("Second task")
        task3 = storage.add_task("Third task")

        assert task1.id == 1
        assert task2.id == 2
        assert task3.id == 3
        assert len(storage.get_all_tasks()) == 3
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)


def test_data_persistence():
    """Test that data persists between storage instances."""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = tmp.name

    try:
        # Add tasks with first instance
        storage1 = FileStorage(tmp_path)
        storage1.add_task("First task")
        storage1.add_task("Second task")

        # Create a new instance and verify data is loaded
        storage2 = FileStorage(tmp_path)
        tasks = storage2.get_all_tasks()

        assert len(tasks) == 2
        assert tasks[0].title == "First task"
        assert tasks[1].title == "Second task"
        assert storage2._next_id == 3  # Next ID should be 3
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)


def test_load_from_existing_file():
    """Test loading from an existing file with data."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as tmp:
        tmp_path = tmp.name
        # Write test data to file
        data = {
            'tasks': [
                {'id': 1, 'title': 'Existing task', 'status': 'Pending'},
                {'id': 2, 'title': 'Another task', 'status': 'Completed'}
            ],
            'next_id': 5
        }
        json.dump(data, tmp)

    try:
        storage = FileStorage(tmp_path)

        tasks = storage.get_all_tasks()
        assert len(tasks) == 2
        assert tasks[0].id == 1
        assert tasks[0].title == "Existing task"
        assert tasks[0].status == "Pending"
        assert tasks[1].id == 2
        assert tasks[1].title == "Another task"
        assert tasks[1].status == "Completed"
        assert storage._next_id == 5
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)