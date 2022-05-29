def find_anagram(word, anagram):
    S1 = 'Debit Card'
    S2 = 'Bad Credit'
    S1_ana = sorted(S1)
    S2_ana = sorted(S2)
    if len(S1_ana) == len(S2_ana):
        print(True)
    else:
        print(False)

find_anagram ('Debit Card', 'Bad Credit')