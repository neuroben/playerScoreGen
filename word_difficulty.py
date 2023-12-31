from score_gen import FileUtil

in_words = FileUtil("wordList.txt")

words = in_words.read_from_file()

easy = []
medium = []
hard = []

for line in words:
    if 3 <= len(line) < 5:
        easy.append(line)
    elif 5 <= len(line) < 8:
        medium.append(line)
    elif 8 <= len(line) < 13:
        hard.append(line)

FileUtil("easy.txt").write_to_file(easy)

FileUtil("medium.txt").write_to_file(medium)

FileUtil("hard.txt").write_to_file(hard)