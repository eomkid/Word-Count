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
        self.__frequencies = {}
