import re

#taken from http://stackoverflow.com/questions/5319922/python-check-if-word-is-in-a-string

def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search


def findAllMatches(word_list, desc):
    '''
    Takes in a word list and description and returns a filtered list with all the matching words
    '''
    filtered_list = []
    for word in word_list:
        match_obj = None
        try:
            match_obj = findWholeWord(word)(desc)
        except:
            pass
        if match_obj:
            filtered_list.append(match_obj.group(0))
    return filtered_list