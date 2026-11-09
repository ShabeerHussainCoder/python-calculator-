r = 0
while True:
  while True:
    try:
      first_number = input("Enter the first number: ")
      if first_number == "q":
        r+=1
        break
      first_number = float(first_number)
      break
    except ValueError:
      print("Invalid input.Please try again.")
  while True:
    try:
      if r ==1:
        break
      second_number = input("Enter the second number: ")
      if second_number == "q":
        r+=1
        break
      second_number = float(second_number)
      break
    except ValueError:
      print("Invalid input.Please try again.")

  if r == 0:
   result = first_number + second_number
   print("Result:", result)
  else:
    print("you have exited the program.")


  if r == 1:
    break
  