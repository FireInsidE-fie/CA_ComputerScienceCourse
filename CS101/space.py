# https://www.codecademy.com/paths/computer-science/tracks/cspath-cs-101/
# modules/cspath-python-control-flow/lessons/python-control-flow/exercises/review

print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")

weight = 185
planet = 3

# Write an if statement below:
if planet == 1:
    print(weight * 0.91)
elif planet == 2:
    print(weight * 0.38)
elif planet == 3:
    print(weight * 2.34)
elif planet == 4:
    print(weight * 1.06)
elif planet == 5:
    print(weight * 0.92)
elif planet == 6:
    print(weight * 1.19)
else:
    print("""There was an error when trying to determine which planet was
    selected.""")
