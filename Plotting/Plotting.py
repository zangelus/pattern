import sysconfig
import NormalDistribution
import SimplerNormalDistribution
import NormalDistributionContour
import Sinusoidal
import DecisionBoundaryNormalDistributions


def main():

    while True:
        print("pick an option to plot")
        print("1-Sinusoidal")
        print("2-Normal distribution multivariable")
        print("3-Normal distribution multivariable contour")
        print("4-Decision boundary Normal distribution multivariable")
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
        else:
            break

if __name__ == "__main__":
    main()