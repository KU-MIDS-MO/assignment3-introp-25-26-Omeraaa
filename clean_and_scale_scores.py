import numpy as np

def clean_and_scale_scores(scores, min_score, max_score):
    cleaned_scores = np.array(scores, dtype=float)
    
    if cleaned_scores.ndim == 1:
        for i in range(len(cleaned_scores)):
            val = cleaned_scores[i]
            if val < min_score:
                cleaned_scores[i] = min_score
            elif val > max_score:
                cleaned_scores[i] = max_score
                
    elif cleaned_scores.ndim == 2:
        rows, cols = cleaned_scores.shape
        for r in range(rows):
            for c in range(cols):
                val = cleaned_scores[r, c]
                if val < min_score:
                    cleaned_scores[r, c] = min_score
                elif val > max_score:
                    cleaned_scores[r, c] = max_score

    range_diff = max_score - min_score
    
    scaled_scores = (cleaned_scores - min_score) / range_diff
    
    return scaled_scores