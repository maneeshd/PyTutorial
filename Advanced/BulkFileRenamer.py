"""
@author: Maneesh D
@email: maneeshd77@gmail.com
@created: 08-Apr-17
"""
from os import rename, listdir

ep_map = {"E1": "I'm Leslie Knope",
          "E2": "Ron and Tammys",
          "E3": "Born & Raised",
          "E4": "Pawnee Rangers",
          "E5": "Meet n Greet",
          "E6": "End of the World",
          "E7": "The Treaty",
          "E8": "Smallest Park",
          "E9": "The Trial of Leslie Knope",
          "E10": "Citizen Knope",
          "E11": "The Comeback Kid",
          "E12": "Campaign Ad",
          "E13": "Bowling for Votes",
          "E14": "Operation Ann",
          "E15": "Dave Returns",
          "E16": "Sweet Sixteen",
          "E17": "Campaign Shake-Up",
          "E18": "Lucky",
          "E19": "Live Ammo",
          "E20": "The Debate",
          "E21": "Bus Tour",
          "E22": "Win, Lose, or Draw"}

path = "D:\\Parks and Rec\\Season 4\\"
try:
    for file in listdir(path):
        # name = file.replace("Episode ", "E")
        # if file[-6:-4] == "20" or file[-6:-4] == "10":
        #     name = "E" + file[-6:-4] + ".mp4"
        # else:
        #     name = "E" + file[-6:-4] + ".mp4"
        #     name = name.replace("0", "")
        fk = file.replace(".mp4", "")
        name = fk + " - " + dick.get(fk) + ".mp4"
        print(file, " -> ", name)
        rename(path+file, path+name)
except FileExistsError:
    pass
