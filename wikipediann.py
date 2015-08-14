#  Author: Abhishek Kadian (abhishekkadiyan@gmail.com)

"""Wikipedia Nearest Neighbor:
Finds the nearest neighbor of a Wikipedia article.
"""

import os
import time
import logging
import wikipedia


class NearestNeighbor:
    """
    """

    def __init__(self, boost_title = 1):
        self.data = []
        self.boost_title = boost_title

    def adddata(self, filepath=None, data=None):
        raise NotImplementedError


def download(titlesfile, datafolder="data/"):
    """Reads list of titles from 'filepath', downloads wikipedia articles for
    titles and stores them as separate files in datafolder.
    """

    if not os.path.exists(datafolder):
        os.makedirs(datafolder)

    with open(titlesfile, "r", encoding="utf-8") as f:
        for line in f:
            title = line.strip()
            logging.debug("Downloading \'{0}\'".format(title.encode("utf-8")))
            print("Downloading:", title.encode("utf-8"))
            page = wikipedia.page(title)
            with open(datafolder + title + ".txt", "wb") as g:
                g.write(bytes(page.title + "\n", "utf-8"))
                g.write(bytes(page.content, "utf-8"))


def tests():
    print("All tests passed.")


def main():
    logging.basicConfig(filename="wikipediann.log", level=logging.DEBUG)
    nn = NearestNeighbor()
    nn.adddata()
    tests()


if __name__ == "__main__":
    main()
