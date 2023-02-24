def main():
    from connection_to_ftp_server import set_up_ftp_tls_server_connection
    from path_mdb_file import get_mdb_path
    from path_cvs_file import get_cvs_path
    # import schedule
    from dialog_window import creating_a_dialog_box
    import pyodbc
    import csv
    from datetime import datetime
    mdb_file = get_mdb_path()
    # Call to the dialog box
    result = creating_a_dialog_box()

    if result is True or type(result) == str:
        # Connect to the database

        conn_str = (
            r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
            f"DBQ={mdb_file};"
        )
        print(conn_str)
        conn = pyodbc.connect(conn_str)

        cursor = conn.cursor()

        # Added new select request for table manifect column Date = today
        today = datetime.today().date().strftime("%d-%m-20%y")
        # print(today)
        if len(result) > 0:
            sql = f"SELECT * FROM Test WHERE FORMAT(Date, 'dd-mm-yyyy') = '{result}'"
        else:
            sql = f"SELECT * FROM Test WHERE FORMAT(Date, 'dd-mm-yyyy') = '{today}'"

        print(sql)

        # Extract the data from the table
        print(cursor.execute(sql))
        cursor.execute(sql)
        rows = cursor.fetchall()

        # get current date and time
        current_datetime = datetime.now().strftime("%m-%d-%y")

        # Save the data to a CSV file
        csv_file = get_cvs_path(current_datetime)
        print(csv_file)
        with open(csv_file, "w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([i[0] for i in cursor.description])  # write headers
            writer.writerows(rows)

        print("Table exported to CSV successfully")

        # Set up the connection to the FTP_TLS server
        set_up_ftp_tls_server_connection(
            current_datetime=current_datetime,
            csv_file=csv_file
        )
        conn.close()
    else:
        print("Cancel")


if __name__ == "__main__":
    main()
