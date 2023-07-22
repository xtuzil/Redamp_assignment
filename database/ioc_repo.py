import psycopg2


def insert_source(conn: psycopg2.extensions.connection, source: str) -> None:
    """
    Insert a source into the database
    """
    cur = conn.cursor()
    try:
        cur.execute(
            """
          INSERT INTO sources (name) VALUES
          (%s)
          """,
            (source,),
        )
        conn.commit()
    except psycopg2.Error as error:
        print(f"Error when inserting source {source}")
        conn.rollback()
    except Exception as error:
        print(f"General Error: {error}")
        conn.rollback()


def get_source_id(conn: psycopg2.extensions.connection, source: str) -> int:
    """
    Get the id of a source or None if it doesn't exist
    """
    cur = conn.cursor()
    cur.execute(
        """
        SELECT id FROM sources WHERE name = %s
        """,
        (source,),
    )
    res = cur.fetchone()
    if not res:
        return None
    return res[0]


def insert_ioc(
    conn: psycopg2.extensions.connection, ioc: str, source_id: int, is_url: bool = True
) -> None:
    """
    Insert an IOC into the database. IOC can be a URL or an IP address
    """
    cur = conn.cursor()
    table = "urls" if is_url else "ip_addresses"
    try:
        cur.execute(
            f"""
          INSERT INTO {table} (value, source_id) VALUES
          (%s, %s)
          """,
            (ioc, source_id),
        )
        conn.commit()
    except psycopg2.Error as error:
        print(f"Error when inserting {ioc} into {table}: {error}")
        conn.rollback()
    except Exception as error:
        print(f"General Error: {error}")
        conn.rollback()


def ioc_exist(
    conn: psycopg2.extensions.connection, ioc: str, source_id: int, is_url: bool = True
) -> bool:
    """
    Check if an IOC exists in the database. IOC can be a URL or an IP address
    """

    cur = conn.cursor()
    table = "urls" if is_url else "ip_addresses"
    cur.execute(
        f"""
        SELECT id FROM {table} WHERE value = %s AND source_id = %s
        """,
        (ioc, source_id),
    )
    res = cur.fetchone()
    if not res:
        return False
    return True
