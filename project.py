from random import randint
import numpy as np
from sklearn.cluster import KMeans

__author__ = "Yogesh Patil, Sahana B S, Vandana Ramesh , Samarth H"
__title__ = "IPL Player Selection Optimization using K-means Clustering of 10D Feature Vector"

lines_to_be_deleted = []

# Open the batsmen data set and convert to numpy readable form
def getBattingData():
    fbat = open("data_bat.txt", "r")
    data = np.loadtxt(fbat)
    fbat.close()
    return data

# Open the bowlers data set and convert to numpy readable form
def getBowlingData():
    fbowl = open("data_bowl.txt", "r")
    data = np.loadtxt(fbowl)
    fbowl.close()
    return data

def clusterData(data):
    km = KMeans(n_clusters=3)
    index = km.fit_predict(data)

    for i in range(len(index)):
        if index[i] == 2:
            np.delete(data, i, 0)
        elif index[i] == 1:
            np.delete(data, i, 0)
        elif index[i] == 0:
            np.delete(data, i, 0)
    return data, i, index[i]

if __name__ == '__main__':

    lines_to_be_deleted = []
    my_batsmen = []
    my_bowlers = []
    removed_batsmen = []
    removed_bowlers = []
    num_batsmen = 25
    num_bowlers = 25
    best_bat_index = []
    avg_bat_index = []
    bad_bat_index = []
    best_bowl_index = []
    avg_bowl_index = []
    bad_bowl_index = []
    category = []
    num_bidders = 3
    num_rounds = 5
    bat_players = open("batsmen.txt")               # Contains list of batsmen
    ball_players = open("bowlers.txt")              # Contains list of bowlers
    bat_players_lines = bat_players.readlines()     # To read the list of batsmen from the file
    ball_players_lines = ball_players.readlines()   # To read the list of bowlers from the file
    bowlers_data = getBowlingData()

    #BATSMEN
    # For num_rounds of bidding for batsmen
    for k in range(0, num_rounds):
        print "ROUND " + str(k) + ": "

        del lines_to_be_deleted[:]
        del best_bat_index[:]
        del avg_bat_index[:]
        del bad_bat_index[:]

        batsmen_data = getBattingData()

        for i in range(0, num_batsmen):
            batsmen_data, player, category = clusterData(batsmen_data)
            if category == 0:
                best_bat_index.append(i)
            if category == 1:
                avg_bat_index.append(i)
            if category == 2:
                bad_bat_index.append(i)

        # Display list of batsmen
        print "Best batsmen:"
        print best_bat_index
        for i in range(0, len(best_bat_index)):
            print bat_players_lines[best_bat_index[i]]

        print "Average batsmen:"
        print avg_bat_index
        for i in range(0, len(avg_bat_index)):
            print bat_players_lines[avg_bat_index[i]]

        print "Worst batsmen:"
        print bad_bat_index
        for i in range(0, len(bad_bat_index)):
            print bat_players_lines[bad_bat_index[i]]

        # Your team selects 1 player
        var1 = best_bat_index[randint(0, len(best_bat_index))-1]
        my_batsmen.append(var1)
        removed_batsmen.append(var1)
        lines_to_be_deleted.append(var1)

        # Remove num_bidders number of players randomly from the data set => auctioned already
        for i in range(0, num_bidders-1):
            if len(best_bat_index) != 0:
                var = best_bat_index[randint(0, len(best_bat_index) - 1)]
                removed_batsmen.append(var)
                lines_to_be_deleted.append(var)
            elif len(avg_bat_index) != 0:
                var = avg_bat_index[randint(0, len(best_bat_index) - 1)]
                removed_batsmen.append(var)
                lines_to_be_deleted.append(var)
            elif len(bad_bat_index) != 0:
                var = bad_bat_index[randint(0, len(best_bat_index) - 1)]
                removed_batsmen.append(var)
                lines_to_be_deleted.append(var)

        print "After round " + str(k) + ": "

        print "Players auctioned so far: "
        # print removed_batsmen
        for i in range(0, len(removed_batsmen)):
            print bat_players_lines[removed_batsmen[i]]

        print "My team after round " + str(k) + ": "
        # print my_batsmen
        for i in range(0, len(my_batsmen)):
            print bat_players_lines[my_batsmen[i]]
        print lines_to_be_deleted

        # for line in fbat_lines:
        #    if line != lines_to_be_deleted[0]:
        #        fbat.write(line)
        # deleteLines()
        print "END OF ROUND " + str(k)
        print "===================================="
    print "END OF BATSMEN BIDDING"
    print "\n\n"


    #BOWLERS
    # For num_rounds of bidding for batsmen
    for k in range(0, num_rounds):
        print "ROUND " + str(k) + ": "

        del best_bowl_index[:]
        del avg_bowl_index[:]
        del bad_bowl_index[:]

        bowlers_data = getBowlingData()

        for i in range(0, num_bowlers):
            bowlers_data, player, category = clusterData(bowlers_data)
            if category == 0:
                best_bowl_index.append(i)
            if category == 1:
                avg_bowl_index.append(i)
            if category == 2:
                bad_bowl_index.append(i)

        # Display list of batsmen
        print "Best bowlers:"
        print best_bowl_index
        for i in range(0, len(best_bowl_index)):
            print ball_players_lines[best_bowl_index[i]]

        print "Average bowlers:"
        print avg_bowl_index
        for i in range(0, len(avg_bowl_index)):
            print ball_players_lines[avg_bowl_index[i]]

        print "Worst batsmen:"
        print bad_bowl_index
        for i in range(0, len(bad_bowl_index)):
            print ball_players_lines[bad_bowl_index[i]]

        # Your team selects 1 player
        var1 = best_bowl_index[randint(0, len(best_bowl_index))-1]
        my_bowlers.append(var1)
        removed_bowlers.append(var1)

        # Remove num_bidders number of players randomly from the data set => auctioned already
        for i in range(0, num_bidders-1):
            if len(best_bowl_index) != 0:
                removed_bowlers.append(best_bowl_index[randint(0, len(best_bowl_index) - 1)])
            elif len(avg_bowl_index) != 0:
                removed_bowlers.append(avg_bowl_index[randint(0, len(best_bowl_index) - 1)])
            elif len(bad_bowl_index) != 0:
                removed_bowlers.append(bad_bowl_index[randint(0, len(best_bowl_index) - 1)])

        print "After round " + str(k) + ": "

        print "Players auctioned so far: "
        # print removed_bowlers
        for i in range(0, len(removed_bowlers)):
            print ball_players_lines[removed_bowlers[i]]

        print "My team after round " + str(k) + ": "
        # print my_bowlers
        for i in range(0, len(my_bowlers)):
            print ball_players_lines[my_bowlers[i]]

        print "END OF ROUND " + str(k)
        print "===================================="
    print "END OF BOWLERS BIDDING"
    print "\n\n"

    print "My final team consists of: "
    # print my_batsmen
    print "Batsmen: "
    for i in range(0, len(my_batsmen)):
        print bat_players_lines[my_batsmen[i]]
    # print my_bowlers
    print "Bowlers: "
    for i in range(0, len(my_bowlers)):
        print ball_players_lines[my_bowlers[i]]
