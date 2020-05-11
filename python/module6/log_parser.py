import csv
from collections import Counter

class LogParser:
    def __init__(self, log_name):
        self.log_name = log_name

    def get_most_common(self, top):
        self.top = int(top)
        with open(self.log_name, 'r') as file:
            iplist = {}
            for line in file.readlines():
                if line != '\n':
                    ip = line.split()[0]
                    if 6 < len(ip) <= 15:
                        iplist[ip] = iplist.get(ip, 0) + 1
            ipcount = Counter(iplist).most_common(top)
            return ipcount

    def log_by_http_code(self, output_file, code):
        self.output_file = output_file
        self.code = code
        with open(self.log_name, 'r') as file:
            with open(self.output_file, 'w') as out_log:
                for line in file.readlines():
                    if line != '\n':
                        split_line = line.split()[8]
                        if split_line == self.code:
                            csv.writer(out_log).writerow(split_line)
