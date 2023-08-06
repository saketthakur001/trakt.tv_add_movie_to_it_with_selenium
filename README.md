# Selenium Automation for trakt.tv

This code demonstrates how to use Selenium version 4 to perform the following tasks on the trakt.tv website:

- Open the website using a Chrome browser with a custom profile
- Search for a movie title on Google and click on the first link
- Click on the heart icon to rate the movie based on a given value and a locator
- Read a CSV file with movie titles and add them to the history on trakt.tv

## Requirements

To run this code, you need to have the following:

- Python 3.6 or higher
- Selenium 4.0.0 or higher
- ChromeDriver 94.0.4606.61 or higher
- pandas 1.3.3 or higher

You also need to have a valid account on trakt.tv and a custom Chrome profile with your login credentials saved.

## How to run

To run this code, follow these steps:

1. Download or clone this repository to your local machine.
2. Open a terminal or command prompt and navigate to the folder where the code is located.
3. Install the required packages using `pip install -r requirements.txt`
4. Edit the code to change the following variables according to your preferences:
    - `options.add_argument("--user-data-dir=C:\\Temp\\ChromeProfile")`: Change the path to your custom Chrome profile folder.
    - `df = pd.read_csv(r"C:\Users\saket\Downloads\movielens-ratings.csv")`: Change the path to your CSV file with movie titles and ratings.
    - `click_heart(driver, value, locator)`: Change the value and locator parameters to rate the movie. The value should be between 1 and 10, and the locator should be one of: id, xpath, css selector, link text, partial link text, class name.
5. Run the code using `python selenium_automation.py`
6. Wait for the code to finish and check the results on trakt.tv.

## Notes

- This code is for demonstration purposes only and may not work for all cases or scenarios.
- This code does not handle any errors or exceptions that may occur during execution.
- This code does not use any best practices or coding standards for Selenium automation.
- This code may violate the terms of service of trakt.tv or Google and may result in account suspension or termination. Use it at your own risk.
