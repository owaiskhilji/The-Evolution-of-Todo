# Todo App API Contract

## CLI Commands Interface

### Add Task Command
- **Command**: `add <title>`
- **Input**: title (string)
- **Output**: task_id (integer)
- **Success**: Returns unique task ID of newly created task
- **Error**: Returns error message if operation fails

### View Tasks Command
- **Command**: `view`
- **Input**: None
- **Output**: List of tasks (array of objects with id, title, status)
- **Success**: Returns all tasks with their details
- **Error**: Returns empty list if no tasks exist

### Complete Task Command
- **Command**: `complete <id>`
- **Input**: id (integer)
- **Output**: success message or error
- **Success**: Updates task status to 'Completed'
- **Error**: Returns error if task ID doesn't exist

### Delete Task Command
- **Command**: `delete <id>`
- **Input**: id (integer)
- **Output**: success message or error
- **Success**: Removes task from storage
- **Error**: Returns error if task ID doesn't exist

## Data Format
### Task Object
```
{
  "id": integer,
  "title": string,
  "status": "Pending" | "Completed"
}
```

## Error Responses
All error responses follow the format:
```
{
  "error": "error message",
  "code": error_code
}
```