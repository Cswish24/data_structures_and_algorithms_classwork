# need to be able to find the minimum number of operations used to modify one string to match another
# ex. string 2 crch to  string 1 catch
# need to loop through string via recursion for div and conq, return whether we can skip to the next letter, replace, insert, or delete
def string_mod(string1, string2, index1=0, index2=0):
    if index1 == len(string1):
        return len(string2) - index2
    if index2 == len(string2):
        return len(string1) - index1
    if string1[index1] == string2[index2]:
        return string_mod(string1, string2, index1 + 1, index2+1)
    else:
        delete = 1 + string_mod(string1, string2, index1, index2+1)
        insert = 1 + string_mod(string1, string2, index1 + 1, index2)
        replace = 1 + string_mod(string1, string2, index1+1, index2+1)
        return min(delete, insert, replace)


print(string_mod('catch', 'crchalsgjk'))


def string_mod_td(string1, string2, index1=0, index2=0, dict={}):
    if index1 == len(string1):
        return len(string2) - index2
    if index2 == len(string2):
        return len(string1) - index1
    strindex = str(index1) + str(index2)
    if strindex in dict:
        return dict[strindex]
    if string1[index1] == string2[index2]:
        dict[strindex] = string_mod_td(
            string1, string2, index1 + 1, index2+1, dict)
        return dict[strindex]
    else:
        delete = 1 + string_mod_td(string1, string2, index1, index2+1, dict)
        insert = 1 + string_mod_td(string1, string2, index1+1, index2, dict)
        replace = 1 + string_mod_td(string1, string2, index1+1, index2+1, dict)
        dict[strindex] = min(delete, insert, replace)
        return dict[strindex]


print(string_mod_td('catch', 'crchalsgjk'))

# kcch catch
# catch tchca
# find a way to store operation totals in the list/ maybe by using unique ids based on indexes need len s1 * len s2 spaces in array
# the optimized step could could come from 3 different areas, ex. 2,2 could come from 1,1 1,2 or 2,1, should come from the min of those
# very last step would be to loop through terminal array indices
#   and perform len difference calculations and add the coressponding len to the final tally
# do i need to create a teminal array? how to determine if a pair of indices is terminal?


# cach catch

def string_mod_dt(string1, string2, index1=0, index2=0):
    dict = {}
    terminal_arr = []
    while True:
        if string1[index1] == string2[index2]:
            index1 += 1
            index2 += 1
            continue
        else:
            delete = index2 + 1
            insert = index1 + 1
            replace = index1 + 1, index2 + 1
            dict[str()]
