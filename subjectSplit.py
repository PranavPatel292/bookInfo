# this file is used in order to remove any duplicate records that might be present in our original 
# data's subject field. This is done in order to remove amguity in the code. Agian some string 
# manipulation has been performed in order to work with CSS naming conversion.

# this function return an array of all the unique subject names for a single record.

def subjectOperations(data):
    tempHashMap = {}
    result = []

    for sD in data:

        noSpace = sD.replace(" ", "")
        
        if noSpace[-1] == ".":
            noSpace1 = noSpace[:-1]
        else:
            noSpace1 = noSpace

        if noSpace1 not in tempHashMap:

            tempHashMap[noSpace1] = True
            noSpace1 = noSpace1.replace("(", "-")
            noSpace1 = noSpace1.replace(")", "-")

            span = "<span class='" +noSpace1+"'>" + sD +"</span><br>"
            
            result.append(span)
        
    return result