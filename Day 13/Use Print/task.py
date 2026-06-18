'''
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)
'''


# PAUSE 1
# The code is supposed to calculate the total number of words given the number pages and the word per page.
# But it's not currently giving any output. Diagnose the problem using print() statements.

word_per_page = 0
print(f"words per page {word_per_page}")
pages = int(input("Number of pages: "))
print(f"words per page {word_per_page}, pages {pages}")
word_per_page == int(input("Number of words per page: "))
print(f"words per page {word_per_page}, pages {pages}")
total_words = pages * word_per_page
print(total_words)

'''
My diagnosis - The word_per_page variable isn't being updated by the user input due to the assignment. Developer used == instead of =
'''


# PAUSE 2
# Fix the code.

word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)