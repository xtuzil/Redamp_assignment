import sys
from database.database import get_connection
from ioc_parser.parser import IOCParser


def print_usage():
    print("Usage: python app.py <url> <delimiter> <ioc_index>")


def check_ioc_index(ioc_index: str) -> int:
    try:
        if int(ioc_index) < 0:
            print("IOC index must be a positive number")
            print_usage()
            sys.exit(1)
    except ValueError:
        print("IOC index must be a number")
        print_usage()
        sys.exit(1)

    return int(ioc_index)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print_usage()
        sys.exit(1)

    source = sys.argv[1]
    delimiter = sys.argv[2]
    ioc_index = check_ioc_index(sys.argv[3])

    conn = get_connection()
    if not conn:
        print("Error connecting to database")
        sys.exit(1)

    parser = IOCParser(source, delimiter, ioc_index, conn)
    parser.run()

    conn.close()
    print("Connection closed")
