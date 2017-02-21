##### 3bet range stats #########
from utils import *
from collections import deque
import numpy as np
import matplotlib.pyplot as plt

# 3betting hands
ax = Card("A","x")
kx = Card("K","x")
qx = Card("Q","x")
aces = Hand(ax,ax)
kings = Hand(kx,kx)
queens = Hand(qx,qx)
aceKing = Hand(ax,kx)
aceQueen = Hand(ax,qx)
# 3.8% of hands with AQ
threeBet_hands = [aces, kings, queens, aceKing, aceQueen]

'''
test 3bet reliability for sample_size
'''
def lab_3bet(sample_size, test_depth, rounding=2):
    hg = HandGenerator()
    deq = deque()
    num3BetHands = 0
    freq_map = {}
    # line graph?
    figure, axes = plt.subplots()
    points = []
    # populate deque
    for i in range(sample_size):
        newHand = hg.randomHand()
        if i % 9 != 0 and containsHand(newHand, threeBet_hands):
            num3BetHands += 1
            deq.append(1)
        else:
            deq.append(0)
    for i in range(test_depth - sample_size):
        oldValue = deq.popleft()
        num3BetHands -= oldValue
        newHand = hg.randomHand()
        if i % 9 != 0 and containsHand(newHand, threeBet_hands):
            num3BetHands += 1
            deq.append(1)
        else:
            deq.append(0)
        point = num3BetHands * 100.0 / sample_size
        freq = round(point, rounding)
        points.append(point)
        if freq not in freq_map:
            freq_map[freq] = 1
        else:
            freq_map[freq] += 1

    # build line graph?
    axes.plot(points)
    axes.set_ylabel('3bet %')
    axes.set_title('Progression of perceived 3bet %.')
    # build chart
    size = len(freq_map)
    ind = np.arange(size)
    width = 0.8
    keys = freq_map.keys()
    keys.sort()
    freq = [freq_map[key] for key in keys]
    fig, ax = plt.subplots()
    rect = ax.bar(ind, freq, width, color='r')
    ax.set_ylabel('Frequency')
    ax.set_xlabel("3bet %")
    ax.set_title('Frequency of perceived 3bet for fixed 3bet range.')
    ax.set_xticks(width / 2 + ind)
    ax.set_xticklabels(keys)
    print "building plot..."
    print freq_map

    plt.show()

if __name__ == "__main__":
    print "Starting 3bet_lab"
    lab_3bet(58, 200)
        



    
