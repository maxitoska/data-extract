import os
import sys


def get_mdb_path():
    # Get the directory of the script file
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Add the directory to the system path so that you can import modules from it
    sys.path.append(script_dir)

    # Use the directory to construct the path to your database file
    print(os.path.join(script_dir, "Database.mdb"))
    return os.path.join(
        script_dir,
        "Database.mdb"
    )
