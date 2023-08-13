# -*- coding:utf-8 -*-

def merge(sentence: str, max_ngram_length = 4):
    '''n-gram合并文本中连续重复的词'''
    final_merge_sent = sentence
    max_ngram_length = min(max_ngram_length, len(sentence))
    for i in range(max_ngram_length, 0, -1):
        start = 0
        end = len(final_merge_sent) - i + 1
        ngrams = []
        while start < end:
            ngrams.append(final_merge_sent[start: start + i])
            start += 1
        result = []
        for cur_word in ngrams:
            result.append(cur_word)
            if len(result) > i:
                pre_word = result[len(result) - i - 1]
                if pre_word == cur_word:
                    for k in range(i):
                        result.pop()

        cur_merge_sent = ""
        for word in result:
            if not cur_merge_sent:
                cur_merge_sent += word
            else:
                cur_merge_sent += word[-1]
        final_merge_sent = cur_merge_sent

    return final_merge_sent

def replace_last_occurrence(s, old, new):
    """
    Replaces the last occurrence of the substring 'old' in the string 's' with the substring 'new'.
    """
    return s[::-1].replace(old[::-1], new[::-1], 1)[::-1]
    
        
if __name__ == "__main__":
    text = "ほんと よい お 歯触り が .行く ? 行く よ , 行く よ , 行く よ , 行く よ , 行く よ , 行く よ , 行く よ , 行く よ , 行く よ , 行く よ , 行く よ , 行く よ , 行く よ , 行く よ , 行く よ ,ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない な , ない"
    print(merge(text,max_ngram_length = 10))
    
    text = "我爱爱北京天安门天安门，天安门上上太阳太阳升。"
    print(merge(text, max_ngram_length = 4))