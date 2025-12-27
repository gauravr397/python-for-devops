import sys
import urllib3
import pdb
import json

class LogAnalyzer:
    
    def __init__(self,input_file,output_file):
        self.input_file=input_file
        self.output_file=output_file
        self.log_count={
            "INFO":0,
            "WARNING":0,
            "ERROR":0
        }


    def analyze_log(self):
        try:
            with open(self.input_file, 'r') as file:
                for line in file:
                    if "INFO" in line:
                        self.log_count["INFO"]+=1
                    elif "WARNING" in line:
                        self.log_count["WARNING"]+=1
                    elif "ERROR" in line:
                        self.log_count["ERROR"]+=1
                    else:
                        pass
            return True

        except Exception as e:
            print(f"An exception error occured: {e}")
            return False

    def summary_data(self):
        print(f"---SUmmary---")
        for key,value in self.log_count.items():
            print(f"{key}:{value}")

    def save_summary(self):
        with open(self.output_file, 'w') as file:
            json.dump(self.log_count,file, indent=4)

if __name__ == "__main__":
    input_log_file="app.log"
    output_summary_file="log_summary.txt"

    analyzer=LogAnalyzer(input_log_file,output_summary_file)

    if analyzer.analyze_log():
        analyzer.summary_data()
        analyzer.save_summary()