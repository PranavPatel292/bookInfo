# this file is used in order to remove any duplicate records that might be present in our original 
# data's subject field. This is done in order to remove amguity in the code. Agian some string 
# manipulation has been performed in order to work with CSS naming conversion.

# this function return an array of all the unique subject names for a single record.
import copy

def subjectOperations(data):
    tempHashMap = {}
    result = []
    counter = 1

    for sD in data:

        if sD[-1] == ".":
            noSpace = sD[:-1]

        else:
            noSpace = sD

        stringToDisplay = list(noSpace)

        noSpace1 = noSpace.replace(" ", "")

        comapreHashMapStrings = noSpace1.lower()

        if comapreHashMapStrings not in tempHashMap:

            tempHashMap[comapreHashMapStrings] = True
            noSpace1 = noSpace1.replace("(", "-")
            noSpace1 = noSpace1.replace(")", "-")

            span = "<span class='" +noSpace1+"'>" +str(counter) +". " + "".join(stringToDisplay) +"</span><br>"
            
            result.append(span)
            counter += 1
    return result