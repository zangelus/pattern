import sysconfig
import NormalDistribution
import SimplerNormalDistribution
import NormalDistributionContour
import Sinusoidal
import DecisionBoundaryNormalDistributions
import ScatterPlot3d
import ScatterPlot3dColor


def main():

    while True:
        print("pick an option to plot")
        print("1-Sinusoidal")
        print("2-Normal distribution multivariable")
        print("3-Normal distribution multivariable contour")
        print("4-Decision boundary Normal distribution multivariable")
        print("5-Scatter 3d")
        print("6-Scatter 3d color")
        print("0-exit")
        option = input()
        x = int(option)
        if(x==1):
            print("plotting sinu")
            Sinusoidal.plot()    
        elif (x==2):
            NormalDistribution.plot()
        elif (x==3): 
            NormalDistributionContour.plot()
        elif (x==4):
            DecisionBoundaryNormalDistributions.plot()
        elif (x==5):
            ScatterPlot3d.plot()
        elif (x==6):
            ScatterPlot3dColor.plot()
        else:
            break

if __name__ == "__main__":
    main()