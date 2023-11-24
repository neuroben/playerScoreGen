import random
import csv
class FileUtil:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_to_file(self, content):
        with open(self.file_name, 'w', newline='') as file:
            # deciding to write to .csv or .txt
            if self.file_name.endswith(".csv"):
                writer = csv.writer(file)
                writer.writerows(content)
            elif self.file_name.endswith(".txt"):
                file.writelines("\n".join(content))
    def read_from_file(self):
        with open(self.file_name, 'r') as file:
            content = file.read().splitlines()
        return content

    def generate_random_players(self, name_count, max_score):
        # importing names
        file_util_in = FileUtil(self.file_name)
        file_content = file_util_in.read_from_file()

        # deleting the unnecessary names
        file_content = file_content[:name_count]

        generated = []

        # generating random scores
        for name in file_content:
            score = random.randrange(0, max_score + 1, 1)
            generated.append([name, str(score)])

        # exporting into .csv
        file_util_out = FileUtil('players.csv')
        file_util_out.write_to_file(generated)


class Main:
    def __init__(self):
        max_player = 1000;

        player_count = int(input(f"How many players do you want to generate? (max {max_player})\n"))
        # ensuring max players
        player_count = min(player_count, max_player)

        max_score = int(input("What is the max score a player can achieve?\n"))

        file_util = FileUtil('names.txt')

        file_util.generate_random_players(player_count, max_score)

# avoiding excetuion when a module is imprted
if __name__ == "__main__":
    main_instance = Main()

