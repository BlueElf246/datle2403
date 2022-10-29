import matplotlib.pyplot as plt
import numpy as np
def run():
    n=np.linspace(1,100)
    plt.plot(n,7*n**2+6*n+5,label='7n^2+6n+5')
    plt.plot(n,7*n**2,label='7n^2')
    plt.legend(loc='upper left')
    plt.show()
def run1():
    n=np.linspace(1,100)
    plt.plot(n,(7*n**2+6*n+5)/(7*n**2),label='propotional')
    plt.legend(loc='upper left')
    plt.show()
def run2():
    n=np.linspace(1,100)
    plt.plot(n,(7*n**2+6*n+5)/(n**2),label='propotional')
    plt.legend(loc='upper left')
    plt.show()
def run3():
    n=np.linspace(1,10**199)
    plt.plot(n,n**0.1,color='y')
    plt.plot(n,(np.log(n))**5,color='r')
    plt.show()
run3()