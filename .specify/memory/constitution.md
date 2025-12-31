<!-- SYNC IMPACT REPORT
Version change: N/A → 1.0.0
Added sections: Core Principles (6 principles), Development Standards, Sub-Agent Delegation, Governance
Removed sections: None
Modified principles: N/A (new constitution)
Templates requiring updates:
  - .specify/templates/plan-template.md ⚠ pending
  - .specify/templates/spec-template.md ⚠ pending
  - .specify/templates/tasks-template.md ⚠ pending
  - .specify/templates/commands/*.md ⚠ pending
Follow-up TODOs: None
-->
# Todo App Constitution

## Core Principles

### I. Python 3.13 Standard
All code must be written in Python 3.13 with strict adherence to modern Python standards and best practices. Dependencies must be managed using `uv` package manager for consistency and performance.

### II. Modular Architecture
Code must be modular and stored in the `src/` directory. Each component should have a single responsibility and be independently testable and maintainable.

### III. Business Logic Compliance (NON-NEGOTIABLE)
All business logic must be derived from @.claude/skills/todo-logic.md. Any deviation from the defined logic requires explicit approval and documentation of the change rationale.

### IV. In-Memory Storage Phase 1
Phase 1 implementation must use in-memory storage only. No persistent database solutions should be implemented during this phase. This ensures rapid development and testing capabilities.

### V. Type Safety and Documentation
All code must include type hints and clear documentation. Clean, well-documented code is required for maintainability and team collaboration.

### VI. Sub-Agent Delegation
For coding tasks, delegate to the 'Developer-Agent'. For testing, ensure the code follows the specifications in the `specs/` folder. This ensures proper workload distribution and specialized handling.

## Development Standards

- Always use Python 3.13 and `uv` for dependency management
- Code must be modular and stored in the `src/` directory
- Phase 1: In-memory storage only
- Use clean, documented Python code with type hints
- All business logic must be derived from @.claude/skills/todo-logic.md

## Sub-Agent Delegation

- For coding tasks, delegate to the 'Developer-Agent'
- For testing, ensure the code follows the specifications in the `specs/` folder
- Agent responsibilities must be clearly defined and followed

## Governance

The Lead Architect is responsible for ensuring all development aligns with this constitution. All code reviews must verify compliance with these principles. Any architectural decisions that conflict with these principles require explicit approval from the Lead Architect.

**Version**: 1.0.0 | **Ratified**: 2025-12-31 | **Last Amended**: 2025-12-31