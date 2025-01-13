# Task Management API

A Django-based API for managing tasks. This API allows users to create, update, delete, and mark tasks as complete or incomplete.

##### Try it out live:
 [https://task-management-api-42al.onrender](https://task-management-api-42al.onrender.com/api/tasks/)
```
User account : 
 {
   username: admin,
   password: admin
 },
  {
   username: victor,
   password: victor
 }
```

## Features

- CRUD operations for tasks and users.
- Mark tasks as complete or incomplete.
- User authentication and management.

## Setup Instructions

### Prerequisites

Ensure you have the following installed on your machine:

1. Python (version 3.8 or higher)
2. pip (Python package manager)
3. Virtual environment package (`venv`)
4. Git

### Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

git clone [https://github.com/](https://github.com/)<your-username>/task-management-api.git
`cd task-management-api`

### Step 2: Set Up a Virtual Environment

##### Create and activate a virtual environment:

On Windows (PowerShell):

```
python -m venv env
.\env\Scripts\Activate
```

#### On macOS/Linux:

```
python3 -m venv env
source env/bin/activate
```

### Step 3: Install Dependencies

##### Install the required Python packages:

`pip install -r requirements.txt`

### Step 4: Configure the Database

##### By default, the project uses SQLite for development. To use a different database:

Update the database settings in task_management/settings.py.
Apply migrations:

```
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Run the Development Server

##### Start the Django development server:

`python manage.py runserver`

### Step 6: Access the Application

##### Open your browser and navigate to:

Note: The default development server address is http://127.0.0.1:8000/. This port number might be different in your setup.

## API Endpoints
`http://127.0.0.1:8000/api/`
### User Endpoints
```
POST /users/: Create a new user.
GET /users/: List all users.
GET /users/{id}/: Retrieve details of a specific user.
PUT /users/{id}/: Update an existing user.
DELETE /users/{id}/: Delete a user.
```
### Task Endpoints
```
POST /tasks/: Create a new task.
GET /tasks/: List all tasks, with optional filters for status, priority, and due date.
GET /tasks/{id}/: Retrieve details of a specific task.
PUT /tasks/{id}/: Update an existing task.
DELETE /tasks/{id}/: Delete a task.
PATCH /tasks/{id}/complete/: Mark a task as completed.
PATCH /tasks/{id}/incomplete/: Mark a task as incomplete.
```
### Filtering and Sorting Tasks
The following query parameters can be used with the GET /tasks/ endpoint:

- **status**: Filter tasks by status. (e.g., `status=Pending` or `status=Completed`)  
- **priority**: Filter tasks by priority. (e.g., `priority=High`, `priority=Medium`, `priority=Low`)  
- **due_date**: Filter tasks by due date. (e.g., `due_date=2025-01-20`)  
- **sort_by**: Sort tasks by due date or priority. (e.g., `sort_by=due_date`, `sort_by=priority`)  
- **order**: Order tasks in ascending or descending order. (e.g., `order=asc` or `order=desc`)  

#### Example Request for Filtering Tasks
`GET /api/tasks/?status=Pending&priority=High`
```
[
    {
        "title": "Task 2",
        "description": "Scheduled for completion",
        "due_date": "2025-01-19 15:24:12",
        "priority": "High",
        "status": "Pending",
        "completed_at": null
    }
]
```
#### Example Request for Sorting Tasks
`GET /api/tasks/?sort_by=due_date&order=asc`
```
[
    {
        "title": "Task 4",
        "description": "Needs follow-up",
        "due_date": "2025-01-11 15:24:12",
        "priority": "Medium",
        "status": "Pending",
        "completed_at": null
    },
    {
        "title": "Task 1",
        "description": "To be started",
        "due_date": "2025-01-19 15:24:12",
        "priority": "Medium",
        "status": "Completed",
        "completed_at": "2025-01-10 15:24:12"
    }
]
```
#### Example Request for Task Creation
`POST /api/tasks/`
```
{
    "title": "Task 1",
    "description": "To be started",
    "due_date": "2025-01-19 15:24:12",
    "priority": "Medium",
    "status": "Completed",
    "completed_at": "2025-01-10 15:24:12"
}
```
#### Example Request for Task Update
`PUT /api/tasks/{id}/`
```
{
    "title": "Updated Task 1",
    "description": "Task has been started",
    "due_date": "2025-01-20 15:24:12",
    "priority": "High",
    "status": "Pending",
    "completed_at": null
}
```

### Step 7: Deactivate the Virtual Environment

##### Once you're done, deactivate the virtual environment:

`deactivate`

## Additional Information

For further customization or deployment instructions, please refer to the Django documentation or contact the project maintainer
