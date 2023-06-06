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

    def test_exercise_circle_area_not_num(self):
        test_param = 'six'
        with self.assertRaises(TypeError):
            main.exercise_circle_area(test_param)

    # 5 exercise tests

    def test_exercise_fullname(self):
        test_param_name = 'Anna'
        test_param_lastname = 'Jo'
        result = main.exercise_reverse_name(test_param_name, test_param_lastname)
        self.assertEqual(result, 'oJ annA')

    def test_exercise_lowercase(self):
        test_param_name = 'WILL'
        test_param_lastname = 'SHO'
        result = main.exercise_reverse_name(test_param_name,test_param_lastname)
        self.assertEqual(result, 'OHS LLIW')

    def test_exercise_uppercase(self):
        test_param_name = 'fo'
        test_param_lastname = 'ally'
        result = main.exercise_reverse_name(test_param_name,test_param_lastname)
        self.assertEqual(result, 'ylla of')

    def test_exercise_not_string(self):
        test_param_name = 123
        test_param_lastname = 435
        with self.assertRaises(TypeError):
            main.exercise_reverse_name(test_param_name, test_param_lastname)

    def test_exercise_none(self):
        test_param_name = None
        test_param_lastname = 'ora'
        with self.assertRaises(TypeError):
            main.exercise_reverse_name(test_param_name, test_param_lastname)



if __name__ == '__main__':
    unittest.main()