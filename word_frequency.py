from logging import Filterer
from pydoc import Doc
from tracemalloc import start

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file, 'r') as f:
        file_string = f.read()
        #file_list = file_string.splitlines() -> usure why I had this here originally
        lower_case_list = file_string.lower()

        import string # Calls string module
        
        # for line in lower_case_list: -> didn't work / listed words vertically 
        no_punct = lower_case_list.translate(str.maketrans('', '', string.punctuation)) # removes punctuation

        lower_nopunct_list = no_punct.split(" ") # makes new list 

        filtered_stop = [word for word in lower_nopunct_list if word not in STOP_WORDS] # filter out STOP_WORDS
        result = ' '.join(filtered_stop)

        filtered_list = result.split() # makes new list 

        d = dict() # create blank dictionary to add word : count as key : value pairs

        for filter in filtered_list: # start of loop to check each word : count and add to dictionary
            if filter in d: 
                d[filter] = d[filter] + 1
            else:
                d[filter] = 1 


        for word in list(d.keys()): # Loopin dictionary to print / janky but working
            w_count = d[word]
            stars = str("*" * w_count)
            print(word, "|", w_count, stars)


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
