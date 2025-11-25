import numpy as np

def count_values_in_bins(data, bin_edges):
    num_bins = len(bin_edges) - 1
    
    counts = np.zeros(num_bins, dtype=int)
    
    # Her bir kutu icin dongu
    for i in range(num_bins):
        lower_bound = bin_edges[i]
        upper_bound = bin_edges[i+1]

        current_count = 0

        for val in data:
            if i == num_bins - 1:
                if val >= lower_bound and val <= upper_bound:
                    current_count += 1
            else:
                if val >= lower_bound and val < upper_bound:
                    current_count += 1
        
        counts[i] = current_count
        
    return counts