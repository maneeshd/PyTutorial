"""
@author: Maneesh D
@date: 5/26/2017
@intepreter: Python 3.6
"""
from operator import itemgetter


print("-" * 78)
print("                            Itemgetter Sorting")
print("-" * 78)
dat = [("C", 1), ("C++", 2), ("Java", 3), ("Python", 4), ("Go", 5), ("Assembly", 1)]
print(sorted(dat, key=itemgetter(0)))
print(sorted(dat, key=itemgetter(0), reverse=True))
print()
print(sorted(dat, key=itemgetter(1)))
print(sorted(dat, key=itemgetter(1), reverse=True))
print()
print(sorted(dat, key=itemgetter(1, 0)))
print(sorted(dat, key=itemgetter(0, 1), reverse=True))
print("-" * 78)
print("                            Dictionary Sorting")
print("-" * 78)
# Sorting Dictionaries
d = {"C": 1, "C++": 2, "Python": 4, "Java": 3, "Go": 5, "Assembly": 1}
print(sorted(d.items(), key=itemgetter(0)))     # Sort Based on keys
print(sorted(d.items(), key=itemgetter(1)))     # Sort Based on value
