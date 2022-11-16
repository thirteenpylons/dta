import socket
from enum import Enum

"""
I haven't figured out implementation for this yet...
The idea was to verify data prior to executing a task.

Say I want to send an email:
    I'll need to verify the data prior to sending:
        my_data = "some data to send..."
        !!!!!This will just verify data and network

        use:
            task = Task(data=my_data, online=True)
            task.request_loop()
            if task.execute:
                # method to execute

        task.request_loop()

    and then execute(send_email) if verified

"""


class Task:
    def __init__(self, data=None, online=False):
        self.failed_attempts = 0
        self.loop_up = False
        self.execute = False
        self.online = online
        self.data = data
        if online:
            self.check_network_connection()

    def request_loop(self) -> None:
        self.loop_up = True
        self.request_loop_status()

    def request_loop_status(self) -> None:
        if self.loop_up:
            self.request_failed_attempts_status()
        else:
            print("Loop is down")

    def request_failed_attempts_status(self) -> None:
        if self.failed_attempts < 3:
            if self.data:
                self.verify_data()
            else:
                self.request_task()
        else:
            self.loop_up = False
            self.failed_attempts = 0
            self.Message.exceeded_attempts(3)

    def verify_data(self) -> None:
        print(self.data)

    def request_task(self) -> None:
        # check if data: verify data else: default task request
        task_response = input("task?: ")
        self.analyze_response(task_response)

    def analyze_response(self, response: str) -> None:
        valid_responses = ["yes", "y", "no", "n"]
        clean_response = response.lower()
        if clean_response in valid_responses:
            self.submit_response(clean_response)
        else:
            self.increment_failed()

    def submit_response(self, response: str) -> None:
        if response.startswith("y"):
            self.loop_up = False
            self.execute_task()
        else:
            self.increment_failed(3)

    def execute_task(self) -> None:
        self.execute = True

    def increment_failed(self, amount=1) -> None:
        self.failed_attempts += amount
        self.request_loop_status()

    def check_network_connection(self):
        network = Network()
        return network.is_connected


    class Message(Enum):
        exceeded_attempts = (
            lambda attempts: f'Warning, reached the maximum of {attempts} attempts!'
        )


class Network:
    def __init__(self):
        self.is_connected = self.check_connection()

    def check_connection(self) -> bool:
        try:
            sock = socket.create_connection(("1.1.1.1", 53))
            if sock is not None:
                sock.close()
            return True
        except OSError:
            pass
        return False


class Data:
    """
    Check to see what kind of data is fed:
        str, list, ...
    check_data_type(self):
        if type(data) == str:
            parse_string_data(self)

    """
    def __init__(self, data: str):
        self.data = data
    def verify(self) -> bool:
        pass
