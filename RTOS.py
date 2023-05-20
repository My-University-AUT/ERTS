from printer import TaskSetPrinter as Printer
from EDFschedular import EDFScheduler
from DMScheduler import DMScheduler
class RTOS:
    """Real-Time Operating System Class"""
    def __init__(self, task_set=None, scheduler_type="EDF", is_preemptive=True):
        """Initialize the RTOS instance
        
        Args:
            task_set (TaskSet): The task set to run on the operating system
        """
        self.task_set = task_set
        if scheduler_type == "EDF":
            self.scheduler = EDFScheduler(task_set, is_preemptive)
        elif scheduler_type == "DM":
            self.scheduler = DMScheduler(task_set)
        
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

        self.scheduler.task_set.set_feasiblity()
        # self.scheduler.task_set.calc_utility()


        self.printer.print_schedule(self.scheduler)
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