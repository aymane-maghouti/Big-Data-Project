import happybase

def decode_dict(d):
    return {k.decode('utf-8').split(':', 1)[1]: v.decode('utf-8') for k, v in d.items()}

def get_last_record_from_hbase():
    # Establish a connection to HBase
    connection = happybase.Connection('localhost')  # Assuming HBase is running locally
    connection.open()

    # Open the 'smartphone' table
    table = connection.table('smartphone')

    # Initialize the scanner
    scanner = table.scan(limit=1, reverse=True)

    # Get the last record
    last_record = {}
    try:
        for key, data in scanner:
            last_record = decode_dict(data)
            break  # Exit the loop after fetching the first (last) record
    finally:
        # Close the scanner
        scanner.close()

    # Close the connection
    connection.close()

    return last_record


