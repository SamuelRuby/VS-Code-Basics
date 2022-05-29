def is_anagram(w1:str, w2:str) -> bool:
    w1 = w1.lower()
    w2 = w2.lower()
    if len(w1) == len(w2):
        for x in w1:
            w2 = w2.replace(x,'')
        print(w2, len(w2), ' result')
        if not len(w2):
            return True
    return False
w1 = 'mart'
w2 = 'tarm'
print(is_anagram(w1,w2))