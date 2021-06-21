
import csv
import os

class Interface():

    def __init__(self):
        self.customers = Interface.read_customers()
        self.inventory = Interface.read_inventory()

    def home_screen(self):
        
        begin = int(input(f"""\nWelcome to Code Platoon Video!
1. View video inventory
2. View customer's rented videos
3. Rent video
4. Return video
5. Add new customer
6. Exit
"""))
        while True:
            if begin == 1:
                self.view_inventory()
                break
            elif begin == 2:
                id = int(input("Please, enter your customer id "))
                customer_id = self.view_customer_videos(id)
                return customer_id
            elif begin == 3:
                rent_id = int(input("Please, enter your customer id "))
                title = str(input("Please, enter the title of the video "))
                rent_id = int(rent_id)
                Store.rent_video(self, rent_id, title)
                Store.check_cust_video(self, rent_id, title)
                break
            elif begin == 4:
                id = int(input("Please, enter your customer id "))
                title = str(input("Please, enter the title of the video "))
                Store.return_video(self, id, title)
                break
            elif begin == 5:
                new_acct = {'current_video_rentals': ''}
                new_acct['id'] = int(input("Enter your new id "))
                new_acct['first_name'] = str(input("Enter your first name "))
                new_acct['last_name'] = str(input("Enter your last name "))
                Customers.create_acct(self, new_acct)
                Customers.add_acct(self, new_acct)
                break
            elif begin == 6:
                break
    # read and extract all the information from the inventory cvs file
    @classmethod
    def read_inventory(cls):
        store_inventory = []
        with open('data/inventory.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                store_inventory.append({'id': row['id'], 'title': row['title'], 'rating': row['rating'], 'copies_available': int(row['copies_available'])})

        return store_inventory
    
    # read and extract all the information from the customers cvs file
    @classmethod
    def read_customers(cls):
        store_customers = []
        with open('data/customers.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                store_customers.append({'id': row['id'], 'first_name': row['first_name'],'last_name': row['last_name'],'current_video_rentals': row['current_video_rentals']})

        return store_customers
    
    # create a function that prints out a list of all videos in the inventory
    def view_inventory(self):
        for videos in self.inventory:
            print(videos)

    # create a function to prints out all the videos that have been checked out by the customer 
    def view_customer_videos(self, id):
        return_message = ''
        for customer in self.customers:
            if str(id) == customer['id']:
                customer_videos = customer['current_video_rentals'].replace('/', ', ') 
                return_message = customer_videos
                break
            else:
                return_message = "You are not a registered customer. Please, create an account"
        print(return_message)

    # write the extracted inventory info back to the cvs file
    def write_inventory(self):
        with open('data/inventory.csv', 'w') as csvfile:
            video_csv = csv.writer(csvfile, delimiter=',')
            video_csv.writerow(['id','title','rating','copies_available'])
            for video in self.inventory:
                video_csv.writerow([video['id'], video['title'], video['rating'], video['copies_available']])
    
    # write the extracted customers info back to the cvs file
    def write_customers(self):
        with open('data/customers.csv', 'w') as csvfile:
            customer_csv = csv.writer(csvfile, delimiter=',')
            customer_csv.writerow(['id','first_name','last_name','current_video_rentals'])
            for customer in self.customers:
                customer_csv.writerow([customer['id'], customer['first_name'], customer['last_name'], customer['current_video_rentals']])
            
# create a Store class function
class Store(Interface):

    def __init__(self,id,title,rating,copies_available):
        super().__init__(id,title,rating,copies_available)
        self.id = id
        self.title = title
        self.rating = rating
        self.copies_available = copies_available
        self.customers = Interface.read_customers()
        self.inventory = Interface.read_inventory()

# create a function that check customer's data to see if the customer has checked out 3 videos or less
    # the fuction should also check if the video the customer is requesting to check is available in the inventory
    def check_cust_video(self, id, title):
        # create a key/value variable that counts the amount a each video available
        videos_count = {}
        # create a variable that count number of videos that has been checked out by the customer
        customer_count = {}

        self.message = ""

        # check the inventory and make sure the number of the video in-stock is greater than 0,
        # and that the customer has checked out less than 3 video
            # if this is true, checkout the video as requested and return a message
        # else, return a message that the customer cannot checkout the video
        for videos in self.inventory:
            videos_count[videos['title']] = int(videos['copies_available'])
            videos['copies_available'] = int(videos['copies_available'])
            videos['id'] = int(videos['id'])
            for customer in self.customers:
                customer['id'] = int(customer['id'])
                customer_videos = customer['current_video_rentals'].split('/')
                if customer_videos == ['']:
                    customer_videos = []
                    customer_count[customer['id']] = 0
                else:
                    customer_count[customer['id']] = int(len(customer_videos))
        for each_customer in customer_count:
            for each_video in videos_count:
                for customer in self.customers:
                    if int(id) != int(customer['id']):
                        self.message = "You are not a registered customer!. Please, enter '5' to register for an account."
                    elif videos_count[title] < 1:
                        self.message = f"Sorry, we are out of {title}. Please, enter a different title."
                        break
                    elif customer_count[id] >= 3:
                        self.message = "Sorry, you have reached your maximum checkout limit. Please, return some of your  videos to checkout more."
                        break
                    elif customer['id'] == int(id) and customer_count[id] < 3:
                        self.message = "Thanks for renting with us! Come back soon."
                        break
        

        return self.message

    # create a function that check the message that was returned in the previous function and modify the inventory if needed
    def rent_video(self, id, title):

        # make sure the message that was returned in the previous function allows the customer to checkout the video
            # then change the number of that video in-stock to reflect the video that was checked out
        # if not, return to homescreen
        print(Store.check_cust_video(self, id, title))
        for videos in self.inventory:
            for customer in self.customers:
                if Store.check_cust_video(self, id, title) == "Thanks for renting with us! Come back soon.":
                    if videos['title'] == title and customer['id'] == id:
                        if customer['current_video_rentals'] == '':
                            customer['current_video_rentals'] = title
                            videos['copies_available'] = videos['copies_available'] - 1
                        else:
                            customer['current_video_rentals'] = customer['current_video_rentals'] + '/' + title
                            videos['copies_available'] = videos['copies_available'] - 1
                else:
                    Interface.home_screen(self)
        
        Interface.write_inventory(self)
        Interface.write_customers(self)
    
    # create a function that check if a customer's information is on file and if the videos the customer is trying to return is listed in the inventory.
    def customer_return(self, id, title):
        
        return_message = "You are not a registered customer or video title is incorrect!. Please, enter '5' to register for an account or enter a correct video title."
        # if the customer is registered and the video is in inventory, return a message that the return was succesful, and modify the inventory and customer record
        # else return that the customer cannot return the video
        for videos in self.inventory:
            for customer in self.customers:
                
                if videos['title'] == title and customer['id'] == str(id):
                    if customer['current_video_rentals'] == title:
                        customer['current_video_rentals'] = ''
                        videos['copies_available'] = videos['copies_available'] + 1
                        return_message = "Thanks for turning in your video! Come back soon."
                        break
                    else:
                        videos_arr = customer['current_video_rentals'].split('/')
                        videos_arr.remove(title)
                        customer['current_video_rentals'] = '/'.join(videos_arr)
                        videos['copies_available'] = videos['copies_available'] + 1
                        return_message = "Thanks for turning in your video! Come back soon."    

        Interface.write_inventory(self)
        Interface.write_customers(self)
        return return_message
    
    # create a function that prints out the return message
        # this is necessary to be able to connect the function to the spec file. The spec file only reads fuction a return statement
    def return_video(self, id, title):
        return_message = Store.customer_return(self, id, title)
        print(return_message)
        if return_message != "Thanks for turning in your video! Come back soon.":
            Interface.home_screen(self)
        

# create a customers class function
class Customers(Interface):

    def __init__(self):
        super().__init__()
        self.customers = Interface.read_customers()
    
    # create a fuction that create accounts for new customers
    def create_acct(self, new_acct):
        ids = []
        new_id = new_acct['id']
        self.output = ''
        for each_acct in self.customers:
            ids.append(int(each_acct['id']))

        # check to make sure that the id chosen by the customer is not already taken
            # if it is, tell the customer to choose a different id
        # else, create the customer's account, and return a succes message
        for i, id in enumerate(ids):
            if new_id == ids[i]:
                self.output = "The id you entered is already taken. Please, try a different id."
                break
            elif new_id != ids[i]:
                self.output = "Thanks! Your account has been successfully created."   
            else:
                continue

        return self.output

    def add_acct(self, new_acct):
        
        # print the message returned from the previous function
        # if the previous function returns a success message, save the customer's info to the csv file
        print(Customers.create_acct(self, new_acct))
        if Customers.create_acct(self, new_acct) == "Thanks! Your account has been successfully created.":
            self.customers.append(new_acct)
            Interface.write_customers(self)
            
        
          
        

        