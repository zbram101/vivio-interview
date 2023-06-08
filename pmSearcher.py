import requests
import csv


class PMSearcher:
    def __init__(self, pubmed_client):
        self.pubmed_client = pubmed_client

    def csv_from_articles(self, query, max_records=50, start_date=None, end_date=None):
        try:
            pmids = self.pubmed_client.search_abstracts(query, max_records, start_date, end_date)
            csv_file = self._generate_csv_filename(query, start_date, end_date)
            self.write_abstracts_to_csv(pmids, csv_file)
            print(f"Abstracts saved to {csv_file}")

        except (requests.RequestException, Exception) as e:
            print("An error occurred during data retrieval:", str(e))

    def write_abstracts_to_csv(self, pmids, csv_file):
        field_names = ["Title", "PMID", "Abstract", "Abstract URL"]

        with open(csv_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()

            total_pmids = len(pmids)
            processed_pmids = 0

            print(f"File: {csv_file} is being populated")

            for pmid in pmids:
                abstract = self.pubmed_client.fetch_abstract_detail(pmid)
                writer.writerow(abstract)

                processed_pmids += 1

                if processed_pmids % 10 == 0:
                    print(f"Processed {processed_pmids}/{total_pmids} PMIDs")

        print(f"Data saved to {csv_file} completed")

    def _generate_csv_filename(self, query, start_date, end_date):
        query = query.replace(" ", "_")
        start_date_str = start_date.strftime("%Y-%m-%d") if start_date else ""
        end_date_str = end_date.strftime("%Y-%m-%d") if end_date else ""
        csv_file = f"{query}_{start_date_str}_{end_date_str}_abstracts.csv"
        return csv_file
