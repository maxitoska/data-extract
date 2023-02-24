import os
import sys


def get_cvs_path(current_datetime):
    # Get the directory of the script file
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Add the directory to the system path so that you can import modules from it
    sys.path.append(script_dir)

    # Use the directory to construct the path to your CSV file
    return (
        os.path.join(
            script_dir,
            f"_Test_{current_datetime}.csv"
        ).replace("\\", "\\\\")
    )
