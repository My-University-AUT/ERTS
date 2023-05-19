from task import * 
class EDFScheduler:
    """Scheduler Class
    
    Attributes:
        task_set (TaskSet): Task set to be scheduled
    """
    def __init__(self, task_set):
        self.task_set = task_set
        self.completed_tasks = []
        
    def get_ready_tasks(self, curr_time):
        """Get a list of all ready tasks in the task set
        
        Returns:
            list: List of all Task objects in the task set that are in the READY state
        """
        ready_tasks = []
        for task in self.task_set.get_all_tasks():
            if task.state == READY and task.act_time <= curr_time:
                ready_tasks.append(task)
        return ready_tasks
    
    def get_highest_priority_task(self, curr_time):
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
            highest_priority = min([task.deadline for task in ready_tasks])
            highest_priority_tasks = [task for task in ready_tasks if task.deadline == highest_priority]

        return highest_priority_tasks[0]

    
    def schedule(self, curr_time=0):
        """Schedule the next task to run
        
        Returns:
            Task: The next task to run, or None if no tasks are ready
        """
        
        highest_priority_task = self.get_highest_priority_task(curr_time)
        if not highest_priority_task:
            return None
        
        highest_priority_task.remaining_time -= 1
        if highest_priority_task.remaining_time == 0:
            highest_priority_task.state = COMPLETED
            highest_priority_task.completion_time = curr_time + 1
       
        return highest_priority_task
    def set_task_set(self, task_set):
        """Set the task set for the scheduler
        
        Args:
            task_set (TaskSet): The task set to be scheduled
        """
        self.task_set = task_set

    def add_task(self, curr_time):
        # return
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
                    name=task.name,
                    period=task.period,
                    state=READY,
                    type=task.type,
                    wcet=task.wcet,
                )
                tasks_to_add.append(newTask)

        self.task_set.append_task(tasks_to_add)


    def get_completed_tasks(self):
        return [task for task in self.task_set.get_all_tasks() if task.state == COMPLETED]
    
