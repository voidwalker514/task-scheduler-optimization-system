class Task:
    def __init__(self, task_id, name, priority, deadline, duration, profit):
        self.task_id = task_id
        self.name = name
        self.priority = priority    # 1 is Highest Priority
        self.deadline = deadline    # Time by which it must be finished
        self.duration = duration    # Time required to complete the task
        self.profit = profit        # Importance score / Profit

    def __lt__(self, other):
        # Fallback comparison for heapq if priority, deadline, and profit are identical
        return self.task_id < other.task_id

    def __repr__(self):
        return f"Task({self.name}, P:{self.priority}, D:{self.deadline}, T:{self.duration}, Profit:{self.profit})"
