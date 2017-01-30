"""""""""""""""""""""""""""""
"  Created On: 17-Oct-2016  "
"  Author: Maneesh D        "
"""""""""""""""""""""""""""""


def jug_solution(l_jug, s_jug, goal):
    print("Solving the water jug problem...")
    goal_reached = 0
    jug1 = 0
    jug2 = 0
    while goal_reached != 1:
        if jug1 == goal:
            goal_reached = 1
            print("Goal Reached... =>(" + str(jug1) + "," + str(jug2) + ")")
            print("Problem Solved...")
            exit(0)
        if jug1 == 0:
            jug1 = l_jug
            print(
                "Fill up " +
                str(l_jug) +
                "-gallon jug... =>(" +
                str(l_jug),
                str(jug2) +
                ")")
        elif jug1 > 0 and jug2 != s_jug:
            filled = 0
            while filled != 1:
                jug2 += 1
                jug1 -= 1
                if jug2 == s_jug or jug1 == 0:
                    filled = 1
            print(
                "Transfer from " +
                str(l_jug) +
                "-gallon jug to " +
                str(s_jug) +
                "-gallon jug... =>(" +
                str(jug1) +
                "," +
                str(jug2) +
                ")")
        elif jug1 > 0 and jug2 == s_jug:
            jug2 = 0
            print(str(s_jug) + "-gallon jug emptied... =>(" + str(jug1) + ",0)")


large_jug = int(input("Enter the size of the larger jug(gallons): "))
small_jug = int(input("Enter the size of the smaller jug(gallons): "))
target = int(
    input("Enter the final amount of water to be left in the larger jug(gallons): "))
if small_jug > large_jug or target > large_jug:
    print("Invalid Inputs...Are you a retard?...")
    exit(0)
jug_solution(large_jug, small_jug, target)
