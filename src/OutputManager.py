import os
import csv


def create_output_directory():
    if not os.path.exists('Output'):
        os.mkdir('Output')


class OutputManager:
    # todo have a clobber setting, append, (1), (2) etc.

    output_type = ""

    def __init__(self, output_type):
        self.output_type = output_type

    def insert_delimiters(self, input_list):
        i = 3
        while i < len(input_list):
            input_list.insert(i, '---------------------------------------')
            i += 4
        return input_list

    def add_titles_inline(self, input_list):
        new_list = []
        it = iter(input_list)
        for a, b, c in zip(it, it, it):
            a = 'Song: ' + a
            b = 'Link: ' + b
            c = 'Artist / Video Channel: ' + c
            new_list.append(a)
            new_list.append(b)
            new_list.append(c)
        return new_list

    def output_to_terminal(self, input_list):
        new_list = self.add_titles_inline(input_list)
        new_list = self.insert_delimiters(new_list)
        for item in new_list:
            print(item)

    def output_to_txt(self, input_list):
        self.create_output_directory()
        new_list = self.add_titles_inline(input_list)
        new_list = self.insert_delimiters(new_list)
        f = open("Output/MySongs.txt", "w+")
        for item in new_list:
            f.write(item + '\n')
        f.close()

    def output_to_csv(self, input_list):
        self.create_output_directory()
        it = iter(input_list)
        with open('Output/MySongs.csv', 'w+') as csvfile:
            file_writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow(['Song', 'Link', 'Artist'])
            for a, b, c in zip(it, it, it):
                file_writer.writerow([a, b, c])

