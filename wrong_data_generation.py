from data_helpers import clean_str
import codecs
import random
import sys

def generation(datain, dataout, dropout_prob=0.25, replacement_prob=0.25):
    DROPOUT_TOKENS = {"a", "an", "the", "'ll", "'s", "'m", "'ve"}

    REPLACEMENTS = {"there": "their", "their": "there", "then": "than",
                    "than": "then"}
    with codecs.open(datain, 'r') as f1:
        with codecs.open(dataout, 'w') as f2:
            for line in f1.readlines():
                line = line.strip()
                line = clean_str(line)
                line = line.split()
                wrong = []
                for token in line:
                    if token not in DROPOUT_TOKENS and token not in REPLACEMENTS:
                        wrong.append(token)
                        continue
                    # Randomly dropout some words from the input.
                    dropout_token = (token in DROPOUT_TOKENS and
                                     random.random() < dropout_prob)
                    replace_token = (token in REPLACEMENTS and
                                     random.random() < replacement_prob)

                    if replace_token:
                        wrong.append(REPLACEMENTS[token])
                    elif not dropout_token:
                        wrong.append(token)
                if wrong != line:
                    wrong = ' '.join(wrong)
                    f2.write(wrong + '\n')


if __name__ == '__main__':
    args = sys.argv
    datain = args[1]
    dataout = args[2]
    generation(datain, dataout)





