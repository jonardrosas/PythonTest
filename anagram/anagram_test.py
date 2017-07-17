
def isAnagram(str1, str2):
    str1_list = list(str1)
    str1_list.sort()
    str2_list = list(str2)
    str2_list.sort()
    return (str1_list == str2_list)

def anagrams(word):
    words = [w.rstrip() for w in open('WORD.LST')]
    for o_word in words:
        if isAnagram(o_word, word):
            return o_word


if __name__ == "__main__":
    print (anagrams('train'))
