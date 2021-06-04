#Business layer for CIS3145 by James Porter

#creates task with three public attributes
class Task:
    def __init__(self, taskID, description, completed):
        self.taskID = taskID
        self.description = description
        self.completed = completed
#override the __str__ method and return the description and the output '(DONE!)'
    def __str__(self):
        return str(self.description) + '\n'

