from sample_path import sample_path
from matplotlib import pyplot as plt
import numpy as np
def main():
    plt.title("Sample Paths of S(t)")
    plt.xlabel("Time (t)")
    plt.ylabel("Asset (S(t))")
    np.random.seed(123)
    time = np.arange(0,1,.001)
    for i in range(0,5):
        path = sample_path(100,0.1,0.025,.04,.5,0,1,.001)
        plt.plot(time, path)
    
    plt.show()

if __name__ == "__main__":
    main()