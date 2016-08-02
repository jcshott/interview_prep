"""
We are given a string consisting of letters- F,L,R. - which is the instruction a robot follows

F- goes forward by one step.

L-turn left.

R- turn right.

String length can be upto 2500 characters.

REASONING FROM STACK OVERFLOW (I didn't get the 4 runs initially)
Each run(one run is executing all commands of the given string once) changes two things: the direction which the robot looks to and its position(that is, each run shifts it by some vector(the direction of this vector depends on the its initial direction before the run) and rotates it).

The number of possible directions is 4. Thus, after running the simulation 4 times it looks in the same direction as it did initially(each rub rotates it by the same angle).

That's why 4 consecutive runs just shift it by some vector without any rotation.

Thus, we can just run the simulation 4 times in a row and see if it stopped in the original point. If it did, we can find the minimum circle that contains its path. Otherwise, no such circle exists.

"""

dir_right = {"N": "E", "E": "S", "S": "W", "W": "N"}
dir_left = {"N": "W", "W": "S", "S": "E", "E": "N"}

def  doesCircleExists(commands):
    output = []
    curr_dir = "N"
    curr_x = 0
    curr_y = 0
    for command_string in commands:
        for x in range(4):
            for c in command_string:
                if c == "R":
                    curr_dir = dir_right[curr_dir]
                elif c == "L":
                    curr_dir = dir_left[curr_dir]
                elif c == "G":
                    if curr_dir == "N":
                        curr_y += 1
                    if curr_dir == "E":
                        curr_x += 1
                    if curr_dir == "S":
                        curr_y -= 1
                    if curr_dir == "W":
                        curr_x -= 1
        if curr_x == 0 and curr_y == 0:
            output.append("YES")
        else:
            output.append("NO")
        curr_dir = "N"
        curr_x = 0
        curr_y = 0
    return output
