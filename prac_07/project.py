class Project:
    def __init__(self, name='', start_date='', priority=0, cost_estimate=0.0, completion_percentage=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost_estimate
        self.completed_percentage = completion_percentage

    def __str__(self):
        start_date = self.start_date.strftime("%d/%m/%Y")
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: {self.cost_estimate}, " \
               f"completion: {self.completion_percentage}%"

    def __repr__(self):
        return str(self)

    def __lt__(self, other):
        return self.priority < other.priority

    def completed_project(self):
        return self.completion_percentage == 100