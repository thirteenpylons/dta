from ..task import Task, Network


task = Task()

def test_init():
    assert task.failed_attempts == 0
    assert task.loop_up == False
    assert task.online == False

def test_request_loop_positive(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "y")
    send = task.request_loop()
    
    test_init()

def test_request_loop_negative(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "n")
    send = task.request_loop()
    
    test_init()

def test_task_online():
    net_task = Task(online=True)
    assert net_task.online == True

def test_Network():
    n = Network()
    assert n.is_connected == True, "Must be connected to the internet, check network coonection."

