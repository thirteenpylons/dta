"""
self.failed_attempts = 0
loop a req to submit task:
    if self.failed_attempts < 3:
        analyze response:
            yes:
                loop down()
                request_task()
            no:
                abort task()
            anything else:
                increment_failed()
    else:
        return None

"""
from ..choice import Task


def test_task_loop_valid_response(monkeypatch):
    task = Task()
    assert task is not None
    assert task.send == False
    monkeypatch.setattr("builtins.input", lambda _: "y")
    pass_task = task.request_task()
    assert task.send == True
    assert task.t == None
def test_task_loop_pass_negative_valid_response():
    pass
def test_task_loop_invalid_response():
    pass
