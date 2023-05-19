import csv
from task import Task
from task_set import TaskSet
from RTOS import RTOS
class Main:
    def __init__(self):
        self.rtos = RTOS()
        task_set = self.read_tasks_from_csv('tasks1.csv')
        self.task_set = TaskSet(task_set)
        

    def run(self):
        # schedule tasks using EDF algorithm
        self.rtos.set_task_set(self.task_set)
        # you need to find hyper period and change duration to hyper period
        duration=86
        self.rtos.run(duration)
    def read_tasks_from_csv(self, filename):
        with open(filename, 'r') as csvfile:
            # header in csv file: priority,name,  state, type, act_time, period, wcet, deadline
            taskreader = csv.reader(csvfile, delimiter=',',)
            next(taskreader, None)  # skip the headers
            task_set = []
            for row in taskreader:
                print(row)
                priority,name,  state, type, act_time, period, wcet, deadline = row
                task = Task(
                    priority=int(priority),
                    name=name,
                    state=int(state),
                    type=int(type),
                    act_time=int(act_time),
                    period=int(period),
                    wcet=int(wcet),
                    deadline=int(deadline)
                )
                task_set.append(task)
            return task_set

if __name__ == '__main__':
    main = Main()
    main.run()
