import requests
import xml.etree.ElementTree as ET
import urllib.parse


class PubMedClient:
    def __init__(self):
        self.pubmed_search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
        self.pubmed_summary_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

    def search_abstracts(self, query, max_records, start_date=None, end_date=None):
        search_params = {
            "db": "pubmed",
            "term": query,
            "retmode": "xml",
            "retmax": max_records,
        }

        if start_date:
            search_params["from"] = start_date.strftime("%Y-%m-%d")
        if end_date:
            search_params["until"] = end_date.strftime("%Y-%m-%d")

        response = self._make_request(self.pubmed_search_url, search_params)
        xml_root = ET.fromstring(response.text)

        id_list = xml_root.findall(".//IdList/Id")
        return [id_element.text for id_element in id_list]

    def fetch_abstract_detail(self, pmid):
        summary_params = {
            "db": "pubmed",
            "id": pmid,
            "verb": "ListSets",
            "retmode": "xml"
        }
        summary_response = self._make_request(self.pubmed_summary_url, summary_params)
        summary_xml_root = ET.fromstring(summary_response.text)

        title_element = summary_xml_root.find(".//ArticleTitle")
        title = title_element.text if title_element is not None else "N/A"

        abstract_element = summary_xml_root.find(".//AbstractText")
        abstract = abstract_element.text if abstract_element is not None else "N/A"

        abstract_url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
        clickable_url = urllib.parse.quote(abstract_url, safe=':/')

        return {
            "Title": title,
            "PMID": pmid,
            "Abstract": abstract,
            "Abstract URL": clickable_url
        }

    def _make_request(self, url, params):
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response
