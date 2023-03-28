from pybaseball import statcast, cache
import pandas as pd

DATA_FILE="project/data.csv"

def main():
    cache.enable()
    data = statcast(start_dt='2022-06-01', end_dt='2022-06-30')
    data = data[data['type'] == 'X']
    cols = [
        'events',
        'hit_distance_sc',
        'launch_angle',
        'launch_speed',
        'estimated_ba_using_speedangle'
    ]
    data = data.filter(items=cols)
    data.to_csv(DATA_FILE)

if __name__ == "__main__":
    main()