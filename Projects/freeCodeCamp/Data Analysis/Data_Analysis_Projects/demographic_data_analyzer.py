import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df.loc[df['sex'] == 'Male','age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((100 * (len(df.loc[df['education'] == 'Bachelors'])) / len(df)) ,1) 

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`

    # advanced ed and rich
    adv =  ((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')) & (df['salary'] == '>50K')
    # advanced ed
    h = (df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')
    # no adv education
    l = ((df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')) 
    # no adv ed and rich
    l_rich = ((df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')) & (df['salary'] == '>50K')  
  
    higher_education = (len(df[h]) / len(df))

    lower_education = len(df[l]) / len(df[l])

    # percentage by ed with salary >50K
    higher_education_rich = round((len(df[adv]) / len(df[h]))*100,1)

    lower_education_rich = round((100 * len(df[l_rich]) / len(df[l])),1)

  
  # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    minHrs = df['hours-per-week'] == min_work_hours
    richl = (df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')
  
    num_min_workers = len(df[richl])

    rich_percentage = round(100 * len(df.loc[richl]) / len(df[minHrs]),1)

    # What country has the highest percentage of people that earn >50K?
  
    # percentage of ppl in each country w/ high salary
    
    r = df['salary'] == '>50K' # rich
    earning_country = df.loc[r,'native-country'].value_counts() # all the countries and their # of rich ppl  

    # all the countries and every entry so pop.
    pop = df['native-country'].value_counts()

    # new data frame, divides earning_country by pop
    percentage = pd.DataFrame({'country':pd.Series(list(earning_country.index)),'percent': pd.Series([], dtype='float')})
    percentage.index = percentage['country'] 
    percentage.drop(['country'],axis=1)
    for index, row in percentage.iterrows():
      percentage.at[index,'percent'] = earning_country[row['country']] / pop[row['country']] # find something better!!

    # sort percentage, so most will be at top
    percentage = percentage.sort_values(by = 'percent',ascending = False)

    highest_earning_country = percentage.iloc[0].name

    highest_earning_country_percentage = round((percentage['percent'].iloc[0] * 100),1)

    # Identify the most popular occupation for those who earn >50K in India.
    top = (df['native-country'] == 'India') & (df['salary'] == '>50K')
    top_IN_occupation = df.loc[top, 'occupation'].mode()[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
