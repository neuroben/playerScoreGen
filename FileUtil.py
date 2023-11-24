"""import random
import csv


class FileUtil:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_to_file(self, content):
        with open(self.file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(content)

    def read_from_file(self):
        with open(self.file_name, 'r') as file:
            content = file.read().splitlines()
        return content

    def generate_random_players(self, name_count, max_score):
        file_util_in = FileUtil(self.file_name)
        file_content = file_util_in.read_from_file()

        file_content = file_content[:name_count]

        generated = []

        for name in file_content:
            score = random.randrange(0, max_score + 1, 1)
            generated.append([name, str(score)])

        file_util_out = FileUtil(r'D:/dev/word-guess/game/names.csv')
        file_util_out.write_to_file(generated)"""