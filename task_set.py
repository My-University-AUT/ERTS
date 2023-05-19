from task import Task
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
    def set_feasible(self, feasible):
        """Set the feasibility of the task set
        
        Args:
            feasible (bool): Whether the task set is feasible
        """
        self.feasible = feasible
    def set_utility(self, utility):
        """Set the utility of the task set
        
        Args:
            utility (float): Utility of the task set
        """
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