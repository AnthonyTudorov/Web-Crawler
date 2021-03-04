from bs4 import BeautifulSoup
import nltk
import re
import os


def clean_title(title):
    invalid_characters = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for c in invalid_characters:
        title.replace(c,'')
    return title


def save_index(index):
    with open('position index.txt', 'w', encoding='utf-8') as f, open('terms.txt', 'w', encoding='utf-8') as t_file:
        term_count = 0
        for term in index:
            try:
                f.write(term + ' => ')
                t_file.write(term + '\n')
            except:
                print("error term: ", term)
            for posting in index[term]:
                for position in index[term][posting]:
                    f.write('(' + str(posting) + ', ' + str(position) + ') ')
            f.write('\n')
            term_count += 1
        print("Total unique terms: " + str(term_count))


def create_frequency_index():
    if not os.path.isdir("pages"):
        print("You need a pages directory in the same directory as this file")
        return
    index = {}
    doc_count = 1
    file_names = os.listdir("pages")
    for f_name in file_names:
        with open("pages/"+f_name, errors='ignore') as file:
            soup = BeautifulSoup(file, 'html.parser')
            print(doc_count, " ", clean_title(soup.title.string))
            text = soup.get_text()
            text = text.lower()
            text = re.sub("\[.*\]", " ", text)
            text = re.sub("[!\"#$%&'()*+\,-.–\—/:;<\=>?@[\]^ `{|}~…′]", " ", text)
            text = text.replace("\\", " ")
            tokens = nltk.word_tokenize(text)
            token_count = 1
            for word in tokens:
                if word in index:
                    if doc_count in index[word]:
                        index[word][doc_count].append(token_count)
                    else:
                        index[word][doc_count] = [token_count]
                else:
                    index[word] = {doc_count: [token_count]}
                token_count += 1
        doc_count += 1
    save_index(index)


create_frequency_index()
