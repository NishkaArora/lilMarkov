# lilmarkov

from collections import defaultdict
import random
import re
import pickle
sylList = [7, 7, 7, 5, 5, 5, 14]
"""
def clean_text(inp):
    inp = re.sub("[\(\[].*?[\)\]]", "", inp)  # remove stuff that is in brackets
    inp = re.sub('[^ a-zA-Z0-9]', '', inp)  # remove special characters
    inp = re.sub("\s\s+", " ", inp)  # remove extra spaces
    return inp

def markov_chain(text):
    words = text.split(' ')  # tokenise the word

    m_dict = defaultdict(list)  # create a default dictionary
    for cur_word, next_word in zip(words[0:-1], words[1:]):  # since w[0:-1] is all the words and w[1:] is all the words except starting from the second word you end up with all word pairs because the first word w[0] goes to the second w[1], and w[1] goes to w[2], the last element of w[1:] is left unpaired except with the second last word from the previous iteration
        m_dict[cur_word].append(next_word)  # appending it to the list (aka the value of the dict) corresponding to each word (aka key of the dict)

    m_dict = dict(m_dict)  # converting default dict back into a dict
    return m_dict

with open('hiphop_lyrics.txt', 'r') as file:
    data = file.read().replace('\n', ' ')

inp = data
inp = clean_text(inp)
states = markov_chain(inp)
"""


def countSyl(word):
    count = 0
    for i in range(len(word)):
        if isVowel(word[i]) and (True if i < 1 else not(isVowel(word[i - 1]))):
            if word[i] == 'e' and i == len(word) - 1 and countVowels(word) > 1:
                break
            count += 1
    return count


def isVowel(letter):
    return letter in 'aAeEiIoOuUyY'


def countVowels(str):
    c = 0
    for x in str:
        if x in 'aAeEiIoOuUyY':
            c += 1
    return c


def generate(state_list, count):
    w1 = random.choice(list(state_list.keys()))
    sent = w1
    syl = countSyl(sent)
    while syl < count:
        w2 = random.choice(state_list[w1])
        w1 = w2
        syl += countSyl(w2)
        sent += ' ' + w2
    return sent


with open('hiphop_states.p', 'rb') as pfile:
    states = pickle.load(pfile)

print(generate(states, 8))

song = ''

for i in sylList:
    song += generate(states, i) + '\n'

print(song)
