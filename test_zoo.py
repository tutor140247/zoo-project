import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
        self.assertEqual(self.zoo.get_ticket_price(-1), None)
        self.assertEqual(self.zoo.get_ticket_price(12), 50)
        self.assertEqual(self.zoo.get_ticket_price(20), 100)
        self.assertEqual(self.zoo.get_ticket_price(60), 150)
        self.assertEqual(self.zoo.get_ticket_price(61), 100)
    
    def test_child2_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)

    def test_child3_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)
    # Add your additional test cases here.

if __name__ == '__main__':
    unittest.main()