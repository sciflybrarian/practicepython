# https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

def listends(list):
    result = []
    if len(list) > 0:
        result.append(list[0])
    if len(list) > 1:
        result.append(list[len(list) - 1])
    return result
