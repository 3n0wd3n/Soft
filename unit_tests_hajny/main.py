import unittest
from rodne_cislo import PersonalId

# python -m unittest -v test_main.py


class TestPersonalId(unittest.TestCase):

  def test_date(self):
    pid = PersonalId()
    self.assertEqual(pid.birth_date("000728/5707"), "2000-7-28")
    self.assertEqual(pid.birth_date("025226/5728"), "2002-2-26")
    self.assertEqual(pid.birth_date("026426/5728"), "bad input")

  def test_gender(self):
    pid = PersonalId()
    self.assertEqual(pid.gender("000728/5707"), "male")
    self.assertEqual(pid.gender("025226/5728"), "female")
    self.assertEqual(pid.gender("026426/5728"), "bad input")

  def test_over(self):
    pid = PersonalId()
    self.assertEqual(pid.is_valid("000728/5707"), True)
    self.assertEqual(pid.is_valid("025226/5728"), True)
    self.assertEqual(pid.is_valid("026426/5728"), False)
    

unittest.main()
