# Linear or sequential search is a method of finding a target value within a list
# It sequentially checks each element of the list for the target value until a match is found or all the element searched
# Best case o(1), worst case o(n)
# https://coggle.it/diagram/W5E5tqYlrXvFJPsq/t/master-the-interview-click-here-for-course-link
beasts = ['Centaur', 'Godzilla', 'Mosura', 'Minotaur', 'Hydra', 'Nessie']

beasts.index('Godzilla')
def findIndex():
    for idx,val in enumerate(beasts):
        if val == 'Godzilla':
            return idx
    return None