# Task Scheduler Optimization System 🚀

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Data Structures](https://img.shields.io/badge/Data_Structures-Priority_Queue-green)
![Algorithm](https://img.shields.io/badge/Algorithm-Greedy-orange)

## 📌 Project Overview
The **Task Scheduler Optimization System** is an industry-oriented project demonstrating advanced Data Structures & Algorithms (DSA). It simulates a real-world CPU/Task scheduler that manages tasks with varying priorities, deadlines, execution times, and profit/importance scores.

## 🎯 Problem Statement
In computing systems and human workflows, thousands of tasks compete for time. A naive first-come-first-serve approach leads to missed deadlines and low efficiency. The problem is to **maximize total profit/importance** and **minimize missed deadlines** by scheduling tasks in the most optimized order.

## 🧠 DSA Concepts Used
- **Priority Queue (Min-Heap):** Used to continuously fetch the highest priority task in `O(log N)` time.
- **Sorting:** Multi-level sorting (Priority -> Deadline -> Profit).
- **Greedy Algorithm:** At any given time, the system greedily chooses the most important valid task to maximize local profit and stay within deadlines.

## 📂 Folder Structure
```
Task-Scheduler-Optimization-System/
│
├── data/                  # CSV datasets containing input tasks
├── src/                   # Core application logic
│   ├── task.py            # Task data structure
│   ├── scheduler.py       # Priority Queue & Greedy algorithm logic
│   └── utils.py           # IO operations and report generation
├── outputs/               # Auto-generated execution reports
├── main.py                # Application entry point
├── README.md              # Project Documentation
└── requirements.txt       # Dependencies (Standard Library)
```

## ⚙️ How to Run
1. Clone the repository.
2. Ensure you have Python 3 installed.
3. Open a terminal and run:
   ```bash
   python main.py
   ```

## 📊 Sample Output
```
 🚀 OPTIMIZED TASK EXECUTION SCHEDULE
=======================================================

✅ COMPLETED TASKS (6):
Task Name            | Start  | End    | Profit  
-------------------------------------------------------
Deploy to Prod       | 0      | 1      | 150     
Fix Login Bug        | 1      | 3      | 100     
Code Review          | 3      | 5      | 50      
Client Meeting       | 5      | 7      | 90      
Server Maintenance   | 7      | 10     | 120     
Write Documentation  | 10     | 13     | 30      

❌ MISSED DEADLINES (2):
- Update DB Schema (Deadline: 10, Duration: 4)
- Refactor Legacy Code (Deadline: 20, Duration: 5)
```

## 🎓 Learning Outcomes
- Real-world application of Heaps and Priority Queues.
- Understanding trade-offs in Greedy optimization.
- Building modular, clean Python architectures.
