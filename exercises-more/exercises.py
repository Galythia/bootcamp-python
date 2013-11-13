# PROB 1
# Return the number of words in the string s. Words are separated by spaces.
# e.g. num_words("abc def") == 2
def num_words(s):
    words = s.split()
    return len(words)

# PROB 2
# Return the sum of all the numbers in lst. If lst is empty, return 0.
def sum_list(lst):
    if len(lst) == 0:
	return len(lst)
    else:
	return sum(lst)

# PROB 3
# Return True if x is in lst, otherwise return False.
def appears_in_list(x, lst):
    return x in lst

# PROB 4
# Return the number of unique strings in lst.
# e.g. num_unique(["a", "b", "a", "c", "a"]) == 3
def num_unique(lst):
    newLst = list(set(lst))
    return len(newLst)

# PROB 5
# Return a new list, where the contents of the new list are lst in reverse order.
# e.g. reverse_list([3, 2, 1]) == [1, 2, 3]
def reverse_list(lst):
    lst.reverse()
    return lst

# PROB 6
# Return a new list containing the elements of lst in sorted decreasing order.
# e.g. sort_reverse([5, 7, 6, 8]) == [8, 7, 6, 5]
def sort_reverse(lst):
    lst.sort()
    lst.reverse()
    return lst

# PROB 7
# Return a new string containing the same contents of s, but with all the
# vowels (upper and lower case) removed. Vowels do not include 'y'
# e.g. remove_vowels("abcdeABCDE") == "bcdBCD"
def remove_vowels(s):
    for letter in s:
	if letter in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']:
	    s = s.replace(letter, '')
    return s

# PROB 8
# Return the longest word in the lst. If the lst is empty, return None.
# e.g. longest_word(["a", "aaaaaa", "aaa", "aaaa"]) == "aaaaaa"
def longest_word(lst):
    if len(lst) == 0:
	return None
    else:
	word = max(set(lst), key=len)
	return word

# PROB 9
# Return a dictionary, mapping each word to the number of times the word
# appears in lst.
# e.g. word_frequency(["a", "a", "aaa", "b", "b", "b"]) == {"a": 2, "aaa": 1, "b": 3}
def word_frequency(lst):
    words = list(set(lst))
    d = {}
    for word in words:
	freq = lst.count(word)
	d[word] = freq
    return d

# PROB 10
# Return the tuple (word, count) for the word that appears the most frequently
# in the list, and the number of times the word appears. If the list is empty, return None.
# e.g. most_frequent_word(["a", "a", "aaa", "b", "b", "b"]) == ("b", 3)
def most_frequent_word(lst):
    if len(lst) == 0:
	return None
    else:
	word = max(set(lst), key=lst.count)
	return (word, lst.count(word))

# PROB 11
# Compares the two lists and finds all the positions that are mismatched in the list.
# Assume that len(lst1) == len(lst2). Return a list containing the indices of all the
# mismatched positions in the list.
# e.g. find_mismatch(["a", "b", "c", "d", "e"], ["f", "b", "c", "g", "e"]) == [0, 3]
def find_mismatch(lst1, lst2):
    return []

# PROB 12
# Returns the list of words that are in word_list but not in vocab_list.
def spell_checker(vocab_list, word_list):
    return list(set(word_list) - set(vocab_list))

