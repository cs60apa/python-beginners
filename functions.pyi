# math functions
import math

# ratio = signal_power / noise_power
# decibels = 10 * math.log10(ratio)

# math.radians = 0.7
# height = math.sin(math.radians)

# examples 1

# note that the execution can only take place using the python ide
degrees = 45
radians = degrees / 180.0 * math.pi
math.sin(radians)

# output 
# 0.7071067811865476

math.sqrt(2) / 2.0

# OutPut
# 0.7071067811865476

# composite functions
x = math.sin(degrees / 360.0 * 2 * math.pi)

x = math.exp(math.log(x+1))

print(x)
# minutes = hours * 60 // correct way of writing composite function
# hours * 60 = minutes // this is wrong 

# Adding new function
def print_lyrics():
    print(" im a dealer and am okay like that")
    print("I nolonger sleep,just coding and coffee")

