import re
import zipfile


class Manager:

    @staticmethod
    def gif_print(location: str):
        regex = r'\w+.*\.sportszone\.[a-z]{3}.*\.gif.*'
        count = 0
        with open(location) as file:
            lines = file.readlines()
            for line in lines:
                find = re.search(regex, line)
                if find is not None:
                    print(find.group())
                    count += 1
        print(f"Gif matches: {count}")



            #with zip_file.open(file) as file:
             #   for lines in file:
              #      read_lines = file.readlines()
               # for line in read_lines:
                #    regex_match = re.search(regex, line)
                 #   if regex_match is not None:
                  #      print(line)
                   #     counter += 1

        #print(f"Number of matched gifs: {counter}")
