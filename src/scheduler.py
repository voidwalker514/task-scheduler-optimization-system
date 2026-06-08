import heapq

class TaskScheduler:
    def __init__(self):
        self.task_queue = [] # Min-heap for Priority Queue
        self.completed_tasks = []
        self.missed_tasks = []
        self.total_profit = 0
        self.total_time_spent = 0

    def add_task(self, task):
        """
        Adds a task to the Priority Queue.
        Priority logic:
        1. Highest priority first (lowest integer value)
        2. Earliest deadline
        3. Highest profit (-profit for min-heap)
        """
        heapq.heappush(self.task_queue, (task.priority, task.deadline, -task.profit, task))

    def run_schedule(self):
        """
        Executes the Greedy Scheduling Algorithm.
        """
        current_time = 0
        
        while self.task_queue:
            # Pop the task with the highest priority
            priority, deadline, neg_profit, task = heapq.heappop(self.task_queue)
            
            # Greedy Choice: If we can finish it before the deadline, do it!
            if current_time + task.duration <= task.deadline:
                current_time += task.duration
                self.total_profit += task.profit
                self.completed_tasks.append((task, current_time))
            else:
                # Missed the deadline, skip or drop the task
                self.missed_tasks.append(task)
        
        self.total_time_spent = current_time
