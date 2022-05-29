word = 'Debit Card'
anagram = 'Bad Credit'

def find_anagram(word,anagram):
    # no need redefining s1 and s2, just use 
    sorted_word:list = sorted(word)
    sorted_anagram:list = sorted(anagram)
    result:bool = sorted_word == sorted_anagram
    # the comparison already gives you the result
    print(result)
    find_anagram(word, anagram)
    return result
    find_anagram(word, anagram)