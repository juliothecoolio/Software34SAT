# data_layer.py
# Author: Julian Jurista
# Date created: 20/07/2026

from datetime import datetime

tasks = []
filename = "tasks.csv"

class Task():
    def __init__(self):
        self.title = ""
        self.difficulity = ""
        self.due_date = ""
        self.estimated_completion_time = ""

# def load_data():
    # load from filename and builds the tasks array of Task objects

# def save_data():
    # overwrites filename with Tasks in the tasks array

# # Get current local date and time
# now = datetime.now()

# print("Full timestamp:", now)
# print("Current year:", now.year)
# print("Current hour:", now.hour)