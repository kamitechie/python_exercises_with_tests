import unittest
import main
import calendar


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

    def test_exercise_reverse_fullname(self):
        test_param_name = 'Anna'
        test_param_lastname = 'Jo'
        result = main.exercise_reverse_name(test_param_name, test_param_lastname)
        self.assertEqual(result, 'oJ annA')

    def test_exercise_reverse_fullname_lowercase(self):
        test_param_name = 'WILL'
        test_param_lastname = 'SHO'
        result = main.exercise_reverse_name(test_param_name, test_param_lastname)
        self.assertEqual(result, 'OHS LLIW')

    def test_exercise_reverse_fullname_uppercase(self):
        test_param_name = 'fo'
        test_param_lastname = 'ally'
        result = main.exercise_reverse_name(test_param_name, test_param_lastname)
        self.assertEqual(result, 'ylla of')

    def test_exercise_reverse_fullname_not_string(self):
        test_param_name = 123
        test_param_lastname = 435
        with self.assertRaises(TypeError):
            main.exercise_reverse_name(test_param_name, test_param_lastname)

    def test_exercise_reverse_fullname_none(self):
        test_param_name = None
        test_param_lastname = 'ora'
        with self.assertRaises(TypeError):
            main.exercise_reverse_name(test_param_name, test_param_lastname)

    # 6 exercise tests

    def test_exercise_list_to_tuple(self):
        test_param = [1, 2, 3, 4, 5, 6]
        self.assertEqual(main.exercise_list_to_tuple(test_param), (1, 2, 3, 4, 5, 6))

    def test_exercise_list_to_tuple_num_and_str(self):
        test_param = [1, 'two', 3, 4]
        self.assertEqual(main.exercise_list_to_tuple(test_param), (1, 'two', 3, 4))

    def test_exercise_list_to_tuple_empty(self):
        test_param = []
        self.assertEqual(main.exercise_list_to_tuple(test_param), ())

    def test_exercise_list_to_tuple_none(self):
        test_param = None
        with self.assertRaises(TypeError):
            main.exercise_list_to_tuple(test_param)

    # 7 exercise tests

    def test_exercise_file_ext(self):
        test_param = 'main.py'
        self.assertEqual(main.exercise_file_ext(test_param), 'py')

    def test_exercise_file_ext_no_ext(self):
        test_param = 'projectpy'
        self.assertEqual(main.exercise_file_ext(test_param), 'Incorrect file name')

    def test_exercise_file_ext_none(self):
        test_param = None
        with self.assertRaises(TypeError):
            main.exercise_file_ext(test_param)

    def test_exercise_file_ext_num(self):
        test_param = 345
        with self.assertRaises(TypeError):
            main.exercise_file_ext(test_param)

    # 8 exercise tests

    def test_exercise_colors(self):
        test_param = ['red', 'blue', 'yellow', 'green']
        self.assertEqual(main.exercise_colors(test_param), 'First color: red\nLast color: green')

    def test_exercise_colors_numbers_in_list(self):
        test_param = ['yellow', 'green', 3, 4]
        self.assertEqual(main.exercise_colors(test_param), 'The list is not valid')

    def test_exercise_colors_empty(self):
        test_param = []
        self.assertEqual(main.exercise_colors(test_param), 'There are no colors in a list')

    def test_exercise_colors_none(self):
        test_param = None
        with self.assertRaises(TypeError):
            main.exercise_colors(test_param)

    # 9 exercise tests

    def test_exercise_exam_date(self):
        test_param = (2021, 8, 23)
        self.assertEqual(main.exercise_exam_date(test_param), 'The examination will start from : 2021 / 8 / 23')

    def test_exercise_exam_date_str(self):
        test_param = 'July 23'
        with self.assertRaises(TypeError):
            main.exercise_exam_date(test_param)

    def test_exercise_exam_date_not_valid(self):
        test_param = (2021, 20, 23)
        self.assertEqual(main.exercise_exam_date(test_param), 'This date does not exist')

    def test_exercise_exam_date_none(self):
        test_param = None
        with self.assertRaises(TypeError):
            main.exercise_exam_date(test_param)

    # 10 exercise tests

    def test_exercise_triple_sum(self):
        test_param = 1
        self.assertEqual(main.exercise_triple_sum(test_param), 6)

    def test_exercise_triple_sum_zero(self):
        test_param = 0
        self.assertEqual(main.exercise_triple_sum(test_param), 0)

    def test_exercise_triple_sum_negative(self):
        test_param = -1
        self.assertEqual(main.exercise_triple_sum(test_param), -6)

    def test_exercise_triple_sum_str(self):
        test_param = 'one'
        with self.assertRaises(TypeError):
            main.exercise_triple_sum(test_param)

    def test_exercise_triple_sum_none(self):
        test_param = None
        with self.assertRaises(TypeError):
            main.exercise_triple_sum(test_param)

    # 14 exercise tests

    #def test_exercise_diff_days(self):
     #   test_param_date1 = (2014, 3, 21)
      #  test_param_date2 = (2014, 3, 14)
       # self.assertEqual(main.exercise_diff_days(test_param_date1, test_param_date2), 7)

    #def test_exercise_diff_days_str(self):
     #   test_param_date1 = '2014, 9, 7'
      #  test_param_date2 = (2014, 3, 14)
       # with self.assertRaises(TypeError):
        #    main.exercise_diff_days(test_param_date1, test_param_date2)

    # 15 exercise tests

    def test_exercise_sphere_volume(self):
        test_param = 1
        self.assertEqual(main.exercise_sphere_volume(test_param), 'Sphere volume: 4.1887902047863905')

    def test_exercise_sphere_volume_negative(self):
        test_param = -1
        with self.assertRaises(ValueError):
            main.exercise_sphere_volume(test_param)

    def test_exercise_sphere_volume_none(self):
        test_param = None
        with self.assertRaises(TypeError):
            main.exercise_sphere_volume(test_param)

    def test_exercise_sphere_volume_not_num(self):
        test_param = 'one'
        with self.assertRaises(TypeError):
            main.exercise_sphere_volume(test_param)

    # 15 exercise tests

    def test_exercise_number_diff(self):
        test_param = 2
        self.assertEqual(main.exercise_number_diff(test_param), 15)

    def test_exercise_number_diff_negative(self):
        test_param = -2
        self.assertEqual(main.exercise_number_diff(test_param), 19)

    def test_exercise_number_diff_zero(self):
        test_param = 0
        self.assertEqual(main.exercise_number_diff(test_param), 17)

    def test_exercise_number_diff_str(self):
        test_param = 'two'
        with self.assertRaises(TypeError):
            main.exercise_number_diff(test_param)

    def test_exercise_number_diff_none(self):
        test_param = None
        with self.assertRaises(TypeError):
            main.exercise_number_diff(test_param)

    # narcissist exercise tests

    def test_number_narcissist_true(self):
        test_param = 1634
        self.assertTrue(main.number_narcissist(test_param))

    def test_number_narcissist_false(self):
        test_param = 123
        self.assertFalse(main.number_narcissist(test_param))

    def test_number_narcissist_zero(self):
        test_param = 0
        with self.assertRaises(ValueError):
            main.number_narcissist(test_param)

    def test_number_narcissist_negative(self):
        test_param = -12
        with self.assertRaises(ValueError):
            main.number_narcissist(test_param)

    def test_number_narcissist_not_num(self):
        test_param = 'one'
        with self.assertRaises(TypeError):
            main.number_narcissist(test_param)

    def test_number_narcissist_none(self):
        test_param = None
        with self.assertRaises(TypeError):
            main.number_narcissist(test_param)

    # exercise to cap case tests

    def test_to_cap_case(self):
        test_param = "How can mirrors be real if our eyes aren't real"
        self.assertEqual(main.to_cap_case(test_param), "How Can Mirrors Be Real If Our Eyes Aren't Real")

    def test_to_cap_case_numbers(self):
        test_param = 234
        with self.assertRaises(TypeError):
            main.to_cap_case(test_param)

    def test_to_cap_case_none(self):
        test_param = None
        with self.assertRaises(TypeError):
            main.to_cap_case(test_param)

    # vowel count exercise tests

    def test_vowel_count(self):
        test_param = 'awesomness'
        self.assertEqual(main.get_count(test_param), 4)

    def test_vowel_count_uppercase(self):
        test_param = 'AwesOmness'
        self.assertEqual(main.get_count(test_param), 4)

    def test_vowel_count_num(self):
        test_param = 367
        with self.assertRaises(TypeError):
            main.get_count(test_param)

    def test_vowel_count_none(self):
        test_param = None
        with self.assertRaises(TypeError):
            main.get_count(test_param)

    # moving zeros exercise tests

    def test_move_zeros(self):
        test_param = [1, 0, 3, 5, 0, 1]
        self.assertEqual(main.move_zeros(test_param), [1, 3, 5, 1, 0, 0])

    def test_move_zeros_list_with_str(self):
        test_param = [0, '2', 3, '5', 0, 1]
        self.assertEqual(main.move_zeros(test_param), ['2', 3, '5', 1, 0, 0])

    def test_move_zeros_all_zeros(self):
        test_param = [0, 0, 0]
        self.assertEqual(main.move_zeros(test_param), [0, 0, 0])

    def test_move_zeros_empty(self):
        test_param = []
        self.assertEqual(main.move_zeros(test_param), 'List is empty')

    def test_move_zeros_none(self):
        test_param = None
        with self.assertRaises(TypeError):
            main.move_zeros(test_param)

    def test_move_zeros_not_list(self):
        test_param = 123
        with self.assertRaises(TypeError):
            main.move_zeros(test_param)


if __name__ == '__main__':
    unittest.main()
