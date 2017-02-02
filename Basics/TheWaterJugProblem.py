"""
@author: Maneesh D
@email: maneeshd77@gmail.com

You have two jugs: a 4-gallon jug and a 3-gallon jug. Neither of the jugs have markings on them.
There is a pump that can be used to fill the jugs with water.
How can you get exactly two gallons of water in the 4-gallon jug?

Algorithm: x=>4-gallon jug & y=>3-gallon jug
----------
Goal: Fill exactly 2 gallons of water in the 4-gallon jug.
Steps:
1.Completely fill th 4-gallon jug. =>(4,y), 0<=x<=4 & 0<=y<=3
2.Pour water from 4-gallon jug to completely fill 3-gallon jug. =>(1,3)
3.Empty 3-gallon jug. =>(1,0)
4.Pour the remaining 1 gallon of water from 4-gallon jug to 3-gallon jug. =>(0,1)
5.Fill up the 4-gallon jug. =>(4,1)
6.Fill up the 3-gallon jug. =>(2,3)
7.Empty 3-gallon jug, now you have 2 gallons of water in 4-gallon jug. =>(2,0)
"""


def water_jug():
    # initial state
    _4g_jug = 0
    _3g_jug = 0
    _4max = 4
    _3max = 3
    goal_reached = 0

    print("Solving the water jug problem...")
    while goal_reached != 1:
        if _4g_jug == 2:
            goal_reached = 1
            print("Goal Reached... =>(" + str(_4g_jug) + "," + str(_3g_jug) + ")")
        if _4g_jug == 0:
            _4g_jug = _4max
            print("Fill up 4-gallon jug... =>(4," + str(_3g_jug) + ")")
        elif _4g_jug > 0 and _3g_jug != _3max:
            filled = 0
            while filled != 1:
                _3g_jug += 1
                _4g_jug -= 1
                if _3g_jug == _3max or _4g_jug == 0:
                    filled = 1
            print("Transfer from 4-gallon jug to 3-gallon jug... =>(" +
                  str(_4g_jug) + "," + str(_3g_jug) + ")")
        elif _4g_jug > 0 and _3g_jug == _3max:
            _3g_jug = 0
            print("3-gallon jug emptied... =>(" + str(_4g_jug) + ",0)")

    print("Problem Solved...")


if __name__ == '__main__':
    water_jug()
