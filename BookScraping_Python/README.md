This Python code is a web scraper designed to extract book data from the "Books to Scrape" website and save it into an Excel file.

Importing Libraries:

requests: Used to send HTTP requests to the website and retrieve its HTML content.
BeautifulSoup from the bs4 library: Used for parsing HTML and navigating the parse tree.
pandas as pd: Used for handling and manipulating data, particularly for creating a DataFrame.
Initialization:

current_page is set to 1 initially to start scraping from the first page.
proceed is set to True to control the loop.

Main Loop:

The code enters a while loop that continues as long as proceed is True.
Inside the loop:
It constructs the URL for the current page using string concatenation.
It sends an HTTP GET request to the URL and retrieves the page content.
It creates a BeautifulSoup object soup to parse the HTML content.
It checks if the title of the page is "404 Not Found". If it is, it sets proceed to False to exit the loop; otherwise, it proceeds with scraping.
It finds all book items on the page using BeautifulSoup's find_all method.
Extracting Book Data:

For each book item found on the page:
It creates a dictionary item to store the book's attributes.
It extracts the book's title, link, price, and stock availability using BeautifulSoup's find method and various HTML attributes.
It appends the item dictionary to the data list.
Printing Progress:

After scraping each page, it prints a message indicating the page number that has been scraped.
DataFrame Creation and Export:

Once all pages have been scraped, it creates a pandas DataFrame df from the data list.
It exports the DataFrame to an Excel file named "books.xlsx" using the to_excel method.
This code essentially automates the process of scraping book data from multiple pages of the website and organizes it into a structured format for further analysis or storage.
