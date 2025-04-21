import seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Declare which site to scrape
webpage_response = requests.get("https://content.codecademy.com/courses/beautifulsoup/cacao/index.html")
webpage = webpage_response.content

# Set up BS with the webpage
soup = BeautifulSoup(webpage, "html.parser")

# Find and set the target data in the dataset to a variable in the code (i.e., Chocolate rating)
chocolate_ratings = soup.find_all(attrs={"Rating"})

# Find and set the target data in the dataset to a variable in the code (i.e., Chocolate rating, company)
company_names = soup.find_all(attrs={"Company"})

# Example Element: <td class="CocoaPercent">Cocoa Percent</td>
# Find and set the target data in the dataset to a variable in the code (i.e., Chocolate rating, company)
cocoa_percents = soup.find_all(attrs={"CocoaPercent"})

def extract_data(elements, header_text, cleaning_func=lambda x: x.strip()):
    data = []
    for element in elements:
        text = element.get_text()
        if header_text in text:
            continue
        data.append(cleaning_func(text))
    return data

# Example usage:
# Extract ratings (without needing extra cleaning function)
ratings = [float(value) for value in extract_data(chocolate_ratings, "Rating")]

# Extract company names
companies = extract_data(company_names, "Company")

# Extract cocoa percentages with custom cleaning to remove "%"
cleaning = lambda text: float(text.replace("%", "").strip())
percentages = [cleaning(text) for text in extract_data(cocoa_percents, "Cocoa\n               Percent\n            ", lambda x: x)]

# Set up columns for a dataframe by stating the column title and then the corresponding data list
d = {"Company": companies, "Rating": ratings, "Percentage": percentages}

# Construct the dataframe and assign it to a variable
chocolate_df = pd.DataFrame.from_dict(d)

print(chocolate_df)

# Let's group the dataframe by the company names (i.e., Ocelot had 13 rows)
# And then use the Rating column name to take the mean rating for the # of rows for each company
mean_ratings = chocolate_df.groupby("Company").Rating.mean()

# Take the previous output and sort it by the X largest values
ten_best = mean_ratings.nlargest(10)
print(ten_best)
print("-----------------")
ten_worst = mean_ratings.nsmallest(10)
print(ten_worst)

# Plot the Cocoa Percentages on the X-axis and Ratings on the Y-axis
plt.scatter(chocolate_df.Percentage, chocolate_df.Rating)
plt.show()

z = np.polyfit(chocolate_df.Percentage, chocolate_df.Rating, 1)
line_function = np.poly1d(z)
plt.plot(chocolate_df.Percentage, line_function(chocolate_df.Percentage), "r--")

# Create a list to hold cocoa percentage, country, and rating data
chocolate_data = []

# Find and extract relevant data for cocoa percentages, countries, and ratings
cocoa_percents = soup.find_all(attrs={"CocoaPercent"})
countries = soup.find_all(attrs={"CompanyLocation"})  # Replace with the actual attribute used in the web page
ratings = soup.find_all(attrs={"Rating"})  # Replace with the actual attribute used in the web page

# Loop through the items and extract data
for percent, country, rating in zip(cocoa_percents, countries, ratings):
    
    # Skip the header
    if "Cocoa\n               Percent\n            " in percent.get_text():  
        continue  # Skip the rest of this loop iteration
    
    # Strip '%' and convert to float for the cocoa percentage
    clean_percent = percent.get_text().replace('%', '').strip()
    cocoa_percentage = float(clean_percent)
    
    # Extract country name and rating
    country_name = country.get_text().strip()
    chocolate_rating = float(rating.get_text().strip())  # Assuming ratings are numerical

    # Append the data as a dictionary to the list for better structure
    chocolate_data.append({
        'cocoa_percentage': cocoa_percentage,
        'country': country_name,
        'rating': chocolate_rating
    })

# Construct the dataframe and assign it to a variable
chocolate_df = pd.DataFrame.from_dict(chocolate_data)

print(chocolate_df)

# Let's group the dataframe by the country names (i.e., Ocelot had 13 rows)
# And then use the Rating column name to take the mean rating for the # of rows for each company
mean_ratings = chocolate_df.groupby("country").rating.mean()

# Take the previous output and sort it by the X largest and smallest values to get top 10 and worst 10 list
ten_best = mean_ratings.nlargest(10)
print(ten_best)
print("-----------------")
ten_worst = mean_ratings.nsmallest(10)
print(ten_worst)

# Let's group the dataframe by the country names
# And then use the cocoa percentage column name to take the mean cocoa percentage for the # of rows for each country
mean_cocoa_percentage = chocolate_df.groupby("country").cocoa_percentage.mean()

# Take the previous output and sort it by the X largest and smallest values to get top 10 and worst 10 list
ten_best = mean_cocoa_percentage.nlargest(10)
print(ten_best)
print("-----------------")
ten_worst = mean_cocoa_percentage.nsmallest(10)
print(ten_worst)