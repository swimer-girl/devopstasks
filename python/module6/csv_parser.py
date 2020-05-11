import csv
import operator


class CsvParser:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_country_profit(self, country):
        self.country = country
        with open(self.file_name, 'r') as file:
            dict = csv.DictReader(file)
            total_profit = 0
            for column in dict:
                if column['Country'] == self.country:
                    total_profit = total_profit + float(column['Total Profit'])
            return round(total_profit, 2)

    def sell_over(self, item_type, threshold):
        self.item_type = str(item_type)
        self.threshold = int(threshold)
        with open(self.file_name, 'r') as file:
            dict = csv.DictReader(file)
            sellers = []
            result = {}
            for column in dict:
                if column['Item Type'] == self.item_type:
                    key = column['Country']
                    if result.get(key) == None:
                        result[key] = int(column['Units Sold'])
                    else:
                        result[key] = int(column['Units Sold'])+int(result[key])
            sort = sorted(result.items(), key=operator.itemgetter(1), reverse=False)
            for key, value in sort:
                if value > threshold:
                    sellers.append(key)
        return sellers

    def save_as(self, new_file_name, delimiter):
        self.new_file_name = new_file_name
        self.delimiter = delimiter
        with open(self.file_name, newline='') as file:
            with open(self.new_file_name, 'w', newline='') as outfile:
                reader = csv.reader(file, delimiter=',')
                writer = csv.writer(outfile, delimiter='\t')
                for row in reader:
                    writer.writerow(row)