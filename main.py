import os

from manager import Manager


def main():

    file = "con267.tweetie.799608879"
    file_location = os.path.abspath(file)

    Manager.gif_print(location=file_location)


if __name__ == '__main__':
    main()

