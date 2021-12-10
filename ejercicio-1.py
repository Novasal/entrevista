import pandas as pd


def weather_change(df):
    """Return a DataFrame with the dates when the weather changed."""
    # Store only the dates when it rained
    rainy_days = df[df.was_rainy == True].reset_index()
    flag_index = 0
    for idx in range(0, len(rainy_days)-1):
        # Check if the date from the current index and the next are non-consecutive
        if (rainy_days['index'][idx] - rainy_days['index'][idx+1]) != -1:
            # If the dates are non-consecutive that means the weather changed
            indexes_to_drop = rainy_days[(rainy_days.index <= idx) & (
                rainy_days.index > flag_index)].index
            # Drop dates from the current flag till the current looping index
            rainy_days.drop(indexes_to_drop, inplace=True)
            flag_index = idx+1

    # If the weather in the last date didn't changed some dates escape the filtering
    if flag_index != rainy_days.index[-1]:
        idx = rainy_days.index[-1]
        indexes_to_drop = rainy_days[(rainy_days.index <= idx) & (
            rainy_days.index > flag_index)].index
        rainy_days.drop(indexes_to_drop, inplace=True)

    return rainy_days


input = pd.DataFrame({
    'date': [
        '1/1/20', '1/2/20', '1/3/20', '1/4/20', '1/5/20',
        '1/6/20', '1/7/20', '1/8/20', '1/9/20', '1/10/20'
    ],
    'was_rainy': [
        False, True, True, False, False,
        True, False, True, True, True
    ]
})

print(weather_change(input))
