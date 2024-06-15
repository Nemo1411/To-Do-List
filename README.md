Here's the updated `README.md` file for your To-Do List application:

```markdown
# To-Do List Application

This is a simple to-do list application built with Flask for the backend and plain HTML/CSS/JavaScript for the frontend. It allows users to add tasks, mark them as completed or not, and delete tasks.

## Features

- Add a new task
- Mark a task as completed or not completed
- Delete a task
- Display all tasks

## Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/todo-list-app.git
   cd todo-list-app
   ```

2. Install the dependencies:
   ```bash
   pip install Flask Flask-SQLAlchemy
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://127.0.0.1:5000`.

## Usage

1. Open the application in your web browser.
2. Add new tasks using the input field and "Add Task" button.
3. Click on the "Complete" button to mark a task as completed.
4. Click on the "Undo" button to mark a task as not completed.
5. Click on the "Delete" button to remove a task.

## Directory Structure

```
todo-list-app/
│
├── app.py
├── templates/
│   └── index.html
└── static/
```

- `app.py`: The main Flask application file.
- `templates/index.html`: The HTML file for the frontend.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Author

Nemo (ryaneirbouh@gmail.com)
```
