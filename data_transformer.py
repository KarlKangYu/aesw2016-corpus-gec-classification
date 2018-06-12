import codecs
import sys

def data_transforming(datafile_in, datafile_out_wrong, datafile_out_right):
    with codecs.open(datafile_in, 'r') as f1:
        with codecs.open(datafile_out_wrong, 'w') as f2:
            with codecs.open(datafile_out_right, 'w') as f3:
                for line in f1.readlines():
                    line = line.strip()
                    wrong, right = line.split('\t')
                    f2.write(wrong + '\n')
                    f3.write(right + '\n')


if __name__ == '__main__':
    args = sys.argv

    datafile_in = args[1]
    datafile_out_wrong = args[2]
    datafile_out_right = args[3]
    data_transforming(datafile_in, datafile_out_wrong, datafile_out_right)
