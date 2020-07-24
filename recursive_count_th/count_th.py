'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # make a variable to keep track of the 
    # number we hit the letters
    count = 0
    # base case
    if len(word) == 0:
        return count
    
    # recursive case
    # checking every 2 letter of the word
    # until we hit the base case
    if word[:2] == 'th':
        count += 1
        return count + count_th(word[1:])

    return count_th(word[1:])

# print(count_th('awwaethth'))
