import os
from src.task import Task
from src.scheduler import TaskScheduler
from src.utils import generate_report, print_schedule, load_tasks_from_csv

def main():
    print("========================================")
    print("  TASK SCHEDULER OPTIMIZATION SYSTEM")
    print("========================================")
    
    # 1. Load tasks from CSV dataset
    tasks = load_tasks_from_csv('data/tasks.csv')
    
    if not tasks:
        print("[!] No data/tasks.csv found or file is empty.")
        print("[!] Using default sample tasks...")
        tasks = [
            Task(1, "Deploy to Prod", priority=1, deadline=3, duration=1, profit=150),
            Task(2, "Fix Login Bug", priority=1, deadline=5, duration=2, profit=100),
            Task(3, "Code Review", priority=2, deadline=6, duration=2, profit=50),
            Task(4, "Update DB Schema", priority=2, deadline=10, duration=4, profit=80),
            Task(5, "Write Documentation", priority=3, deadline=15, duration=3, profit=30)
        ]

    scheduler = TaskScheduler()
    
    for t in tasks:
        scheduler.add_task(t)
        
    print(f"\n[+] Loaded {len(tasks)} tasks into Priority Queue.")
    print("[+] Sorting by Priority -> Deadline -> Profit...")
    
    # 2. Run Algorithm
    print("[+] Running Greedy Scheduling Algorithm...")
    scheduler.run_schedule()
    
    # 3. Output results
    print_schedule(scheduler)
    
    # 4. Generate Report
    report_path = 'outputs/schedule_report.txt'
    generate_report(scheduler, report_path)
    print(f"[+] Detailed performance report saved to: {report_path}")

if __name__ == "__main__":
    main()
