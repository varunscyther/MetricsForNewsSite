"""
This program is using panda library for reading the csv file data.
On the basis of data following metrics are created
- Click through rate - number of users on previous page/number of users on current page * 100
- Conversion rate per page - number of users on previous page/number of users on current page * 100
- Average page per time - [Σ(Time Spent on a Page by a User) / Number of Users]
- Share reading ratio - Number of people share the page/number of users on the page
"""

import pandas as pd

"""
Function to set up the initial data set values.
Using panda library reading it from csv and creating input data list
"""


def setup():
    global input_data_list
    dataset = pd.read_csv("input/dataset.csv");

    input_data_list = []
    for index, data_row_set in dataset.iterrows():
        input_data_list.append(data_row_set)


"""
Function to calculate all the metrics associated with new sites.
"""


def calculate_metrics():
    click_through_rate()
    coversion_rate_per_page()
    average_page_time()
    share_reading_ratio


"""
Function to calculate all the click through rate.
"""


def click_through_rate():
    dictionary = {}
    for data in input_data_list:
        if not bool(dictionary):
            dictionary[data[0]] = {}
            dictionary[data[0]]["numberOfClicks"] = data[3]
            dictionary[data[0]]["numberOfAds"] = data[4]
        else:
            for day, info in list(dictionary.items()):
                if data[0] == day:
                    for key in info:
                        if key == "numberOfClicks":
                            stored_no_of_clicks = dictionary[data[0]]["numberOfClicks"]
                            stored_no_of_clicks += data[3]
                            dictionary[data[0]]["numberOfClicks"] = stored_no_of_clicks
                        elif key == "numberOfAds":
                            stored_no_of_ads = dictionary[data[0]]["numberOfAds"]
                            stored_no_of_ads += data[4]
                            dictionary[day]["numberOfAds"] = stored_no_of_ads
                elif data[0] != day:
                    dictionary[data[0]] = {}
                    dictionary[data[0]]["numberOfClicks"] = data[3]
                    dictionary[data[0]]["numberOfAds"] = data[4]

    for day, details in dictionary.items():
        print("Day : " + str(day) + " , " + "total no. of clicks over ads is : " + str(details["numberOfClicks"])
              + " and " + "total no. of ads display : " + str(details["numberOfAds"])
              + " so the click through rate (total no. of clicks over ads/total no. of ads display * 100) is : "
              + str((details["numberOfClicks"] / details["numberOfAds"]) * 100))


"""
Function to calculate the conversion rate per page.
"""


def coversion_rate_per_page():
    for data in input_data_list:
        print("For day : " + str(data[0]) + " and page no :" + str(data[1])
              + " , the conversion rate (number of users on previous page/number of users on current page * 100 ) is : "
              + str((data[7] / data[6]) / 100))


"""
Function to calculate the average page per time.
"""


def average_page_time():
    for data in input_data_list:
        total_time_spent = data[9] * 5 + data[10] * 10
        number_of_users = data[5]
        print("For day : " + str(data[0]) + " and page no :" + str(data[1])
              + " , the  is average page time ([Σ(Time Spent on a Page by a User) / Number of Users] is : "
              + str((total_time_spent / number_of_users)))


"""
Function to calculate the share reading ratio.
"""


def share_reading_ratio():
    for data in input_data_list:
        no_of_users_shared_the_page = data[11]
        number_of_users = data[5]
        print("For day : " + str(data[0]) + " and page no :" + str(data[1])
              + " , the share reading ratio (number of people share the page/number of users on the page) is : "
              + str((no_of_users_shared_the_page / number_of_users)))


setup()
calculate_metrics()
