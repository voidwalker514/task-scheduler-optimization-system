import csv
import os
from src.task import Task

def load_tasks_from_csv(filepath):
    tasks = []
    if not os.path.exists(filepath):
        return tasks
    try:
        with open(filepath, mode='r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                tasks.append(Task(
                    task_id=int(row['task_id']),
                    name=row['name'],
                    priority=int(row['priority']),
                    deadline=int(row['deadline']),
                    duration=int(row['duration']),
                    profit=int(row['profit'])
                ))
    except Exception as e:
        print(f"Error reading CSV: {e}")
    return tasks

def print_schedule(scheduler):
    print("\n" + "="*55)
    print(" [OPTIMIZED TASK EXECUTION SCHEDULE]")
    print("="*55)
    
    print(f"\n[+] COMPLETED TASKS ({len(scheduler.completed_tasks)}):")
    print(f"{'Task Name':<20} | {'Start':<6} | {'End':<6} | {'Profit':<8}")
    print("-" * 55)
    
    current_time = 0
    for task, end_time in scheduler.completed_tasks:
        start = end_time - task.duration
        print(f"{task.name:<20} | {start:<6} | {end_time:<6} | {task.profit:<8}")
        
    print(f"\n[-] MISSED DEADLINES ({len(scheduler.missed_tasks)}):")
    if not scheduler.missed_tasks:
         print("None! All attempted tasks completed on time.")
    for task in scheduler.missed_tasks:
        print(f"- {task.name} (Deadline: {task.deadline}, Duration: {task.duration})")
        
    print("\n" + "="*55)
    print(" [PERFORMANCE SUMMARY]")
    print("="*55)
    print(f"Total Profit Earned : {scheduler.total_profit}")
    print(f"Total Time Spent    : {scheduler.total_time_spent}")
    total_tasks = len(scheduler.completed_tasks) + len(scheduler.missed_tasks)
    print(f"Tasks Completed     : {len(scheduler.completed_tasks)} / {total_tasks}")
    print("="*55 + "\n")

def generate_report(scheduler, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w') as f:
        f.write("=== TASK SCHEDULING SYSTEM REPORT ===\n\n")
        f.write(f"Total Tasks Evaluated : {len(scheduler.completed_tasks) + len(scheduler.missed_tasks)}\n")
        f.write(f"Tasks Completed       : {len(scheduler.completed_tasks)}\n")
        f.write(f"Missed Deadlines      : {len(scheduler.missed_tasks)}\n")
        f.write(f"Total Profit Earned   : {scheduler.total_profit}\n")
        f.write(f"Total Execution Time  : {scheduler.total_time_spent}\n\n")
        
        f.write("--- SCHEDULED TASKS (EXECUTION TIMELINE) ---\n")
        for task, end_time in scheduler.completed_tasks:
             f.write(f"[{end_time - task.duration} -> {end_time}] : {task.name} (Profit: +{task.profit})\n")
             
        f.write("\n--- MISSED TASKS ---\n")
        for task in scheduler.missed_tasks:
             f.write(f"- {task.name} (Needed {task.duration} time, but deadline was {task.deadline})\n")
