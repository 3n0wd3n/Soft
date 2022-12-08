class PersonalId:
  def is_valid(self, personal_id):
    # Check if the number is divisible by 11 and if the month is valid
    return int(personal_id.replace("/", "")) % 11 == 0 and (
        int(personal_id[2:4]) in range(1, 13) or int(personal_id[2:4]) in range(51, 63))

  def gender(self, personal_id):
    # If the month is in the range 1-12, the gender is male
    if int(personal_id[2:4]) in range(1, 13):
      return "male"
    # If the month is in the range 51-62, the gender is female
    elif int(personal_id[2:4]) in range(51, 63):
      return "female"
    # If the month is not in either of these ranges, the input is invalid
    else:
      return "bad input"

  def birth_date(self, personal_id):
    # If the first two digits of the number are greater than 53, the year is in the 19xx range
    if int(personal_id[:2]) > 53:
      year = str(1900 + int(personal_id[:2]))
    # Otherwise, the year is in the 20xx range
    else:
      year = str(2000 + int(personal_id[:2]))

    # Get the gender of the person
    gender = self.gender(personal_id)

    # If the gender is female, the month is the original month minus 50
    if gender == "female":
      month = str(int(personal_id[2:4]) - 50)
    # If the gender is male, the month is the original month
    elif gender == "male":
      month = str(int(personal_id[2:4]))
    # If the gender is not male or female, the input is invalid
    else:
      return "bad input"

    # Return the birth date in the format "YYYY-MM-DD"
    return f"{year}-{month}-{personal_id[4:6]}"
