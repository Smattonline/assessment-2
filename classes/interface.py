import csv
import os

class Interface():

    def __init__(self):
        pass

    def variables(self):
        self.customers = []
        self.inventory = Interface.reading()

    def home_screen(self):
        
        begin = int(input(f"""\nWelcome to Code Platoon Video!
    1. View video inventory
    2. View customer's rented videos
    3. Rent video
    4. Return video
    5. Add new customer
    6. Exit
    \n"""))
        while True:
            if begin == 1:
                self.view_inventory()
                break
            elif begin == 2:
                self.view_all_customers()
                break
            elif begin == 3:
                pass
            elif begin == 4:
                pass
            elif begin == 5:
                pass
            elif begin == 6:
                break
    
    @classmethod
    def reading(cls):
        store_inventory = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/inventory.csv")
        with open(path,'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                new_row = Interface(**dict(row))
                # store_inventory.append(new_row)
                store_inventory.append({'id': new_row.id, 'title': new_row.title, 'rating': new_row.rating, 'copies_available': new_row.copies_available})
        return store_inventory
    
    def view_inventory(self):
        # print(self.inventory)
        # print(Interface.reading(self))
        for videos in self.inventory:
            return videos