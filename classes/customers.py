

from classes.store import VideoStore


class Customers:

    def __init__(self, customer_id, first_name, last_name, rentals_by_title):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.rentals_by_title = rentals_by_title
        self.customers_data = []
        self.inventory = VideoStore.video_list()

    def view_inventory(self):
        self.name = ''
        for video in self.inventory:
            print(VideoStore.video_list())
            return f"{video['video_id']}, {video['video_title']}, {video['rating']}, {video['copies_available']}"

   
