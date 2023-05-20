
from task import * 
from Scheduler import Scheduler

class DMScheduler(Scheduler):
    def get_ready_tasks(self, curr_time):
        """Get a list of all ready tasks in the task set
        
        Returns:
            list: List of all Task objects in the task set that are in the READY state
        """
        ready_tasks = []
        for task in self.task_set.get_all_tasks():
            if (task.state == READY or task.state == RUNNING) and task.act_time <= curr_time:
                ready_tasks.append(task)
        return ready_tasks
    
    def get_highest_priority_task(self, curr_time):
        # check if EDF is not preemptive, pick the task from task_set which has state=RUNNING.
        if not self.is_preemptive:
            running_tasks = self.get_running_tasks()
            if running_tasks:
                return running_tasks[0]
        
        ready_tasks = self.get_ready_tasks(curr_time=curr_time)
        if not ready_tasks:
            return None
        # check for interrupts
        interrupt_tasks = [task for task in ready_tasks if task.type == INTERRUPT]
        highest_priority_tasks = []
        if interrupt_tasks:
            ready_tasks = interrupt_tasks
            highest_priority = min([task.priority for task in ready_tasks])
            highest_priority_tasks = [task for task in ready_tasks if task.priority == highest_priority]
        else:
            highest_priority = min([task.relative_deadline for task in ready_tasks])
            highest_priority_tasks = [task for task in ready_tasks if task.relative_deadline == highest_priority]
        return highest_priority_tasks[0]

    
    def schedule(self, curr_time=0):
        """Schedule the next task to run
        
        Returns:
            Task: The next task to run, or None if no tasks are ready
        """
        # schedule deadline monotonic scheduler based on highest priority
        highest_priority_task = self.get_highest_priority_task(curr_time)
        if not highest_priority_task:
            return None
        # decrease remaining time by 1
        highest_priority_task.remaining_time -= 1
        if highest_priority_task.remaining_time == 0:
            highest_priority_task.state = COMPLETED
            highest_priority_task.completion_time = curr_time + 1
        else:
            highest_priority_task.state = RUNNING