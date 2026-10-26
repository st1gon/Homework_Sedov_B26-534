class Task:
    def __init__(self, title, priority, status, due_date):
        self.title = title
        self.priority = priority
        self.status = status
        self.due_date = due_date

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_high_priority_tasks(self):
        return [t.title for t in self.tasks if t.priority == "High"]
