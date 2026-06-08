class RobotScheduler:
    def __init__(self):
        self.robots={}
        self.tasks=[]

    def register_robot(self,robot_id,capacity):
        if robot_id in self.robots:
            raise ValueError(f"Robot {robot_id} already exists.")
        # Check if the robot ID already exists in the registry.
        # If it does, raise an error to prevent duplicate registration.
        self.robots[robot_id]={"capacity":capacity,"status":"idle"}
         # Otherwise, create a new robot entry with:
         # - capacity: the robot's capability value
         # - status: initialized as "idle", meaning the robot is currently free
    

    def assign_task(self,robot_id,task):
    # Check whether the robot exists in the registry.
    # If not, raise an error because the robot_id is invalid.

        if robot_id not in self.robots:
            raise KeyError("robot_id not found.")
        
    # If the robot is not idle, it is currently busy and cannot take a new task.
    # Return False to indicate that assignment failed.

        if self.robots[robot_id]["status"]!="idle":
            return False
    # Mark the robot as busy because a new task is now assigned.
    #     
        self.robots[robot_id]["status"]="busy"
        self.tasks.append({"robot":robot_id,"task":task})

    # Return True to indicate the task was successfully assigned.
        return True
        
    def complete_task(self,robot_id):
    # Check whether the robot exists in the registry.
    # If it does not exist, raise an error because the ID is invalid.
        if robot_id not in self.robots:
            raise KeyError("Robot not found.")
        self.robots[robot_id]["status"]="idle"

    def get_status(self,robot_id):
        return self.robots.get(robot_id)
    
