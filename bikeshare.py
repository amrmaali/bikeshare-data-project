import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

list_months = ['january', 'february', 'march', 'april', 'may', 'june']
list_days = ['saturday','sunday','monday','tuesday','wednesday','thursday','friday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please choose city name (chicago, new york city, washington): ').lower()
    while city not in CITY_DATA.keys():
        city = input('Please make sure city in the following list (chicago, new york city, washington): ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('If you want to filter by a specific month choose  one of the following: {} or type all to get data for the whole time-frame: '.format(list_months)).lower()
    while month not in list_months:
        if month == 'all':
            break
        else:
            month = input('Please make sure your choice for month was correct: ').lower()
     # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please choose a specific day to filter by form the following list {} or type all to get data for all weekdays: '.format(list_days)).lower()
    while day not in list_days:
        if day == 'all':
            break
        else:
            day = input('Please make sure your choice for day was correct').lower()

    print('-'*40)
    return city, month, day


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month is: %s ' % df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('The most common day of week is: %s ' % df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print('The most common start hour is: %s ' % df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common start station is: %s' % df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('The most common end station is: %s' % df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('The most common station combination is: %s' % (df['Start Station']+'-'+df['End Station']).mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total Travel Time is: %s hours' % (df['Trip Duration']/360).sum())

    # TO DO: display mean travel time
    print('Average Travel Time is: %s mins' % (df['Trip Duration']/60).mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('User Type Counts:\n %s ' % (df['User Type']).value_counts())

    if set(['Birth Year','Gender']).issubset(df.columns):
    # TO DO: Display counts of gender
        print('Count of users by Gender: \n %s' % (df['Gender']).value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
        print('Earliest birth year for a user: \n %s  ' % (df['Birth Year']).min())
        print('Latest birth year for a user:  \n %s  ' % (df['Birth Year']).max())
        print('Most Common birth year for a user: \n %s  ' % (df['Birth Year']).mean())
    else:
        print('\n Gender and Birth Year Data arent available !')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw(city):
    print('\n You can check raw data below \n')
    user_input = input('Would you like to see raw data? (yes/no): \n')
    pd.read_csv(CITY_DATA[city])
    while user_input == 'yes':
        try:
            for n in pd.read_csv(CITY_DATA[city], chunksize =5):
                print(n)
                user_input = input('Would you like to see raw data? (yes/no):')
                if user_input != 'yes':
                    print('Thank you!')
                    break
            break
        except KeyboardInterrupt:
            print('Thank you!')
    else:
        user_input = input('Please enter yes or no?: ')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw(city)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
