
import csv
import os

class VideoStore:
    
    def __init__(self, id, title, rating, copies_available):
        self.inventory = []
        self.video_id = id
        self.video_title = title
        self.rating = rating
        self.copies_available = copies_available

    def reading(self):
        store_inventory = []
        with open('data/inventory.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                store_inventory.append(**row)
        self.inventory = store_inventory
        return store_inventory
    
    @classmethod
    def video_list(cls):
        cls.inventory = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/inventory.csv")
        with open(path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls.inventory.append(VideoStore(**dict(row)))
        return cls.inventory

    def __str__(self):
        # for video in VideoStore.video_list():
        #     print(VideoStore.video_list())
        return self.inventory #f"{video['id']}, {video['title']}, {video['rating']}, {video['copies_available']}"

    def view_inventory(self):
        for video in self.inventory:
            return f"{video['id']}, {video['title']}, {video['rating']}, {video['copies_available']}"
                