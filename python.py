import time
import pandas as pd
import numpy as np
#
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['january' , 'february' ,' march', 'april', 'may','june','july',' august',' september','october','november','december']

DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city= input("please input name of the city :\n").lower()
    while not city  in CITY_DATA :
       city = input("please input name of city again :\n").lower()
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("name of the month \n").lower()
    while not month  in MONTHS :
        month = input("please input name of the month again :\n").lower()   

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("name of th day :\n").lower()
    while not day in DAYS :
       day = input("please input name of the day again :\n").lower()
   
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

    if(city == "chicago") :
      df = pd.read_csv(CITY_DATA['chicago'])
    elif(city == "new_yourk") :
      df = pd.read_csv(CITY_DATA['new york city'])
    elif(city == "washington") :
      df = pd.read_csv(CITY_DATA['washington'])
   
    #convert start time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    df["day"] = df["Start Time"].dt.day
    df["month"] = df["Start Time"].dt.month
    return df




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    mode = df["month"].mode()[0]
    print("most common month is : ",mode)
   
   
    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day   
    mode = df['day'].mode()[0]
    print("most common day in the week is :", mode ) 
 
    # TO DO: display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    mode = df["hour"].mode()
    print("most common hour is :",mode)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    df['Start Statuon'] = df['Start Station']
    mode = df['Start Station'].mode()[0]
    print("The most common start station is :\n",mode)

    # TO DO: display most commonly used end station
    df['End Station'] = df['End Station']
    mode = df['End Station'].mode()[0]
    print("The most commonly used end station is :\n",mode)

    # TO DO: display most frequent combination of start station and end station trip
    df["trip"] = df["Start Station"] + df["End Station"]
    mode = df["trip"].mode()[0]      
    print(" most frequent combination of start station and end station trip is :\n",mode)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df["Trip Duration"] = df['Trip Duration'].sum()  
    mode = df['Trip Duration'].mode()[0]
    print("The total travel time is:\n ",mode)

    # TO DO: display mean travel time
    df["Trip Duration"] = df['Trip Duration'].mean()  
    mode = df['Trip Duration'].mode()[0]
    print("The mean travel time is:\n",mode)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    df["User Type"] = df["User Type"]
    mode = df['User Type'].value_counts()
    print("count of user types is\n :",mode)

    # TO DO: Display counts of gender
    
    if 'Gender' not in df.columns:
        print('this city have no gender ')
    else:
      mode = df["Gender"].value_counts()  
      print("Gender count is :",mode)
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df.columns:
        print("this city have no birth year data\n")
    else:    
      mode = df["Birth Year"].value_counts()
      print("most common year of birth is \n",mode)
    
    #recent year
      birth_year = df["Birth Year"]
      most_recent = birth_year.max()
      print("The most recent birth year:\n", most_recent)
    
    #earliest year
      birth_year = df["Birth Year"]
      earliest_year = birth_year.min()
      print("The most earliest birth year:\n", earliest_year)
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


def display_data(df):
    start = 0
    end = 5
    start_data = input('do you want to see more data? ').lower()
    if start_data == "yes":
       while end <= df.shape[0] :

           print(df.iloc[start:end])
           start += 5
           end += 5

           end_data = input("Do you want continue? ").lower()
           if end_data == 'no':
               break
   

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        print()
        if restart != 'yes' and restart != 'y' and restart != 'yus':
            break

if __name__ == "__main__":
	main()
