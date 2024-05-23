import io
import os
import sys
import unittest
import life_path_number


class TestLifePathNumber(unittest.TestCase):

    def setUp(self):
        self.input_file_name = "input.txt"
        self.output_file_name = "output.txt"

    def tearDown(self):
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
        if os.path.exists(self.input_file_name):
            os.remove(self.input_file_name)
        if os.path.exists(self.output_file_name):
            os.remove(self.output_file_name)

    def test_calc_life_path_number_ep(self):
        self.assertEqual(7,
                         life_path_number.calc_life_path_number(21, 5, 2024))
        self.assertEqual(9,
                         life_path_number.calc_life_path_number(11, 5, 1901))
        self.assertEqual(11,
                         life_path_number.calc_life_path_number(2, 8, 1990))

    def test_add_digists_ep(self):
        self.assertEqual(11, life_path_number.add_digists(11))
        self.assertEqual(11, life_path_number.add_digists(1901))
        self.assertEqual(3, life_path_number.add_digists(12))
        self.assertEqual(7, life_path_number.add_digists(1987))

    def test_is_master_number_ep(self):
        self.assertTrue(life_path_number.is_master_number(11))
        self.assertTrue(life_path_number.is_master_number(22))
        self.assertTrue(life_path_number.is_master_number(33))
        self.assertFalse(life_path_number.is_master_number(21))

    def test_is_master_number_bva(self):
        self.assertFalse(life_path_number.is_master_number(10))
        self.assertTrue(life_path_number.is_master_number(11))
        self.assertTrue(life_path_number.is_master_number(11))
        self.assertFalse(life_path_number.is_master_number(12))
        self.assertFalse(life_path_number.is_master_number(21))
        self.assertTrue(life_path_number.is_master_number(22))
        self.assertTrue(life_path_number.is_master_number(22))
        self.assertFalse(life_path_number.is_master_number(23))
        self.assertFalse(life_path_number.is_master_number(32))
        self.assertTrue(life_path_number.is_master_number(33))
        self.assertTrue(life_path_number.is_master_number(33))
        self.assertFalse(life_path_number.is_master_number(34))

    def test_get_lucky_colour_ep(self):
        self.assertEqual("Red", life_path_number.get_lucky_colour(1))
        self.assertEqual("Orange", life_path_number.get_lucky_colour(2))
        self.assertEqual("Yellow", life_path_number.get_lucky_colour(3))
        self.assertEqual("Green", life_path_number.get_lucky_colour(4))
        self.assertEqual("Sky Blue", life_path_number.get_lucky_colour(5))
        self.assertEqual("Indigo", life_path_number.get_lucky_colour(6))
        self.assertEqual("Violet", life_path_number.get_lucky_colour(7))
        self.assertEqual("Magenta", life_path_number.get_lucky_colour(8))
        self.assertEqual("Gold", life_path_number.get_lucky_colour(9))
        self.assertEqual("Silver", life_path_number.get_lucky_colour(11))
        self.assertEqual("White", life_path_number.get_lucky_colour(22))
        self.assertEqual("Crimson", life_path_number.get_lucky_colour(33))
        self.assertEqual(None, life_path_number.get_lucky_colour(0))

    def test_get_lucky_colour_bva(self):
        self.assertEqual(None, life_path_number.get_lucky_colour(0))
        self.assertEqual("Red", life_path_number.get_lucky_colour(1))
        self.assertEqual("Gold", life_path_number.get_lucky_colour(9))
        self.assertEqual(None, life_path_number.get_lucky_colour(10))
        self.assertEqual(None, life_path_number.get_lucky_colour(10))
        self.assertEqual("Silver", life_path_number.get_lucky_colour(11))
        self.assertEqual("Silver", life_path_number.get_lucky_colour(11))
        self.assertEqual(None, life_path_number.get_lucky_colour(12))
        self.assertEqual(None, life_path_number.get_lucky_colour(21))
        self.assertEqual("White", life_path_number.get_lucky_colour(22))
        self.assertEqual("White", life_path_number.get_lucky_colour(22))
        self.assertEqual(None, life_path_number.get_lucky_colour(23))
        self.assertEqual(None, life_path_number.get_lucky_colour(32))
        self.assertEqual("Crimson", life_path_number.get_lucky_colour(33))
        self.assertEqual("Crimson", life_path_number.get_lucky_colour(33))
        self.assertEqual(None, life_path_number.get_lucky_colour(34))

    def test_calc_life_path_number_wb(self):
        self.assertEqual(5, life_path_number.calc_life_path_number(1, 1, 2001))
        self.assertEqual(5, life_path_number.calc_life_path_number(9, 7, 2005))

    def test_add_digists_wb(self):
        self.assertEqual(11, life_path_number.add_digists(11))
        self.assertEqual(1, life_path_number.add_digists(1990))
        self.assertEqual(3, life_path_number.add_digists(2001))
        self.assertEqual(0, life_path_number.add_digists(-1))

    def test_is_master_number_wb(self):
        self.assertFalse(life_path_number.is_master_number(1))

    def test_get_lucky_colour_wb(self):
        self.assertEqual("Silver", life_path_number.get_lucky_colour(11))
        self.assertEqual("Red", life_path_number.get_lucky_colour(1))
        self.assertEqual(None, life_path_number.get_lucky_colour(0))

    def test_main_ep(self):
        sys.stdin = io.StringIO("20 May 2024")
        cap_out = io.StringIO()
        sys.stdout = cap_out
        actual = life_path_number.main()
        self.assertTrue(actual)
        self.assertTrue("Indigo" in cap_out.getvalue())
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

        sys.stdin = io.StringIO("20 ABC 2024")
        actual = life_path_number.main()
        self.assertFalse(actual)
        sys.stdin = sys.__stdin__

        with open(self.input_file_name, "w") as input_file:
            input_file.write("20 May 2024")
        actual = life_path_number.main(self.input_file_name,
                                       self.output_file_name)
        self.assertTrue(actual)
        with open(self.output_file_name, "r") as output_file:
            self.assertTrue("Indigo" in output_file.readline())
        os.remove(self.input_file_name)
        os.remove(self.output_file_name)

        with open(self.input_file_name, "w") as input_file:
            input_file.write("20 ABC 2024")
        actual = life_path_number.main(self.input_file_name,
                                       self.output_file_name)
        self.assertFalse(actual)
        os.remove(self.input_file_name)

        sys.stdin = io.StringIO("20 May 2024 20 May 2024")
        cap_out = io.StringIO()
        sys.stdout = cap_out
        actual = life_path_number.main()
        self.assertTrue(actual)
        self.assertTrue("True" in cap_out.getvalue())
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

        sys.stdin = io.StringIO("20 May 2024 21 May 2024")
        cap_out = io.StringIO()
        sys.stdout = cap_out
        actual = life_path_number.main()
        self.assertTrue(actual)
        self.assertTrue("False" in cap_out.getvalue())
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

    def test_main_wb(self):
        with open(self.input_file_name, "w") as input_file:
            input_file.write("20 ABC 2024")
        actual = life_path_number.main(self.input_file_name,
                                       self.output_file_name)
        self.assertFalse(actual)
        os.remove(self.input_file_name)

        with open(self.input_file_name, "w") as input_file:
            input_file.write("20 May 2024")
        actual = life_path_number.main(self.input_file_name, "")
        self.assertFalse(actual)
        os.remove(self.input_file_name)

        with open(self.input_file_name, "w") as input_file:
            input_file.write("20 May 2024")
        actual = life_path_number.main(self.input_file_name,
                                       self.output_file_name)
        self.assertTrue(actual)
        with open(self.output_file_name, "r") as output_file:
            self.assertTrue("6" in output_file.readline())
        os.remove(self.input_file_name)
        os.remove(self.output_file_name)

        with open(self.input_file_name, "w") as input_file:
            input_file.write("20 May 2024 20 May 2024")
        actual = life_path_number.main(self.input_file_name,
                                       self.output_file_name)
        self.assertTrue(actual)
        with open(self.output_file_name, "r") as output_file:
            self.assertTrue("True" in output_file.readline())
        os.remove(self.input_file_name)
        os.remove(self.output_file_name)

        sys.stdin = io.StringIO("20 ABC 2024")
        actual = life_path_number.main()
        self.assertFalse(actual)
        sys.stdin = sys.__stdin__

        sys.stdin = io.StringIO("20 May 2024")
        cap_out = io.StringIO()
        sys.stdout = cap_out
        actual = life_path_number.main()
        self.assertTrue(actual)
        self.assertTrue("6" in cap_out.getvalue())
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

        sys.stdin = io.StringIO("20 May 2024 20 May 2024")
        cap_out = io.StringIO()
        sys.stdout = cap_out
        actual = life_path_number.main()
        self.assertTrue(actual)
        self.assertTrue("True" in cap_out.getvalue())
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__


if __name__ == '__main__':
    unittest.main()
