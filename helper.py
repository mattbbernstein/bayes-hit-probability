import numpy as np
from sklearn.metrics import accuracy_score, recall_score, f1_score


def get_bases_earned(row):
    hit_events = {
        'single':1,
        'double':2,
        'triple':3,
        'home_run':4
    }

    if row['events'] in hit_events:
        return hit_events[row['events']]
    return 0

def get_spray_angle(row):
    spray_angle = (np.arctan(
        (row["hc_x"]-125.42) / (198.27-row["hc_y"]))
        ) *(180/np.pi) * 0.75
    if row["stand"] == "L":
        spray_angle *= -1
    return spray_angle

def cm_scores(true, pred):
    return{
        "Accuracy":accuracy_score(true, pred), 
        "Sensitivity":recall_score(true, pred), 
        "Specificity":recall_score(true, pred, pos_label=0),
        "F1 Score": f1_score(true, pred)
    }