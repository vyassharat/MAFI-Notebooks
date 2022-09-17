import numpy as np

def sample_path(s0, mu, delta, r, sigma, start_time, end_time, dt):
    steps = int((end_time-start_time)/dt)
    path = np.zeros(steps)
    path[0]=s0
    for i in range(1,steps):
        dW = np.random.normal(0,1) * np.sqrt(dt)
        last = path[i-1]
        path[i] = last + (mu-delta)*last*dt + sigma*last*dW

    return path
