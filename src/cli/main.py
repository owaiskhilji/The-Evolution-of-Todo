"""
CLI interface for the Todo application.
"""

import sys
import argparse
from typing import List
from src.services.todo_service import TodoService


def create_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser for the CLI."""
    parser = argparse.ArgumentParser(
        description="CLI-based Todo application",
        prog="todo"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", type=str, help="The title of the task to add")

    # View command
    view_parser = subparsers.add_parser("view", help="View all tasks")

    # Complete command
    complete_parser = subparsers.add_parser("complete", help="Mark a task as completed")
    complete_parser.add_argument("id", type=int, help="The ID of the task to complete")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="The ID of the task to delete")

    # Update command
    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("id", type=int, help="The ID of the task to update")
    update_parser.add_argument("title", type=str, help="The new title for the task")

    return parser


def main(args: List[str] = None) -> int:
    """
    Main entry point for the CLI application.

    Args:
        args: Command line arguments (defaults to sys.argv)

    Returns:
        Exit code (0 for success, non-zero for errors)
    """
    if args is None:
        args = sys.argv[1:]

    parser = create_parser()
    parsed_args = parser.parse_args(args)

    # Initialize the todo service with file storage
    service = TodoService()

    # Execute the appropriate command
    try:
        if parsed_args.command == "add":
            task = service.add_task(parsed_args.title)
            print(f"Task added with ID: {task.id}")
            return 0

        elif parsed_args.command == "view":
            tasks = service.view_tasks()
            if not tasks:
                print("No tasks found.")
            else:
                for task in tasks:
                    status_icon = "X" if task.status == "Completed" else "O"
                    print(f"[{status_icon}] {task.id}: {task.title}")
            return 0

        elif parsed_args.command == "complete":
            if service.complete_task(parsed_args.id):
                print(f"Task {parsed_args.id} marked as completed.")
            else:
                print(f"Error: Task with ID {parsed_args.id} not found.")
                return 1
            return 0

        elif parsed_args.command == "delete":
            if service.delete_task(parsed_args.id):
                print(f"Task {parsed_args.id} deleted.")
            else:
                print(f"Error: Task with ID {parsed_args.id} not found.")
                return 1
            return 0

        elif parsed_args.command == "update":
            # For now, we'll just update the title of the task
            if service.storage.update_task(parsed_args.id, title=parsed_args.title):
                print(f"Task {parsed_args.id} updated to: {parsed_args.title}")
            else:
                print(f"Error: Task with ID {parsed_args.id} not found.")
                return 1
            return 0

        else:
            # No command provided, show help
            parser.print_help()
            return 0

    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())