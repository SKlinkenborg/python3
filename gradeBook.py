# Define lists of grades
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
# Your code below: 
# Add Computer Science score
gradebook.append(["computer science", 100])
# Add visual arts score
gradebook.append(["visual arts", 93])
# Update Visual Arts score by adding 5 points
gradebook[-1][-1] = gradebook[-1][-1] + 5
# Remove poetry score
gradebook[2].remove(85)
# Update poetry to contain "Pass" grade
gradebook[2].append("Pass")
# Append gradebook to last_semester_gradebook to create full_grade_book
full_gradebook = last_semester_gradebook + gradebook
for subject, grade in full_gradebook:
  print(f"{subject}: {grade}")