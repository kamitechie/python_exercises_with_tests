import unittest
import main
import datetime


class TestMain(unittest.TestCase):
    # 4 exercise tests
    def test_exercise_circle_area(self):
        test_param = 6
        self.assertEqual(main.exercise_circle_area(test_param), 113.09733552923255)

    def test_exercise_circle_area_negative(self):
        test_param = -1
        with self.assertRaises(ValueError):
            main.exercise_circle_area(test_param)

    def test_exercise_circle_area_none(self):
        test_param = None
        with self.assertRaises(TypeError):
            main.exercise_circle_area(test_param)



if __name__ == '__main__':
    unittest.main()