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
        lower_case_list = file_string.lower()

        # Calls string module
        import string 
        # Removes punctuation
        no_punct = lower_case_list.translate(str.maketrans('', '', string.punctuation)) 
        # Makes new list
        lower_nopunct_list = no_punct.split(" ")  
        # Filter out STOP_WORDS
        filtered_stop = [word for word in lower_nopunct_list if word not in STOP_WORDS] 
        result = ' '.join(filtered_stop)
        # Makes new list 
        filtered_list = result.split() 

        # Create empty dictionary to add word : count as key : value pairs
        d = dict() 
        # Start of loop to check each word : count and add to dictionary
        for filter in filtered_list: 
            if filter in d: 
                d[filter] = d[filter] + 1
            else:
                d[filter] = 1 
        # Loop in dictionary to print / janky but working
        for word in list(d.keys()): 
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
