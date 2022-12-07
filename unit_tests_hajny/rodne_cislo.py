class RodneCislo:

  def over(self, rc):
    return int(rc.replace("/", "")) % 11 == 0 and int(rc[2:4]) in range(
      1, 13) or int(rc[2:4]) in range(51, 63)

  def pohlavi(self, rc):
    if int(rc[2:4]) - 50 in range(1, 13):
      return "žena"
    elif int(rc[2:4]) in range(1, 13):
      return "muž"
    else:
      return "bad input"

  def datum_narozeni(self, rc):
    if int(rc[:2]) > 53:
      year = str(1900 + int(rc[:2]))
    else:
      year = str(2000 + int(rc[:2]))

    if self.pohlavi(rc) == "žena":
      mesic = str(int(rc[2:4]) - 50)
    elif self.pohlavi(rc) == "muž":
      mesic = str(int(rc[2:4]))
    else:
      return "bad input"

    return f"{rc[4:6]}.{mesic}.{year}"