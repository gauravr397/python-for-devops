import sys
import urllib3
import pdb
import os

input_file_path="app.log"

def analyze_log():
    """
    Reads the log file and counts occurrences of INFO, WARNING, and ERROR.
    Returns None if the file does not exist.
    """
    if not os.path.exists(input_file_path):
        return None

    log_count={
        "INFO":0,
        "WARNING":0,
        "ERROR":0
    }

    try:
        with open(input_file_path, 'r') as file:
            for line in file:
                if "INFO" in line:
                    log_count["INFO"]+=1
                elif "WARNING" in line:
                    log_count["WARNING"]+=1
                elif "ERROR" in line:
                    log_count["ERROR"]+=1
                else:
                    pass
                
        return {
            "FileName":input_file_path,
            "summary":log_count
        }

    except Exception as e:
        print(f"An exception error occured: {e}")
        return None