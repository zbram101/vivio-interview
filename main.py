import datetime
from pmSearcher import PMSearcher 
from pubMedClient import PubMedClient

class CommandLineInterface:
    def __init__(self, pmc_searcher):
        self.pmc_searcher = pmc_searcher

    def run(self):
        while True:
            print("Welcome to the PMCSearcher where you can search for articles on a topic")
            query = input("Enter search keyword (e.g: covid or 'q' to quit): ")

            if query.lower() == "q":
                break

            max_records = input("Enter max number of records [optional]: ")
            start_date = input("Enter start date (YYYY-MM-DD) [optional]: ")
            end_date = input("Enter end date (YYYY-MM-DD) [optional]: ")

            try:
                max_records = int(max_records) if max_records else None
            except ValueError:
                print("Invalid input for max number of records. Please enter an integer.")
                continue

            try:
                start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d") if start_date else None
                end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d") if end_date else None
            except ValueError:
                print("Invalid date format. Please enter dates in the format YYYY-MM-DD.")
                continue

            self.pmc_searcher.csv_from_articles(query, max_records, start_date, end_date)


def main():
    pubmed_client = PubMedClient()
    pmc_searcher = PMSearcher(pubmed_client)
    cli = CommandLineInterface(pmc_searcher)
    cli.run()


if __name__ == "__main__":
    main()