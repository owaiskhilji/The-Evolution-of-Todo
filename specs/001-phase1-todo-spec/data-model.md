# Data Model: Phase 1 Todo App

## Task Entity

### Attributes
- **id**: Integer
  - Unique identifier for each task
  - Auto-incremented when new tasks are created
  - Primary key for the task

- **title**: String
  - Represents the task description
  - Required field when creating a task
  - Can contain any text content

- **status**: String
  - Represents the task's state
  - Valid values: 'Pending', 'Completed'
  - Default value: 'Pending' when task is created

### State Transitions
- **Initial State**: 'Pending' (when task is created via add_task)
- **Transition**: 'Pending' → 'Completed' (when complete_task is called)
- **Final State**: 'Completed' (no further transitions)

### Validation Rules
- id must be unique across all tasks
- title must not be empty
- status must be either 'Pending' or 'Completed'
- id must be a positive integer

### Relationships
- The Task entity is independent (no relationships with other entities in Phase 1)