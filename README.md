# Task Management API

A Django-based API for managing tasks. This API allows users to create, update, delete, and mark tasks as complete or incomplete.

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

bash
git clone [https://github.com/](https://github.com/)<your-username>/task-management-api.git
cd task-management-api

### Step 2: Set Up a Virtual Environment

##### Create and activate a virtual environment:

On Windows (PowerShell):

PowerShell

python -m venv env
.\env\Scripts\Activate
On macOS/Linux:

Bash

python3 -m venv env
source env/bin/activate

### Step 3: Install Dependencies

##### Install the required Python packages:

`pip install -r requirements.txt`

### Step 4: Configure the Database

##### By default, the project uses SQLite for development. To use a different database:

Update the database settings in task_management/settings.py.
Apply migrations:

`
python manage.py makemigrations
python manage.py migrate

`

### Step 5: Run the Development Server

##### Start the Django development server:

`python manage.py runserver`

### Step 6: Access the Application

##### Open your browser and navigate to:

Note: The default development server address is http://127.0.0.1:8000/. This port number might be different in your setup.

### Step 7: Deactivate the Virtual Environment

##### Once you're done, deactivate the virtual environment:

Bash

deactivate

## Additional Information

For further customization or deployment instructions, please refer to the Django documentation or contact the project maintainer
