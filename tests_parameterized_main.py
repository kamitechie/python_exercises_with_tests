import unittest
import main
from parameterized import parameterized


class TestMain(unittest.TestCase):
    # 5 exercise tests
    @parameterized.expand([
        ('test_exercise_reverse_fullname_basic', 'Anna', 'Jo', 'oJ annA'),
        ('test_exercise_reverse_fullname_uppercase', 'WILL', 'SHO', 'OHS LLIW'),
        ('test_exercise_reverse_fullname_lowercase', 'foo', 'ally', 'ylla oof'),
        ('test_exercise_reverse_fullname_not_string', 123, 123, None, TypeError),
        ('test_exercise_reverse_fullname_none', None, 'smth', None, TypeError)
    ])
    def test_exercise_reverse_fullname(self, name, in_1, in_2, expected, expected_error=None):
        if expected_error is None:
            assert main.exercise_reverse_name(in_1, in_2) == expected
        else:
            with self.assertRaises(TypeError):
                main.exercise_reverse_name(in_1, in_2)


if __name__ == '__main__':
    unittest.main()
