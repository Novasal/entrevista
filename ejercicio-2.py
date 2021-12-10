import pandas as pd


def season_of_date(date):
    """Return season of date."""
    year = str(date.year)
    seasons = {
        'spring': pd.date_range(start='19/03/'+year, end='19/06/'+year),
        'summer': pd.date_range(start='20/06/'+year, end='21/09/'+year),
        'fall': pd.date_range(start='22/09/'+year, end='20/12/'+year)
    }
    if date in seasons['spring']:
        return 'Spring'
    elif date in seasons['summer']:
        return 'Summer'
    elif date in seasons['fall']:
        return 'Fall'
    else:
        return 'Winter'


def get_season(df):
    """Return DataFrame with the orders and their deliver season."""
    df.ORD_DT = pd.to_datetime(df.ORD_DT)
    df['SEASON'] = df['ORD_DT'].map(season_of_date)
    df.drop(['ORD_DT', 'QT_ORDD'], axis=1, inplace=True)
    return df


input = pd.DataFrame({
    'ORD_ID': [
        '113-8909896-6940269', '114-0291773-7262677',
        '114-0291773-7262697', '114-9900513-7761000',
        '112-5230502-8173028', '112-7714081-3300254',
        '114-5384551-1465853', '114-7232801-4607440'
    ],
    'ORD_DT': [
        '09/23/19', '01/01/20', '12/05/19', '09/24/20',
        '01/30/20', '05/02/20', '04/02/20', '10/09/20'
    ],
    'QT_ORDD': [
        1, 1, 1, 1, 1, 1, 1, 1
    ]
})

print(get_season(input))
