import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
	def test_first_last_name(self):
		formatted_name = get_formatted_name('donald', 'trump')
		self.assertEqual(formatted_name, 'Donald Trump')

	def test_first_last_middle_name(self):
		formatted_name = get_formatted_name('uhuru', 'kenyatta', 'muigai')
		self.assertEqual(formatted_name, 'Uhuru Muigai Kenyatta')

unittest.main()