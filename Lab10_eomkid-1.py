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

        translation_table = str.maketrans(", ", string.punctuation)

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
