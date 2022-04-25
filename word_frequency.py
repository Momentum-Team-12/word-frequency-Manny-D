from pydoc import Doc


STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file, 'r') as f:
        file_string = f.read()
        file_list = file_string.splitlines()
    for line in file_list:   
        lower_case_list = line.lower()

        import string

        no_punct = lower_case_list.translate(str.maketrans('', '', string.punctuation))

        a = no_punct.split()

        stop_filtered = [word for word in a if word not in STOP_WORDS]
        result = ' '.join(stop_filtered)
        
        filtered = result.split()

        # List word with count with # and *
        from collections import Counter

        word_count = Counter(filtered)
        # doc = [result]

        # count = dict(Counter(word for sentence in doc for word in sentence.split())) # is counting per sentence
        #count = dict(Counter(word for word in doc))
        #print(count)

        print(word_count.most_common())






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
