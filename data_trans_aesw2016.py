import codecs
import sys

def data_transformer(datain, dataout_right, dataout_wrong, dataout_absolute_right):
    with codecs.open(datain, 'r') as f1:
        with codecs.open(dataout_right, 'w') as fr:
            with codecs.open(dataout_wrong, 'w') as fw:
                with codecs.open(dataout_absolute_right, 'w') as fa:
                    for line in f1.readlines():
                        line = line.strip()
                        label, _, sentence = line.split('\t')
                        sentence = sentence.strip()
                        if label == '1':
                            fr.write(sentence + '\n')
                        if label == '-1':
                            fw.write(sentence + '\n')
                        if label == '0':
                            fa.write(sentence + '\n')

if __name__ == '__main__':
    args = sys.argv

    datain = args[1]
    dataout_right = args[2]
    dataout_wrong = args[3]
    dataout_absolute_right = args[4]
    data_transformer(datain, dataout_right, dataout_wrong, dataout_absolute_right)




