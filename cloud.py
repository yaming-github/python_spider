from os import path
from collections import Counter
import jieba
from wordcloud import WordCloud

d = path.dirname(__file__)

def get_words_frequency():
    list = []
    file = open(path.join(d, 'comment.txt')).read()
    arr = jieba.lcut(file)
    for word in arr:
        if len(word) > 1:
            list.append(word)
    words_dict = dict(Counter(list))
    return words_dict

def get_wordcloud(w_dict):
    wc = WordCloud(
        font_path = path.join(d, 'STHeitiLight.ttc'),
        background_color = 'white',
        scale = 3)
    wc.generate_from_frequencies(w_dict)
    wc.to_file('word_cloud.jpg')

if __name__ == '__main__':
    w_dict = get_words_frequency()
    # print(sorted(w_dict.items(), key = lambda kv:kv[1], reverse = True))
    get_wordcloud(w_dict)
