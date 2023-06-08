# Description

The PMCSearcher will communicate with the PubMed database using the PubMedClient, perform the search, and retrieve the abstracts for the specified query and parameters.

# Setup

1) setup virual env - python3 -m venv .venv    
2) activate - source .venv/bin/activate
3) install dependencies - pip3 install -r requirements.txt
4) start application - python3 main.py

# Usage

Once the appliction is running by executing the main.py script: python main.py. The program will display a welcome message and prompt you to enter a search query.

Enter the search query or 'q' to quit to retrieve articles on the desired topic. Question you will be asked:

- enter search keyword e.x: covid
- enter max # of results (defaults to 40) e.x: 100
- enter start_date (optional) e.x: 2020-01-01
- enter end_date (optional) e.x: 2023-01-01

The retrieved abstracts will be saved to a CSV file in the current directory. The file name will be generated based on the search query and parameters, following the format: {query}_{start_date}_{end_date}_abstracts.csv.

Once the process is complete, the program will display a message indicating the location where the abstracts CSV file has been saved.

# Architecture


The PMCSearcher tool is designed using a modular architecture, consisting of the following components:

## PubMedClient: 
This component handles the interaction with the PubMed database. It is responsible for performing search queries and fetching detailed information about articles based on their PubMed IDs (PMIDs). The PubMedClient uses the NCBI E-Utilities API for communication with PubMed.
## PMCSearcher: 
This component encapsulates the functionality related to searching for articles and generating the CSV file. It relies on the PubMedClient to perform search queries and retrieve article details. The PMCSearcher class provides methods to search for abstracts based on user-defined parameters (query, max number of records, start date, and end date), and to write the retrieved abstracts to a CSV file.
## CommandLineInterface: 
This component provides a command-line interface for users to interact with the PMCSearcher tool. It handles user input, such as the search query and search parameters, and communicates with the PMCSearcher to execute the search and generate the CSV file. The CommandLineInterface class runs a loop that continuously prompts the user for input until they choose to quit.



# Areas of Improvement Given Time

1) There are lots of string in the CommandLineInterface and PMSearcher would be better to bring that in from a properties file.
2) The logging currently happend in command line, instead a log file would be better. can store in s3 or other places with deploying.
3) Enabling the user to gracefully quit mid way in search and reset the values would be a good feature to enable for User experince. 

