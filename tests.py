import unittest
import unittest
from modules.labyrinth import Labyrinth
from test_files.labyrinths import *

class TestLabyrinth(unittest.TestCase):

    def test_first_example(self):
        self.assertEqual(Labyrinth(first_labyrinth).simple_a_star(), 11, "Should be 11")

    def test_second_example(self):
        self.assertEqual(Labyrinth(second_labyrinth).simple_a_star(), -1, "Should be -1")

    def test_third_example(self):
        self.assertEqual(Labyrinth(third_labyrinth).simple_a_star(), 2, "Should be 2")

    def test_fourth_example(self):
        self.assertEqual(Labyrinth(fourth_labyrinth).simple_a_star(), 16, "Should be 16")


unittest.main()
