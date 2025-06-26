# utils.py

import numpy as np

def calculate_map_at_k(recommended_items, ground_truth, k=10):
    ap_sum = 0.0
    num_users_evaluated = 0

    for user_id, recs in recommended_items.items():
        if user_id not in ground_truth:
            continue

        relevant_items = ground_truth[user_id]
        if not relevant_items:
            continue

        precision_at_k = []
        hits = 0
        
        normalization_factor = min(len(relevant_items), k)
        if normalization_factor == 0:
            continue 

        for i, item_id in enumerate(recs[:k]):
            if item_id in relevant_items:
                hits += 1
                precision_at_k.append(hits / (i + 1))
        
        if not precision_at_k:
            ap_sum += 0.0
        else:
            ap_sum += np.sum(precision_at_k) / normalization_factor
        
        num_users_evaluated += 1
    
    if num_users_evaluated == 0:
        return 0.0
    return ap_sum / num_users_evaluated