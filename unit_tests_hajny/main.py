import unittest
from rodne_cislo import RodneCislo

# python -m unittest -v test_main.py


class TestRodneCislo(unittest.TestCase):

  def test_date(self):
    rc = RodneCislo()
    self.assertEqual(rc.datum_narozeni("000728/5707"), "28.7.2000")
    self.assertEqual(rc.datum_narozeni("025226/5728"), "26.2.2002")
    self.assertEqual(rc.datum_narozeni("026426/5728"), "bad input")

  def test_gender(self):
    rc = RodneCislo()
    self.assertEqual(rc.pohlavi("000728/5707"), "muž")
    self.assertEqual(rc.pohlavi("025226/5728"), "žena")
    self.assertEqual(rc.pohlavi("026426/5728"), "bad input")

  def test_over(self):
    rc = RodneCislo()
    self.assertEqual(rc.over("000728/5707"), True)
    self.assertEqual(rc.over("025226/5728"), True)
    self.assertEqual(rc.over("026426/5728"), False)
    


unittest.main()
