from social_age  import get_social_status
import unittest


class TestSocialAge(unittest.TestCase):

    def test_can_get_child(self):
        age = 12
        expected_res = 'ребёнок'
        function_res = get_social_status(age)
        self.assertEqual(expected_res, function_res)

    def test_can_get_teenager(self):
        age = 17
        expected_res = 'подросток'
        function_res = get_social_status(age)
        self.assertEqual(expected_res, function_res)

    def test_can_get_grown(self):
        age = 19
        expected_res = 'взрослый'
        function_res = get_social_status(age)
        self.assertEqual(expected_res, function_res)

    def test_can_get_grand(self):
        age = 52
        expected_res = 'пожилой'
        function_res = get_social_status(age)
        self.assertEqual(expected_res, function_res)

    def test_cannot_pass_str_age(self):
        age = "8"
        with self.assertRaises(ValueError):
            get_social_status(age)

    def test_minus_age(self):
        age = -5
        with self.assertRaises(ValueError):
            get_social_status(age)
