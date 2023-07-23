import psycopg2
import requests
from database.ioc_repo import get_source_id, insert_ioc, insert_source, ioc_exist
from ioc_parser.utils import is_ip_address, strip_ioc


class IOCParser:
    """
    Class for parsing IOCs from a source
    """

    def __init__(
        self,
        source: str,
        delimiter: str,
        ioc_index: int,
        conn: psycopg2.extensions.connection,
    ) -> None:
        self.source = source
        self.delimiter = delimiter
        self.ioc_index = ioc_index
        self.conn = conn

    def fetch_content(self) -> str | None:
        """
        Fetch content from a url
        """
        try:
            response = requests.get(self.source)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {self.source}: {e}")
            return None

    def process_content(
        self,
        content: str,
    ) -> dict[list[str], list[str]]:
        """
        Process content and return a dict with array of urls and ip addresses
        """
        lines = content.split("\n")
        urls = []
        ip_addressses = []
        for line in lines:
            parts = [line]
            if not (self.delimiter == ""):
                parts = line.split(self.delimiter)

            if len(parts) <= self.ioc_index:
                print(f"Can't get index {self.ioc_index} on line: {line}")
                continue

            ioc = parts[self.ioc_index]

            if ioc == "":
                continue

            if is_ip_address(ioc):
                ip_addressses.append(ioc)
            else:
                # check if url is valid based on provided conditions
                urls.append(ioc)

        return {"urls": urls, "ip_addresses": ip_addressses}

    def store_iocs(
        self,
        processed_ioc: dict[list[str], list[str]],
    ) -> None:
        """
        Store processed IOCs in the database
        """
        urls = processed_ioc["urls"]
        ip_addresses = processed_ioc["ip_addresses"]

        if len(urls) > 0 or len(ip_addresses) > 0:
            source_id = get_source_id(self.conn, self.source)

            if source_id is None:
                insert_source(self.conn, self.source)
                source_id = get_source_id(self.conn, self.source)

            inserted_urls_count = 0
            for url in urls:
                url = strip_ioc(url)

                if not ioc_exist(self.conn, url, source_id):
                    insert_ioc(self.conn, url, source_id, is_url=True)
                    inserted_urls_count += 1

            inserted_ip_addresses_count = 0
            for ip_address in ip_addresses:
                ip_address = strip_ioc(ip_address)
                if not ioc_exist(self.conn, ip_address, source_id, is_url=False):
                    insert_ioc(self.conn, ip_address, source_id, is_url=False)
                    inserted_ip_addresses_count += 1

            print(
                f"Inserted {inserted_urls_count} urls ({len(urls) - inserted_urls_count} already exist)."
            )
            print(
                f"Inserted {inserted_ip_addresses_count} ip addresses ({len(ip_addresses) - inserted_ip_addresses_count} already exist)."
            )

        else:
            print("No IOCs found in provided source")

    def run(self) -> None:
        """
        Main function for running the parser
        """
        content = self.fetch_content()
        if not content:
            print("Content is empty")
            return

        processed_ioc = self.process_content(content)
        self.store_iocs(processed_ioc)
