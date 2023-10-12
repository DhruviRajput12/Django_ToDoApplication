# Django_ToDoApplication

# Django ToDo App

A simple ToDo web application built with Django that allows you to manage your tasks. It provides features like adding, updating, and deleting tasks, and it uses DataTables for a clean, organized interface with a search function for tasks.

## Features

- Create, update, and delete tasks.
- Clean and organized interface using DataTables.
- Search functionality to easily find tasks.

## Getting Started

### Prerequisites

- Python 3.x
- Django (install using `pip install django`)

### Installation

1. Clone the repository:
   git clone https://github.com/yourusername/django-todo-app.git

2. Navigate to the project directory:
    cd django-todo-app

3. Create and activate a virtual environment:
    python -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate

4. Install the required packages:
    pip install -r requirements.txt
    
5. Run the migrations:
    python manage.py migrate

6. Create a superuser:
    python manage.py createsuperuser

7. Start the development server:
    python manage.py runserver

    Access the ToDo app by visiting http://localhost:8000/.
    Log in with the superuser account created earlier.
    You can now add, update, and delete tasks from the Task Page.


# Screenshots
<h3> Home Page </h3>
<div align="center">
  <img src="https://github.com/DhruviRajput12/Django_ToDoApplication/blob/master/homepage.png" alt="homepage" />
</div>

<h3> Task Page <h3> 
<div align="center">
  <img src="https://github.com/DhruviRajput12/Django_ToDoApplication/blob/master/taskpage.png" alt="taskpage" />
</div>

<h3> Update Task Page <h3> 
<div align="center">
  <img src="https://github.com/DhruviRajput12/Django_ToDoApplication/blob/master/updatetask.png" alt="updatetaskpage" />
</div>

<h3> Delete Task Page <h3> 
<div align="center">
  <img src="https://github.com/DhruviRajput12/Django_ToDoApplication/blob/master/deletetask.png" alt="deletetaskpage" />
</div>




