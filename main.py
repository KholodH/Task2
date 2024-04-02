import requests
from bs4 import BeautifulSoup
import csv

try:
    # Send a GET request to the Wikipedia page
    url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if the request was not successful

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table that contains the population data
    table = soup.find('table', class_='wikitable')

    # Extract the table headers
    headers = [header.get_text(strip=True) for header in table.find_all('th')]

    # Extract the table rows
    rows = []
    for row in table.find_all('tr'):
        cells = [cell.get_text(strip=True) for cell in row.find_all('td')]
        if cells:
            rows.append(cells)

    # Store the extracted data in a CSV file
    filename = 'population_data.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(rows)

    print("Data has been scraped and stored in", filename)

except requests.exceptions.RequestException as e:
    print("Error occurred during the request:", str(e))

except Exception as e:
    print("An error occurred:", str(e))