####### utils tests #####
from utils import *
import numpy as np
import matplotlib.pyplot as plt





def rngRangeTest(testRange, sampleSize):
    print "starting..."
    rng = Rng()
    freq = [0 for i in range(testRange)]
    for i in range(sampleSize):
        freq[rng.randRange(testRange)] += 1
    N = testRange

    ind = np.arange(N)  # the x locations for the groups
    width = 0.5       # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, freq, width, color='r')

##    womenMeans = (25, 32, 34, 20, 25)
##    womenStd = (3, 5, 2, 3, 3)
##    rects2 = ax.bar(ind + width, womenMeans, width, color='y', yerr=womenStd)

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of rng range.')
    ax.set_xticks(ind + width)
    ax.set_xticklabels([i for i in range(testRange)])

##    ax.legend((rects1[0], rects2[0]), ('Men', 'Women'))
    print "autolabel..."

##    def autolabel(rects):
##        # attach some text labels
##        for rect in rects:
##            height = rect.get_height()
##            ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
##                    '%d' % int(height),
##                    ha='center', va='bottom')
##
##    autolabel(rects1)
##    autolabel(rects2)
    print "gonna show plot..."
    plt.show()
        

if __name__=="__main__":
    rngRangeTest(20, 100000)
        
    
