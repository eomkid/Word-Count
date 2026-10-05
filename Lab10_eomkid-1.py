"""Program: Word Counter
Author: Brandon Barrett
Description: This program counters the words from preselected txt files
Date: October 8, 2026"""

import string
from pathlib import Path
"""These modules will be used in mainpulating the text present in the files, 
    into manipulatable string for the program to analyze"""


class WordAnalyzer:
    """This class will be used to read txt files and determine words counts of them"""

    def __init__(self, filepath: str):
        """Initizes the WordAnalyzer and provides it with a Path object to store filepath strings.
        Also constains a dictionary for storing word frequences"""
        self.__filepath = Path(filepath)
        self.__word_frequencies = {}

    def process_file(self):
        """Reads the txt files, removes punctuations using a translation table.
        Also tracks word frequency.
        Additionally returns True if the process passes and False if there is some kind of error
        while attempting to read or find the file. """
        if not self.__filepath.exists():
            print(f"Error: The file {self.__filepath} doesn't exist")
            return False

        additional_punctions = string.punctuation + "“”‘’"
        translation_table = str.maketrans('', '', additional_punctions)

        try:
            with self.__filepath.open("r", encoding="utf-8") as file:
                for lines in file:
                    strip_line = lines.translate(translation_table).lower()
                    words = strip_line.split()

                    for word in words:
                        self.__word_frequencies[word] = self.__word_frequencies.get(
                            word, 0) + 1
            return True

        except FileNotFoundError:
            print(f"Error: The file {self.__filepath} couldn't be found.")
            return False

    def print_report(self):
        """Prints the sorted word and their frequencies in the following format:
        \nword :: frequency """
        sorted_words = sorted(self.__word_frequencies.keys())
        for words in sorted_words:
            print(f"{words:<11}  ::  {self.__word_frequencies[words]}")


def main():
    file_menu = {
        "1": {"file": "The Count of Monte Cristo", "path": Path("monte_cristo.txt")},
        "2": {"file": "A Princess of Mars", "path": Path("princess_mars.txt")},
        "3": {"file": "Tarzan of the Apes", "path": Path("Tarzan.txt")},
        "4": {"file": "Treasure Island", "path": Path("treasure_island.txt")}
    }

    while True:
        print("\nWord Analyzer")
        print("What file would you like to analyze today:")
        for num, txt in file_menu.items():
            print(f"{num}. {txt['file']}")
        print("5. Exit")

        user_input = input("Please enter a number 1-5: ").strip()

        if user_input == "5":
            print("Another time then, bye bye")
            break

        if user_input in file_menu:
            selected_file = file_menu[user_input]
            print(f"\n Analyzing File: {selected_file['path'].name}...\n")

            analyzer_bot = WordAnalyzer(str(selected_file['path']))
            if analyzer_bot.process_file():
                analyzer_bot.print_report()

            input("\n Presss Enter to return to file selection.")
        else:
            print(
                "Your choice is invalid. Please enter a positive whole number from 1-5.")
            input("Presss Enter to return to file selection.")


if __name__ == "__main__":
    main()
