import unittest
from classes.interface import Interface
from classes.interface import Store
from classes.interface import Customers


class AssesmentTestCase(unittest.TestCase):
    """Tests for interface.py"""
    """Most of the test cases will not pass after the first trial, because csv files would have been modified"""

    def test_view_video_inventory(self):
        '''Should print a list of the inventory'''
        output_1 = [{'id': '1', 'title': 'Guardians of the Galaxy', 'rating': 'PG-13', 'copies_available': 4}, {'id': '2', 'title': 'Prometheus', 'rating': 'R', 'copies_available': -14}, {'id': '3', 'title': 'Split', 'rating': 'PG-13', 'copies_available': 2}, {'id': '4', 'title': 'Sing', 'rating': 'PG', 'copies_available': 10}, {'id': '5', 'title': 'La La Land', 'rating': 'PG-13', 'copies_available': 0}, {'id': '6', 'title': 'WALL-E', 'rating': 'G', 'copies_available': 3}, {'id': '7', 'title': 'The Prestige', 'rating': 'PG-13', 'copies_available': 1}, {'id': '8', 'title': 'The Dark Knight', 'rating': 'PG-13', 'copies_available': 5}, {'id': '9', 'title': 'Inception', 'rating': 'PG-13', 'copies_available': 2}, {'id': '10', 'title': 'Interstellar', 'rating': 'PG-13', 'copies_available': -5}]
        self.assertEqual(Interface.read_inventory(), output_1)

    def test_view_customers_list(self):
        '''Should print a list of customers'''
        output_2 = [{'id': '1', 'first_name': 'Jon', 'last_name': 'Young', 'current_video_rentals': 'Guardians Of The Galaxy/La La Land'}, {'id': '2', 'first_name': 'Tom', 'last_name': 'Prete', 'current_video_rentals': 'Prometheus/Split'}, {'id': '3', 'first_name': 'Rod', 'last_name': 'Levy', 'current_video_rentals': 'The Dark Knight/Guardians Of The Galaxy/Split'}, {'id': '4', 'first_name': 'Ankur', 'last_name': 'Shah', 'current_video_rentals': 'The Prestige'}, {'id': '5', 'first_name': 'Chris', 'last_name': 'Howell', 'current_video_rentals': 'Sing'}, {'id': '6', 'first_name': 'Matt', 'last_name': 'Jake', 'current_video_rentals': 'Guardians of the Galaxy'}, {'id': '7', 'first_name': 'Musa', 'last_name': 'Sho', 'current_video_rentals': ''}, {'id': '8', 'first_name': 'Nate', 'last_name': 'Juan', 'current_video_rentals': 'Split'}]
        self.assertEqual(Interface.read_customers(), output_2)

    def test_create_new_acct(self):
        '''Should create an acct for a new customer'''
        self.customers = Interface.read_customers()
        new_acct = {'id': 14, 'first_name': 'Jamal', 'last_name': 'Lawrence', 'current_video_rentals': ''}
        output_3 = "Thanks! Your account has been successfully created."
        self.assertEqual(Customers.create_acct(self, new_acct), output_3)
    
    def test_rent_video(self):
        '''Should rent a video'''
        self.customers = Interface.read_customers()
        self.inventory = Interface.read_inventory()
        output_4 = "Thanks for renting with us! Come back soon."
        self.assertEqual(Store.check_cust_video(self, 4, 'Sing'), output_4)
    
    def test_return_video(self):
        '''Should return a video'''
        self.customers = Interface.read_customers()
        self.inventory = Interface.read_inventory()
        output_5 = "Thanks for turning in your video! Come back soon."
        self.assertEqual(Store.customer_return(self, 5, "The Dark Knight"), output_5)


if __name__ == '__main__':
    unittest.main()

'''
# This can be pasted in csv files to retest

id,title,rating,copies_available
1,Guardians of the Galaxy,PG-13,4
2,Prometheus,R,-14
3,Split,PG-13,2
4,Sing,PG,10
5,La La Land,PG-13,0
6,WALL-E,G,3
7,The Prestige,PG-13,1
8,The Dark Knight,PG-13,4
9,Inception,PG-13,2
10,Interstellar,PG-13,-5

id,first_name,last_name,current_video_rentals
1,Jon,Young,Guardians Of The Galaxy/La La Land
2,Tom,Prete,Prometheus/Split
3,Rod,Levy,The Dark Knight/Guardians Of The Galaxy/Split
4,Ankur,Shah,The Prestige
5,Chris,Howell,Sing/The Dark Knight
6,Matt,Jake,Guardians of the Galaxy
7,Musa,Sho,
8,Nate,Juan,Split

'''