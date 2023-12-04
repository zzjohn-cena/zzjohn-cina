# tests/performance/basic_performance_test.py

from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def perform_request(self):
        self.client.get("/tasks")
