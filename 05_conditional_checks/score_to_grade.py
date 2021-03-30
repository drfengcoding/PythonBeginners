try:
  score = int(input("What's your score?"))
except ValueError:
  print("Please enter a number!")
else:
  if score > 100 or score < 0:
    print("Invalid score.")
  elif score >= 70:
    print("Grade A.")
  elif score >=60:
    print("Grade B.")
  elif score >=50:
    print("Grade C.")
  else:
    print("Grade D.")

