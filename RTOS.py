from printer import TaskSetPrinter as Printer
from EDFschedular import EDFScheduler
from task import RUNNING
class RTOS:
    """Real-Time Operating System Class"""
    def __init__(self, task_set=None):
        """Initialize the RTOs instance
        
        Args:
            task_set (TaskSet): The task set to run on the operating system
        """
        self.task_set = task_set
        self.scheduler = EDFScheduler(task_set)
        self.printer = Printer()

    def run(self, duration):
        """Run the task set on the operating system for a specified duration
        
        Args:
            duration (int): The duration to run the task set for
        
        Returns:
            List of Task: The completed task set after running on the operating system for the specified duration
        """
        self.scheduler.schedule()
        for curr_time in range(1, duration):
            self.scheduler.add_task(curr_time=curr_time)
            self.scheduler.schedule(curr_time=curr_time)

        # completed_tasks = self.scheduler.get_completed_tasks()
        # self.printer.print_schedule(completed_tasks)
        all_tasks = self.scheduler.task_set.get_all_tasks()
        self.printer.print_schedule(all_tasks)
        # return completed_tasks
    def set_task_set(self, task_set):
        """Set the task set for the operating system
        
        Args:
            task_set (TaskSet): The task set to run on the operating system
        """
        self.task_set = task_set
        self.scheduler.set_task_set(task_set)
    
    def get_hyper_period(self):
        return self.task_set.get_hyper_period()