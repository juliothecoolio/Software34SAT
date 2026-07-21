# business_layer.py
# Author: Julian Jurista
# Date created: 20/07/2026
from datetime import datetime
import data_layer as d

now = datetime.now()
current_task = None

# test task
task_date = datetime(2026, 7, 31, 0, 0)
print(task_date)

# d.load_data()

def add_task(title, difficulty, due_date, estimated_completion_time):
    priority = 0.0

    #DUE DATE VALIDATION
    if now.month - task_date.month == 0:
        if now.day - task_date.day == 1:
            priority += 10
        elif now.day - task_date.day == 2:
            priority += 9
        elif now.day - task_date.day == 3:
            priority += 8
        elif now.day - task_date.day == 4:
            priority += 7
        elif now.day - task_date.day == 5:
            priority += 6
        elif now.day - task_date.day == 6:
            priority += 5
        elif now.day - task_date.day >= 7 and now.day - task_date.day < 14:
            priority += 4
        elif now.day - task_date.day >= 14 and now.day - task_date.day < 21:
            priority += 3
        elif now.day - task_date.day >= 21 and now.day - task_date.day < 28:
            priority += 2
        else:
            priority += 1

    # DIFFICULTY VALIDATION 
    if difficulty == "Very Easy":
        priority = priority * 1
    elif difficulty == "Easy":
        priority = priority * 1.5
    elif difficulty == "Moderate":
        priority = priority * 2
    elif difficulty == "Difficult":
        priority = priority * 2.5
    elif difficulty == "Very Difficult":
        priority = priority * 3
    elif difficulty == "Extreme":
        priority = priority * 4
    


