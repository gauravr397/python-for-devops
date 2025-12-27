import sys
import urllib3
import pdb

def analyze_log(input_file_path):
    # pdb.set_trace()
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
                
        return log_count

    except Exception as e:
        print(f"An exception error occured: {e}")
        return None

def save_summary(count, output_file):
    with open(output_file, 'w') as file:
        file.write("Log file Report")
        for key,value in count.items():
            file.write(f"{key}:{value}\n")

if __name__ == "__main__":
    input_log_file="app.log"
    output_summary_file="log_summary.txt"

    summary_data=analyze_log(input_log_file)

    if summary_data:
        print(f"---SUmmary---")
        for key,value in summary_data.items():
            print(f"{key}:{value}")

        save_summary(summary_data,output_summary_file)