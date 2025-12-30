import sys
import urllib3
import pdb
import json
import argparse

class LogAnalyzer:
    
    def __init__(self,input_file,output_file,log_level):
        self.input_file=input_file
        self.output_file=output_file
        self.log_level=log_level.upper() if log_level else None
        self.log_count={
            "INFO":0,
            "WARNING":0,
            "ERROR":0
        }


    def analyze_log(self):
        try:
            with open(self.input_file, 'r') as file:
                for line in file:
                    for level in self.log_count.keys():
                        if level in line:
                            self.log_count[level]+=1
            return True

        except Exception as e:
            print(f"An exception error occured: {e}")
            return False

    def summary_data(self):
        print(f"\n--- Log Analysis Summary ---")
        if self.log_level:
            count = self.log_count.get(self.log_level, 0)
            print(f"{self.log_level}: {count}")
        else:
            for key, value in self.log_count.items():
                print(f"{key}: {value}")

    def save_summary(self):
        if not self.output_file:
            print("\n No output file specified. Skipping save.")
            return
        data_to_save = self.log_count
        if self.log_level:
            data_to_save = {self.log_level: self.log_count.get(self.log_level, 0)}

        try:
            with open(self.output_file, 'w') as file:
                json.dump(data_to_save, file, indent=4)
            print(f"\n Summary saved to: {self.output_file}")
        except Exception as e:
            print(f"Failed to save summary: {e}")


def main():
    parser=argparse.ArgumentParser(description="CLI Tool")

    parser.add_argument("--file", required=True, help="Enter the file name or path eg: app.log")
    parser.add_argument("--out", help="ENter the output file name eg: log_summary.txt")
    parser.add_argument("--level", help="Enter the log level filter to check eg: INFO , WARNING, ERROR ")

    args=parser.parse_args()

    analyzer=LogAnalyzer(args.file,args.out,args.level)

    if analyzer.analyze_log():
        analyzer.summary_data()
        analyzer.save_summary()

if __name__ == "__main__":
    main()