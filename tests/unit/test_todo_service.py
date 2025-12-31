"""
Unit tests for the TodoService functionality.
"""

import pytest
import tempfile
import os
from src.services.todo_service import TodoService
from src.models.task import Task


def test_add_task_success():
    """Test successfully adding a task."""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = tmp.name

    try:
        service = TodoService(storage_file=tmp_path)

        task = service.add_task("Test task")

        assert isinstance(task, Task)
        assert task.id == 1
        assert task.title == "Test task"
        assert task.status == "Pending"
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)


def test_add_task_empty_title():
    """Test adding a task with empty title raises error."""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = tmp.name

    try:
        service = TodoService(storage_file=tmp_path)

        with pytest.raises(ValueError, match="Task title cannot be empty"):
            service.add_task("")

        with pytest.raises(ValueError, match="Task title cannot be empty"):
            service.add_task("   ")
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)


def test_add_multiple_tasks_unique_ids():
    """Test that multiple tasks get unique IDs."""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = tmp.name

    try:
        service = TodoService(storage_file=tmp_path)

        task1 = service.add_task("First task")
        task2 = service.add_task("Second task")
        task3 = service.add_task("Third task")

        assert task1.id == 1
        assert task2.id == 2
        assert task3.id == 3
        assert task1.title == "First task"
        assert task2.title == "Second task"
        assert task3.title == "Third task"
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)


def test_add_task_trims_whitespace():
    """Test that task title is trimmed of whitespace."""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = tmp.name

    try:
        service = TodoService(storage_file=tmp_path)

        task = service.add_task("   Task with spaces   ")

        assert task.title == "Task with spaces"
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)


def test_view_tasks_empty():
    """Test viewing tasks when no tasks exist."""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = tmp.name

    try:
        service = TodoService(storage_file=tmp_path)

        tasks = service.view_tasks()

        assert tasks == []
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)


def test_view_tasks_with_tasks():
    """Test viewing tasks when tasks exist."""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = tmp.name

    try:
        service = TodoService(storage_file=tmp_path)

        service.add_task("First task")
        service.add_task("Second task")

        tasks = service.view_tasks()

        assert len(tasks) == 2
        assert tasks[0].id == 1
        assert tasks[0].title == "First task"
        assert tasks[0].status == "Pending"
        assert tasks[1].id == 2
        assert tasks[1].title == "Second task"
        assert tasks[1].status == "Pending"
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)


def test_view_tasks_returns_copy():
    """Test that view_tasks returns a copy of the tasks."""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = tmp.name

    try:
        service = TodoService(storage_file=tmp_path)

        service.add_task("Test task")
        tasks1 = service.view_tasks()
        tasks2 = service.view_tasks()

        # Modifying one list should not affect the other
        tasks1.append(Task(id=999, title="Fake task", status="Pending"))

        assert len(tasks1) == 2
        assert len(tasks2) == 1
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)


def test_complete_task_success():
    """Test successfully completing a task."""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = tmp.name

    try:
        service = TodoService(storage_file=tmp_path)

        task = service.add_task("Test task")
        result = service.complete_task(task.id)

        assert result is True
        updated_task = service.view_tasks()[0]
        assert updated_task.status == "Completed"
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)


def test_complete_task_not_found():
    """Test completing a non-existent task returns False."""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = tmp.name

    try:
        service = TodoService(storage_file=tmp_path)

        result = service.complete_task(999)

        assert result is False
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)


def test_complete_task_already_completed():
    """Test completing an already completed task."""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = tmp.name

    try:
        service = TodoService(storage_file=tmp_path)

        task = service.add_task("Test task")
        service.complete_task(task.id)  # Complete it once
        result = service.complete_task(task.id)  # Try to complete again

        assert result is True
        updated_task = service.view_tasks()[0]
        assert updated_task.status == "Completed"
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)


def test_delete_task_success():
    """Test successfully deleting a task."""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = tmp.name

    try:
        service = TodoService(storage_file=tmp_path)

        task = service.add_task("Test task")
        result = service.delete_task(task.id)

        assert result is True
        assert len(service.view_tasks()) == 0
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)


def test_delete_task_not_found():
    """Test deleting a non-existent task returns False."""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = tmp.name

    try:
        service = TodoService(storage_file=tmp_path)

        result = service.delete_task(999)

        assert result is False
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)


def test_delete_task_with_multiple_tasks():
    """Test deleting one task doesn't affect others."""
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = tmp.name

    try:
        service = TodoService(storage_file=tmp_path)

        task1 = service.add_task("First task")
        task2 = service.add_task("Second task")
        task3 = service.add_task("Third task")

        # Delete the middle task
        result = service.delete_task(task2.id)

        assert result is True
        remaining_tasks = service.view_tasks()
        assert len(remaining_tasks) == 2
        assert remaining_tasks[0].id == 1
        assert remaining_tasks[0].title == "First task"
        assert remaining_tasks[1].id == 3
        assert remaining_tasks[1].title == "Third task"
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)