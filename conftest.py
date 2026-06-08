import pytest
from robot_scheduler import RobotScheduler

@pytest.fixture
def scheduler():
    s=RobotScheduler()
    s.register_robot("R001",capacity=10)
    return s
#for testing the register_robot method
