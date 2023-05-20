from task import Task, PERIODIC, APERIODIC, SPORADIC, INTERRUPT
from numpy import *                 
import math
class TaskSet:
    """Task Set Class
    
    Attributes:
        tasks (list): List of Task objects
        utility (float): Utility of the task set
        self.feasible (bool): Whether the task set is feasible
    """
    def __init__(self, tasks=[]):
        
        self.tasks = tasks
        self.base_task_set = array(tasks).copy()
        self.utility = 0
        self.feasible = False
        
    def get_base_task_set(self):
        return self.base_task_set
    
    def set_base_task_set(self, task_set):
        self.base_task_set = task_set
        
    def append_task(self, task_list):
        self.tasks += task_list
        
    def add_task(self, task):
        """Add a task to the task set
        
        Args:
            task (Task): Task object to add
        """
        self.tasks.append(task)
        
    def remove_task(self, task):
        """Remove a task from the task set
        
        Args:
            task (Task): Task object to remove
        """
        self.tasks.remove(task)
        
    def get_task_by_name(self, name) -> Task:
        """Get a task from the task set by name
        
        Args:
            name (str): Name of the task to get
        
        Returns:
            Task: The task object with the given name, or None if not found
        """
        for task in self.tasks:
            if task.name == name:
                return task
        return None
    
    def get_all_tasks(self) -> list:
        """Get a list of all tasks in the task set
        
        Returns:
            list: List of all Task objects in the task set
        """
        return self.tasks
    def set_feasiblity(self):
        """Set the feasibility of the task set
        
        Args:
            feasible (bool): Whether the task set is feasible
        """
        # check task set is feasible by comparing all tasks completion_time to their deadline and return boolean. if completion time is none therefor task is not done yet
        for task in self.tasks:
            if task.completion_time is None or task.completion_time > task.deadline:
                self.feasible = False
                return
        self.feasible = True
    
    def calc_utility(self):
        """Set the utility of the task set
        
        Args:
            utility (float): Utility of the task set
        """
        # calculate the utility of task set, sum of ratio of wcet to period
        utility = 0
        for task in self.base_task_set:
            # calculate the utilization for tasks with type=Periodic
            if task.type == PERIODIC or task.type == SPORADIC or task.type == INTERRUPT:
                utility += task.wcet / task.period
            # calculate the utilization for tasks with type=Aperiodic
            elif task.type == APERIODIC:
                utility += task.wcet / task.deadline           
            
        self.utility = utility


    def get_hyper_period(self):
        num1 = self.tasks[0].period
        num2 = self.tasks[1].period
        lcm = self.lcm(num1, num2)
        
        for i in range(2, len(self.tasks)):
            period = self.tasks[i].period
            if period > 0:
                lcm = self.lcm(lcm, period)
        return lcm
    
    def lcm(self, a, b):
        return abs(a*b) // math.gcd(a, b)
    
    def is_feasible(self):
        return self.feasible
    def get_utility(self):
        return self.utility