import abc
from task import COMPLETED, RUNNING, READY, PERIODIC, Task

class Scheduler(abc.ABC):
    def __init__(self, task_set, is_preemptive=True):
        """Scheduler Class
        
        Attributes:
            task_set (TaskSet): Task set to be scheduled
        """
        self.task_set = task_set
        self.completed_tasks = []
        self.is_preemptive = is_preemptive

    def get_completed_tasks(self):
        return [task for task in self.task_set.get_all_tasks() if task.state == COMPLETED]
    
    def get_running_tasks(self):
        return [task for task in self.task_set.get_all_tasks() if task.state == RUNNING]    
    
    def add_task(self, curr_time):
        """Add the task to the scheduler
        
        Args:
            curr_time (int): Current time of scheduler
        """
        task_set = self.task_set.get_base_task_set()
        tasks_to_add = []
        for task in task_set:
            if task.type == PERIODIC and curr_time % task.period == 0:
                newTask = Task(
                    priority=task.priority,
                    act_time=curr_time + task.act_time,
                    deadline=curr_time + task.deadline,
                    relative_deadline=task.relative_deadline,
                    name=task.name,
                    period=task.period,
                    state=READY,
                    type=task.type,
                    wcet=task.wcet,
                )
                tasks_to_add.append(newTask)

        self.task_set.append_task(tasks_to_add)

    def schedule(self, curr_time):
        pass

    def set_task_set(self, task_set):
        """Set the task set for the scheduler
        
        Args:
            task_set (TaskSet): The task set to be scheduled
        """
        self.task_set = task_set