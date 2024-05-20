import io
import os
import sys
import unittest
import common


class TestCommon(unittest.TestCase):

    def test_get_birthday_from_input_ep(self):
        sys.stdin = io.StringIO("20 May 2024")
        actual = common.get_birthday_from_input()
        self.assertEqual("20 May 2024", actual)
        sys.stdin = sys.__stdin__

    def test_get_birthday_from_file_ep(self):
        input_file_name = "input.txt"
        with open(input_file_name, "w") as input_file:
            input_file.write("20 May 2024")
        actual = common.get_birthday_from_file(input_file_name)
        self.assertEqual("20 May 2024", actual)
        os.remove(input_file_name)

    def test_write_output_to_console_ep(self):
        cap_out = io.StringIO()
        sys.stdout = cap_out
        common.write_output_to_console("Hello world!")
        self.assertEqual("Hello world!\n", cap_out.getvalue())
        sys.stdout = sys.__stdout__

    def test_write_output_to_file_ep(self):
        output_file_name = "output.txt"
        result = common.write_output_to_file("Hello world!", output_file_name)
        self.assertTrue(result)
        with open(output_file_name, "r") as output_file:
            self.assertEqual("Hello world!", output_file.readline())
        os.remove(output_file_name)

    def test_convert_birthdays_ep(self):
        actual = common.convert_birthdays("")
        self.assertEqual([], actual)

        actual = common.convert_birthdays("20 May 2024")
        self.assertEqual([(20, 5, 2024)], actual)

        actual = common.convert_birthdays("20 May 2024 01 01 2024")
        self.assertEqual([(20, 5, 2024), (1, 1, 2024)], actual)

        actual = common.convert_birthdays("1 1 2024 1 1 2024 1 1 2024")
        self.assertEqual([], actual)

    def test_convert_birthday_ep(self):
        try:
            actual = common.convert_birthday("20 May 0")
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

        try:
            actual = common.convert_birthday("20 ABC 2024")
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

        try:
            actual = common.convert_birthday("0 May 2024")
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

        try:
            actual = common.convert_birthday("20 ABC 10000")
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

        try:
            actual = common.convert_birthday("100 May 100")
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

        try:
            actual = common.convert_birthday("32 Month 2024")
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

        try:
            actual = common.convert_birthday("")
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

        try:
            actual = common.convert_birthday(None)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)

        actual = common.convert_birthday("20 Jan 2024")
        self.assertEqual((20, 1, 2024), actual)

        actual = common.convert_birthday("20 January 2024")
        self.assertEqual((20, 1, 2024), actual)

        actual = common.convert_birthday("20 01 2024")
        self.assertEqual((20, 1, 2024), actual)

    def test_verify_year_ep(self):
        self.assertEqual(-1, common.verify_year(1000))
        self.assertEqual(1957, common.verify_year(1957))
        self.assertEqual(-1, common.verify_year(3000))

    def test_verify_year_bva(self):
        self.assertEqual(-1, common.verify_year(1900))
        self.assertEqual(1901, common.verify_year(1901))

        self.assertEqual(2024, common.verify_year(2024))
        self.assertEqual(-1, common.verify_year(2025))

    def test_verify_month_ep(self):
        self.assertEqual(-1, common.verify_month(-10))
        self.assertEqual(11, common.verify_month(11))
        self.assertEqual(-1, common.verify_month(20))

    def test_verify_month_bva(self):
        self.assertEqual(-1, common.verify_month(0))
        self.assertEqual(1, common.verify_month(1))

        self.assertEqual(12, common.verify_month(12))
        self.assertEqual(-1, common.verify_month(13))

    def test_verify_day_ep(self):
        self.assertEqual(-1, common.verify_day(-10))
        self.assertEqual(11, common.verify_day(11))
        self.assertEqual(-1, common.verify_day(40))

    def test_verify_day_bva(self):
        self.assertEqual(-1, common.verify_day(0))
        self.assertEqual(1, common.verify_day(1))

        self.assertEqual(31, common.verify_day(31))
        self.assertEqual(-1, common.verify_day(32))

    def test_convert_month_str_ep(self):
        self.assertEqual(-1, common.convert_month_str("ABC"))
        self.assertEqual(-1, common.convert_month_str(""))
        self.assertEqual(-1, common.convert_month_str(None))
        self.assertEqual(1, common.convert_month_str("Jan"))
        self.assertEqual(1, common.convert_month_str("January"))
        self.assertEqual(1, common.convert_month_str("01"))

    def test_get_birthday_from_input_wb(self):
        sys.stdin = io.StringIO("20 May 2024")
        actual = common.get_birthday_from_input()
        self.assertEqual("20 May 2024", actual)
        sys.stdin = sys.__stdin__

    def test_get_birthday_from_file_wb(self):
        input_file_name = "input.txt"
        with open(input_file_name, "w") as input_file:
            input_file.write("20 May 2024")
        actual = common.get_birthday_from_file(input_file_name)
        self.assertEqual("20 May 2024", actual)
        os.remove(input_file_name)

        actual = common.get_birthday_from_file(input_file_name)
        self.assertEqual("", actual)

    def test_write_output_to_console_wb(self):
        cap_out = io.StringIO()
        sys.stdout = cap_out
        common.write_output_to_console("Hello world!")
        self.assertEqual("Hello world!\n", cap_out.getvalue())
        sys.stdout = sys.__stdout__

    def test_write_output_to_file_wb(self):
        output_file_name = "output.txt"
        result = common.write_output_to_file("Hello world!", output_file_name)
        self.assertTrue(result)
        with open(output_file_name, "r") as output_file:
            self.assertEqual("Hello world!", output_file.readline())
        os.remove(output_file_name)

        result = common.write_output_to_file("Hello world!", "")
        self.assertFalse(result)

    def test_convert_birthdays_wb(self):
        self.assertEqual([], common.convert_birthdays(None))
        self.assertEqual([], common.convert_birthdays("20 May"))
        self.assertEqual([(20, 5, 2024)],
                         common.convert_birthdays("20 May 2024"))
        self.assertEqual([], common.convert_birthdays("20 ABC 2024"))

    def test_convert_birthday_wb(self):
        try:
            actual = common.convert_birthday(None)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)
        try:
            actual = common.convert_birthday("20 May")
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)
        try:
            actual = common.convert_birthday("20 ABC 2024")
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)
        actual = common.convert_birthday("20 May 2024")
        self.assertTrue((20, 5, 2024), actual)

    def test_verify_year_wb(self):
        self.assertEqual(2000, common.verify_year(2000))
        self.assertEqual(-1, common.verify_year(1900))

    def test_verify_month_wb(self):
        self.assertEqual(2, common.verify_month(2))
        self.assertEqual(-1, common.verify_month(0))

    def test_verify_day_wb(self):
        self.assertEqual(2, common.verify_day(2))
        self.assertEqual(-1, common.verify_day(0))

    def test_convert_month_str_wb(self):
        self.assertEqual(1, common.convert_month_str("Jan"))
        self.assertEqual(1, common.convert_month_str("January"))
        self.assertEqual(1, common.convert_month_str("1"))
        self.assertEqual(-1, common.convert_month_str("TEST"))


if __name__ == '__main__':
    unittest.main()
