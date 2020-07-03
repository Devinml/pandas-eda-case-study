import pandas as pd



if __name__ == '__main__':
    df_cities = pd.read_csv('../data/cities.csv')
    df_lines = pd.read_csv('../data/lines.csv')
    df_station_lines = pd.read_csv('../data/station_lines.csv')
    df_stations = pd.read_csv('../data/stations.csv')
    df_systems = pd.read_csv('../data/systems.csv')
    df_track_lines = pd.read_csv('../data/track_lines.csv')
    df_tracks = pd.read_csv('../data/tracks.csv')

    print (df_cities.head())
    print (df_lines.head())
    print (df_station_lines.head())
    print (df_stations.head())
    print (df_systems.head())
    print (df_track_lines.head())
    print (df_tracks.head())