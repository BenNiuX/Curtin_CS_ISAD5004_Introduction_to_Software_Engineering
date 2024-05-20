import io
import os
import sys
import unittest
import generation


class TestGeneration(unittest.TestCase):

    def test_get_generation_ep(self):
        self.assertEqual(None, generation.get_generation(1000))
        self.assertEqual("Silent Generation", generation.get_generation(1940))
        self.assertEqual("Baby Boomers", generation.get_generation(1950))
        self.assertEqual("Generation X", generation.get_generation(1970))
        self.assertEqual("Millennials", generation.get_generation(1980))
        self.assertEqual("Generation Z", generation.get_generation(2000))
        self.assertEqual("Generation Alpha", generation.get_generation(2020))
        self.assertEqual(None, generation.get_generation(2030))

    def test_get_generation_bva(self):
        self.assertEqual(None, generation.get_generation(1900))
        self.assertEqual("Silent Generation", generation.get_generation(1901))

        self.assertEqual("Silent Generation", generation.get_generation(1945))
        self.assertEqual("Baby Boomers", generation.get_generation(1946))

        self.assertEqual("Baby Boomers", generation.get_generation(1964))
        self.assertEqual("Generation X", generation.get_generation(1965))

        self.assertEqual("Generation X", generation.get_generation(1979))
        self.assertEqual("Millennials", generation.get_generation(1980))

        self.assertEqual("Millennials", generation.get_generation(1994))
        self.assertEqual("Generation Z", generation.get_generation(1995))

        self.assertEqual("Generation Z", generation.get_generation(2009))
        self.assertEqual("Generation Alpha", generation.get_generation(2010))

        self.assertEqual("Generation Alpha", generation.get_generation(2024))
        self.assertEqual(None, generation.get_generation(2025))

    def test_main_ep(self):
        sys.stdin = io.StringIO("20 May 2024")
        cap_out = io.StringIO()
        sys.stdout = cap_out
        actual = generation.main()
        self.assertTrue(actual)
        self.assertTrue("Generation Alpha\n" in cap_out.getvalue())
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__

        sys.stdin = io.StringIO("20 ABC 2024")
        actual = generation.main()
        self.assertFalse(actual)
        sys.stdin = sys.__stdin__

        input_file_name = "input.txt"
        output_file_name = "output.txt"
        with open(input_file_name, "w") as input_file:
            input_file.write("20 May 2024")
        actual = generation.main(input_file_name, output_file_name)
        self.assertTrue(actual)
        with open(output_file_name, "r") as output_file:
            self.assertTrue("Generation Alpha" in output_file.readline())
        os.remove(input_file_name)
        os.remove(output_file_name)

        input_file_name = "input.txt"
        with open(input_file_name, "w") as input_file:
            input_file.write("20 ABC 2024")
        actual = generation.main(input_file_name, output_file_name)
        self.assertFalse(actual)
        os.remove(input_file_name)

    def test_main_wb(self):
        input_file_name = "input.txt"
        output_file_name = "output.txt"
        with open(input_file_name, "w") as input_file:
            input_file.write("20 ABC 2024")
        actual = generation.main(input_file_name, output_file_name)
        self.assertFalse(actual)
        os.remove(input_file_name)

        input_file_name = "input.txt"
        with open(input_file_name, "w") as input_file:
            input_file.write("20 May 2024")
        actual = generation.main(input_file_name, "")
        self.assertFalse(actual)
        os.remove(input_file_name)

        input_file_name = "input.txt"
        output_file_name = "output.txt"
        with open(input_file_name, "w") as input_file:
            input_file.write("20 May 2024")
        actual = generation.main(input_file_name, output_file_name)
        self.assertTrue(actual)
        with open(output_file_name, "r") as output_file:
            self.assertTrue("Generation Alpha" in output_file.readline())
        os.remove(input_file_name)
        os.remove(output_file_name)
        
        sys.stdin = io.StringIO("20 ABC 2024")
        actual = generation.main()
        self.assertFalse(actual)
        sys.stdin = sys.__stdin__

        sys.stdin = io.StringIO("20 May 2024")
        cap_out = io.StringIO()
        sys.stdout = cap_out
        actual = generation.main()
        self.assertTrue(actual)
        self.assertTrue("Generation Alpha\n" in cap_out.getvalue())
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__


if __name__ == '__main__':
    unittest.main()
