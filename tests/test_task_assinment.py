import pytest

def test_assign_task_success(scheduler):
    result=scheduler.assign_task("R001","pick_item_A")
    assert result==True
    assert scheduler.get_status("R001")["status"]=="busy"

def test_assign_task_to_busy_robot(scheduler):
    scheduler.assign_task("R001","pick_item_A")
    result=scheduler.assign_task("R001","pick_item_B")
    assert result==False

def test_assign_task_robot_not_found(scheduler):
    with pytest.raises(KeyError):
        scheduler.assign_task("R999","pick_item_X")

def test_complete_task_restores_idle(scheduler):
    scheduler.assign_task("R001","pick_item_A")
    scheduler.complete_task("R001")
    assert scheduler.get_status("R001")["status"]=="idle"


