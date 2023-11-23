import time
import pandas as pd
import numpy as np
from datetime import datetime

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print("Kindly select what City you would like to explore, Chicago, NY, or Washington")

    try:
        city = input("Select a country (Chicago, New York, Washington): ").title()
    except (KeyboardInterrupt, KeyboardInterrupt):
        print('\nYou entered a wrong City value')

    if city in ['Chicago', 'New York', 'Washington']:
        print('\nYou have selected {}'.format(city))
        global file_data    
        file_data = pd.read_csv(CITY_DATA[city])
    else:
       print('Kindly choose from the available locations')
   


    # get user input for month (all, january, february, ... , june)
    # valid input for months available in X
    X = ['1', '2', '3', '4', '5', '6']
    try:
        xmonth = input('\nWhat month would you like to explore? Kindly indicate with numbers from 1 to 6 (Jan to June) or none (for all months): \n')
    except (KeyboardInterrupt, UnboundLocalError, NameError):
        print('\nWRONG INPUTE!!!')

    try:
        file_data['Start Time'] = pd.to_datetime(file_data['Start Time'])
        file_data['End Time'] = pd.to_datetime(file_data['End Time'])
    except (KeyboardInterrupt, UnboundLocalError, NameError):
        print('\nYou entered a wrong City value')

    if xmonth == 'none':
        print('You have selected to view all month data in {}.'.format(city.title()))
        month = 0
    elif xmonth in X:
        print('You have selected to desplay data of month {} in {}'.format(xmonth, city.title()))
        month = int(xmonth)
    else:
        print('Kindly input a valid option ie. 1 - 6 (for January to June) or none (for all data): \n')


    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\nPlease select a day (Mon, Tue, Wed, Thu, Fri, Sat, Sun) or choose none: ').title()
    xday = {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6,}

    if day in xday:
        print('you have Selected {}'.format(day))
        day = xday[day]
    elif day == 'None':
        print('you have selected no filter')
    else:
        print('Kindly select from the provided options')

    print('-'*40)
    return(city, month, day)



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    if month in [1, 2, 3, 4, 5, 6]:
        df1 = file_data.loc[file_data['Start Time'].dt.month == month]
    else:
        df1 = file_data

    if day in [0, 1, 2, 3, 4, 5, 6]:
        df = df1.loc[df1['Start Time'].dt.weekday == day]
    else:
        df = df1

    df = df.fillna(0)

    return df

#get_filters()

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    i = df['Start Time'].dt.month
    month_set = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June'}
    month_occurence = i.value_counts()

    max_month_occurence = month_occurence.idxmax()

    if max_month_occurence in month_set:        
        max_month = month_set[max_month_occurence]
        print('\n{} month has the highest occurence with {} counts.'.format(max_month, month_occurence[max_month_occurence]))


    # display the most common day of week
    j = df['Start Time'].dt.dayofweek
    day_set = {0:'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    day_occurence = j.value_counts()
    max_day_occurence = day_occurence.idxmax()

    if max_day_occurence in day_set:
        max_day = day_set[max_day_occurence]
        print('\n{} had the highest occurence of days with {} counts'.format(max_day, day_occurence[max_day_occurence]))



    # display the most common start hour
    k = df['Start Time'].dt.time
    #day_set = {0:'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    start_occurence = k.value_counts()
    max_start = start_occurence.idxmax()

    print('\n{} had the highest occurence of start times with {} counts'.format(max_start, start_occurence[max_start]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    i = df['Start Station']
    station_count = i.value_counts()
    freq_station = station_count.idxmax()
    print('\nThe most commonly used start station is {}'.format(freq_station))


    # display most commonly used end station
    j = df['End Station']
    station_count = j.value_counts()
    freq_station = station_count.idxmax()
    print('\nThe most commonly used end station is {}'.format(freq_station))

    # display most frequent combination of start station and end station trip

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    i = df['Trip Duration'].sum()
    print('\nTotal travel time was {}'.format(i))

    # display mean travel time
    i = df['Trip Duration'].mean()
    print('\nThe average travel time was {}'.format(i))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    i = df['User Type']
    user_types = i.value_counts()
    
    print('The user types available are: ')
    
    for a in range(len(user_types)):
        user_type = user_types.keys()
        print('{} = {}'.format(user_type[a], user_types[a]))
        a += 1

    # Display counts of gender
    i = df['Gender']
    genders = i.value_counts()
    
    print(genders)
    
    #for a in range(len(genders)):
    #    user_type = genders.keys()
    #    print(genders)
        #if genders[a] is str():
        #    print('{} = {}'.format(user_type[a], genders[a]))
    #    a += 1


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
