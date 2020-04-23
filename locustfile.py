from locust import HttpLocust, TaskSet, task, between, events

class UserBehaviour(TaskSet):
    @task
    def home(self):
        self.client.get("/fr/")

    @task
    def news(self):
        self.client.get("/fr/news.php")

    @task
    def history(self):
        self.client.get("/fr/page/en-savoir-plus/notre-histoire.php")

    @task
    def contacts(self):
        self.client.get("/fr/contact.php")

    @task
    def generalPresentation(self):
        self.client.get("/fr/page/projets-de-modernisation-cles-en-main/presentation-generale.php")
        
class WebsiteUser(HttpLocust):
    task_set = UserBehaviour 
    wait_time = between(1, 3) # Between 1 and 3 seconds between each task
