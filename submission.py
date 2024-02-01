import matplotlib.pyplot as plt
import numpy as np

def find_chords(radians, identifiers):
  chords = {}
  for i, point in enumerate(identifiers):
    # Deconstruct the identifier into a position ('s' or 'e') and a unique identifier (1 or 2)
    identifier = int(point[1])
    
    # If the identifier isn't in chords yet, create a list containing two dummy values
    if identifier not in chords:
      chords[identifier] = [float('inf'), 0]
    
    # Sort the values so that the starting point is always the lesser valaue
    if radians[i] < chords[identifier][0]:
      chords[identifier][0] = radians[i]
    else:
      chords[identifier][1] = radians[i]
  return chords

def count_intersections(radians, identifiers) -> int:
  intersections = 0

  # Step 1: Enumerate through the identifiers to determine the positions points that make up the lines
  chords = find_chords(radians, identifiers)

  # Step 2: Check all combinations of chords to determine if they intersect using the following logic:
  # If s1 < s2 < e1 or s2 < e1 < e2, we know that the chords intersect
  for i in range(len(chords)):
    for j in range(i + 1, len(chords)):
      s1, e1 = chords[i + 1]
      s2, e2 = chords[j + 1]
      
      if (s1 < s2 < e1) and (s2 < e1 < e2):
        intersections += 1

  return intersections

# Test cases:
radians1 = [0.78, 1.47, 1.77, 3.92]
identifiers1 = ['s1', 's2', 'e1', 'e2']
print("Example 1:", count_intersections(radians1, identifiers1))

radians2 = [0.90, 1.30, 1.70, 2.92]
identifiers2 = ['s1', 'e1', 's2', 'e2']
print("Example 2:", count_intersections(radians2, identifiers2))

radians3 = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]
identifiers3  = ['s1', 's2', 'e1', 'e2', 's3', 's4', 'e3', 'e4']
print("Example 3:", count_intersections(radians3, identifiers3))

radians4 = [0.25, 1.25, 2.25, 3.5, 4.5, 6.0]
identifiers4 = ['e1', 'e2', 'e3', 's1', 's2', 's3']
print("Example 4:", count_intersections(radians4, identifiers4))

radians5 = [1, 2, 3, 4]
identifiers5 = ['s2', 's1', 'e1', 'e2']
print("Example 5:", count_intersections(radians5, identifiers5))

# Visual Representation of Test Cases
input_case = input("Enter a test case number (1 - 5): ")
input_case = int(input_case)
match input_case:
  case 1:
    sampleRadians = radians1
    sampleIdentifiers = identifiers1
  case 2:
    sampleRadians = radians2
    sampleIdentifiers = identifiers2
  case 3:
    sampleRadians = radians3
    sampleIdentifiers = identifiers3
  case 4:
    sampleRadians = radians4
    sampleIdentifiers = identifiers4
  case 5:
    sampleRadians = radians5
    sampleIdentifiers = identifiers5

radius = 1
angles = np.linspace(0, np.pi * 4)
xl = np.sin(angles) * radius
yl = np.cos(angles) * radius
plt.figure(figsize=(4, 4))
plt.plot(xl, yl)

# Draw point labels
for i, (x, y) in enumerate(zip(np.sin(sampleRadians) * radius, np.cos(sampleRadians) * radius)):
  plt.text(x, y + 0.1, sampleIdentifiers[i], color='black', ha='center', va='bottom')

# Draw line segments
samplePoints = find_chords(sampleRadians, sampleIdentifiers)  
for i in range(1, len(samplePoints) + 1):
  plt.plot([np.sin(samplePoints[i][0]) * radius, np.sin(samplePoints[i][1]) * radius],
           [np.cos(samplePoints[i][0]) * radius, np.cos(samplePoints[i][1]) * radius],
           color='red')

plt.scatter(np.sin(sampleRadians) * radius, np.cos(sampleRadians) * radius, color='orange', label='Example 4')
plt.show()