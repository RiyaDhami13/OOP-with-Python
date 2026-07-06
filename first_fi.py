def print_details():
  try:
    name = "Riya Dhami"
    university = "Far Western University"
    department = "Computer Engineering"
    semester = "2nd"

    #using f string method
    print(f"Name: {name}")
    print(f"University: {university}")
    print(f"Department: {department}")
    print(f"Semester: {semester}")

  except Exception as error:
    print("Unable to display details.")

#entry point 
if __name__ == "__main__":
  print_details()
