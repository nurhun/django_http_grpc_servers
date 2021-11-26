# from locust import HttpLocust, TaskSet, task, HttpUser

import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    # wait_time = between(1, 2)

    @task
    def home(self):
        self.client.get("/crud/")

# class WebsiteUser(HttpUser):
#     """
#     User class that does requests to the locust web server running on localhost
#     """

#     host = "http://127.0.0.1:8000/crud"
#     wait_time = between(2, 5)
#     tasks = [QuickstartUser]

    # for i in range(4):
    #     @task(2)
    #     def first_page(self):
    #         self.client.get('/list_page/')



    # @task(3)
    # def get_second_page(self):
    #     self.client.('/create_page/', {'name': 'first_obj'}, headers={'X-CSRFToken': csrftoken})


    # @task(4)
    # def add_advertiser_api(self):
    #     auth_response = self.client.post('/auth/login/', {'username': 'suser', 'password': 'asdf1234'})
    #     auth_token = json.loads(auth_response.text)['token']
    #     jwt_auth_token = 'jwt '+auth_token
    #     now = datetime.datetime.now()

    #     current_datetime_string = now.strftime("%B %d, %Y")
    #     adv_name = 'locust_adv' 
    #     data = {'name', current_datetime_string}
    #     adv_api_response = requests.post('http://127.0.0.1:8000/api/advertiser/', data, headers={'Authorization': jwt_auth_token})



    # class ApplicationUser(HttpLocust):
    #     task_set = UserActions
    #     min_wait = 0
    #     max_wait = 0