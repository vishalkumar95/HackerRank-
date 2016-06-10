# Your teacher has given you the task of drawing a staircase structure. 
# Being an expert programmer, you decided to make a program to draw it for you instead. 
# Given the required height, can you print a staircase as shown in the example?

# Input 
# You are given an integer  depicting the height of the staircase.

# Output 
# Print a staircase of height  that consists of # symbols and spaces. For example for , here's a staircase of that height:

def printStairs(num):
    # Keep track of the number of spaces to add
    spaces = num - 1
    # Run the loop to print the stairs
    for i in range(num):
        print (' ' * spaces + '#' * (i + 1))
        spaces = spaces - 1
