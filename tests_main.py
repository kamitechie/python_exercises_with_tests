import unittest
import main
import datetime


class TestMain(unittest.TestCase):
    def test_exercise_circle_area(self):
        test_param = 6
        self.assertEqual(main.exercise_date_time(test_param), 113.09733552923255)



if __name__ == '__main__':
    unittest.main()