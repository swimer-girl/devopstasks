import argparse
import requests
from lxml import html
import datetime
import boto3


class CountTags:
    def __init__(self, page):
        headers = {"Accept-Language": "En-us"}
        self.page = requests.get(page, headers=headers)

    def parse_html(self):
        parse = html.fromstring(self.page.content)
        all_elems = parse.cssselect('*')
        all_tags = [x.tag for x in all_elems]
        count_each_tag = {elem: all_tags.count(elem) for elem in all_tags}
        print('All tags:', len(all_tags), count_each_tag)

    def log_file(self, log_name):
        self.log_name = log_name
        log_data = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        with open(self.log_name, 'a') as write_file:
            log_string = f"{log_data} {self.page.url} {self.parse_html()}\n"
            write_file.write(log_string)
        file_log = write_file
        return file_log

    def upload_file(self, bucket_name):
        self.bucket_name = bucket_name
        s3 = boto3.resource('s3')
        s3.meta.client.upload_file(self.log_name, self.bucket_name, self.log_name)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Считаем теги на вебстранице')
    parser.add_argument('page', type=str, help='Вводим страницу для которой будет идти подсчет')
    parser.add_argument('-w', type=str, nargs='?', const=f'{parser.prog}.log', help='Запись в файл.',
                        metavar='FILENAME')
    parser.add_argument('-s3', type=str, nargs='?',
                        help='Отправить файл в s3 bucket. Имя s3 бакета указывать обязательно.',
                        metavar='BUCKET_NAME')
    args = parser.parse_args()

    countTags = CountTags(args.page)
    print(countTags.parse_html())
    if args.w and args.s3:
        countTags.log_file(args.w)
        countTags.upload_file(args.s3)
    elif args.w:
        countTags.log_file(args.w)
    elif args.s3:
        countTags.upload_file(args.s3)
