import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race = pd.Series(df['race'])
    race_count = race.value_counts()

    # What is the average age of men?
    mask = df['sex'] == 'Male'
    average_age_men = df[mask].loc[:, 'age'].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    mask = df['education'] == 'Bachelors'
    percentage_bachelors =  round((((len(df[mask])) * 100) / len(df)), 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    h_mask = (df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')
    h_income_mask = ((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')) & (df['salary'] == '>50K')
    # What percentage of people without advanced education make more than 50K?
    l_mask = (df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')
    l_income_mask = ((df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')) & (df['salary'] == '>50K')
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # percentage with salary >50K
    higher_education_rich = round(((len(df[h_income_mask]) * 100) / len(df[h_mask])), 1)
    lower_education_rich = round(((len(df[l_income_mask]) * 100) / len(df[l_mask])), 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers_mask = (df['salary'] == '>50K') & (df['hours-per-week'] == min_work_hours)
    num_min_hours_workers_mask = (df['hours-per-week'] == min_work_hours)
    num_min_workers = len(df[num_min_hours_workers_mask])
    rich_percentage = round((len(df[num_min_workers_mask]) * 100) / num_min_workers)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_countries = df.loc[df['salary'] == '>50K', 'native-country'].value_counts()
    population_country = df.loc[df['native-country'] != '', 'native-country'].value_counts()

    highest_earning_country = None
    highest_earning_country_percentage = 0

    # Calculate percentage of high earners for each country and find max
    earning_percentages = (highest_earning_countries * 100 / population_country)
    highest_earning_country = earning_percentages.idxmax()
    highest_earning_country_percentage = round(earning_percentages.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.loc[(df['salary'] == '>50K') & (df['native-country'] == 'India'), 'occupation'].value_counts().index[0]

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
