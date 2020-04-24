from locust import HttpLocust, TaskSet, task, between
import common
import argparse

LIST_URL_TO_TEST = []

class UserBehaviour(TaskSet):   
    @task
    def setup(self):
        for url in LIST_URL_TO_TEST:                        
            self.schedule_task(self.createTask, args=[url])
   
    #@task
    def createTask(self, url : str):
        self.client.get(url)

        
class WebsiteUser(HttpLocust):
    global LIST_URL_TO_TEST
    
    # Get host
    parser = argparse.ArgumentParser()
    parser.add_argument('-H', '--host')
    args, unknown = parser.parse_known_args()
    webSiteUrl = args.host

    # Get all links for website "webSiteUrl"
    print("Get all links of main URL : '" + webSiteUrl + "'" )
    LIST_URL_TO_TEST = common.getLinksFromURL(webSiteUrl, webSiteUrl, [])

    # Test
    task_set = UserBehaviour
    wait_time = between(1, 3) # Between 1 and 3 seconds between each task

    
