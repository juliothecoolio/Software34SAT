# business_layer.py
# Author: Julian Jurista
# Date created: 20/07/2026

from datetime import datetime
import sys
import os
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QTimeEdit
import data_layer as d

now = datetime.now()
current_task = None

# test task
due_date = datetime(2026, 7, 31, 0, 0)
print(due_date)

d.load_data()

def add_task(title, difficulty, due_date, estimated_completion_time):
    priority = 0.0

    #DUE DATE CALCULATION
    if now.month - due_date.month == 0:
        if now.day - due_date.day == 1:
            priority += 10
        elif now.day - due_date.day == 2:
            priority += 9
        elif now.day - due_date.day == 3:
            priority += 8
        elif now.day - due_date.day == 4:
            priority += 7
        elif now.day - due_date.day == 5:
            priority += 6
        elif now.day - due_date.day == 6:
            priority += 5
        elif now.day - due_date.day >= 7 and now.day - due_date.day < 14:
            priority += 4
        elif now.day - due_date.day >= 14 and now.day - due_date.day < 21:
            priority += 3
        elif now.day - due_date.day >= 21 and now.day - due_date.day < 28:
            priority += 2
        else:
            priority += 1

    # DIFFICULTY CALCULATION 
    if difficulty == "Very Easy":
        priority = priority * 1
    elif difficulty == "Easy":
        priority = priority * 1.25
    elif difficulty == "Moderate":
        priority = priority * 1.5
    elif difficulty == "Difficult":
        priority = priority * 1.75
    elif difficulty == "Very Difficult":
        priority = priority * 2
    elif difficulty == "Extreme":
        priority = priority * 3
    



    # ESTIMATED COMPLETION TIME CALCULATION
    if estimated_completion_time <= 1:
        priority = priority * 1.25
    elif estimated_completion_time < 2 and estimated_completion_time > 1:
        priority = priority * 1.5
    elif estimated_completion_time < 3 and estimated_completion_time > 2:
        priority = priority * 1.75
    elif estimated_completion_time < 4 and estimated_completion_time > 3:
        priority = priority * 2
    elif estimated_completion_time < 5 and estimated_completion_time > 4:
        priority = priority * 2.25
    elif estimated_completion_time < 6 and estimated_completion_time > 5:
        priority = priority * 2.5
    elif estimated_completion_time < 7 and estimated_completion_time > 6:
        priority = priority * 2.75
    elif estimated_completion_time < 8 and estimated_completion_time > 7:
        priority = priority * 3
    elif estimated_completion_time < 9 and estimated_completion_time > 8:
        priority = priority * 3.25
    elif estimated_completion_time < 10 and estimated_completion_time > 9:
        priority = priority * 3.5
    else:
        priority = priority * 4

