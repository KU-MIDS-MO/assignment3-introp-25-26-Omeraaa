import numpy as np

def moving_average(signal, window_size):
    n = len(signal)
    result = np.zeros(n, dtype=float)
    
    k = (window_size - 1) // 2
    
    for i in range(n):
        start_index = i - k
        if start_index < 0:
            start_index = 0
            
        end_index = i + k + 1
        if end_index > n:
            end_index = n

        current_window = signal[start_index : end_index]

        result[i] = np.mean(current_window)
        
    return result