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
class Task:
    def __init__(self):
        self.failed_attempts = 0
        self.loop_up = False

        self.send = False
        self.t = None

    def task_loop(self):
        inquire_task = True
        while inquire_task:
            if self.failed_attempts < 3:
                self.request_task()
            else:
                return None
    

    def request_loop(self):
        self.loop_up = True
        self.request_loop_status()
    
    def request_loop_status(self):
        if self.loop_up:
            self.request_failed_attempts_status()
        else:
            return "Loop is down"
    
    def request_failed_attempts_status(self):
        if self.failed_attempts < 3:
            self.request_task()
        else:
            self.loop_up = False
            self.failed_attempts = 0
            return "Too many failed attempts"

    def request_task(self) -> bool:
        task_response = input("task?: ")
        return self.analyze_response(task_response)

    def analyze_response(self, response: str) -> bool:
        valid_responses = ["yes", "y"]
        self.send = response.lower() in valid_responses

    def increment_failed(self):
        self.failed_attempts += 1

    def execute_task(self):
        self.t = "yeeeee"

    def pass_task(self):
        pass