# 🚀 Python Challenge: Tasks API

Welcome! Your goal is to finalize a modular Task Management API. We have provided the architecture and database configuration; you must implement the core logic.

**Estimated Time:** 40 minutes.

## Your Task

You are responsible for implementing the logic required for Requirements 2 and 3.

You should ensure your implementation follows the established architectural pattern (Route -> Service -> Model) and provides consistent JSON error responses when a request cannot be processed.

Feel free to:
1. Install new dependencies to the project
2. Use Documentation
3. Use AI agents
4. Improve the code

## Requirements

### 1. GET `/tasks` (Already Implemented)
* Fetch all tasks.
* **Filter:** Must support an optional query parameter `status` (e.g., `/tasks?status=pending`).

### 2. POST `/tasks`
* Receive a JSON body with `title`.
* **Validation:** The `title` must be at least 5 characters long.
* **Response:** `201 Created` or `400 Bad Request`.

### 3. PATCH `/tasks/<id>/complete`
* Mark a task as "completed".
* **Validation:** * If ID doesn't exist: `404 Not Found`.
    * If already completed: `409 Conflict`.
* **Response:** `200 OK`.

## Setup

1. **Database:** `docker-compose up`
2. **Environment:** `pip install -r requirements.txt`
3. **Run:** `python main.py`

## Testing

We have provided a suite of tests to validate the GET endpoint. You can use these as a reference to build tests for your new implementation.

To run the tests:

`pytest`

### Good luck! And have fun :)