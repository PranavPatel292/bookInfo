# this file basically returns all the uniques subjects that are in the 
# dataset. Apart from this, a bit of string manupilcation has been done in order
# for it to work with CSS naming conversions.

# this file returns an hashmap of all the unique subject recoards.

def findAllUniqueSubjects(data):

    hashMapUniquesubjects = {}

    for i in range(len(data)):
        if data[i]["Subjects"] != None:
            splitData = data[i]["Subjects"].split(";")

            for j in splitData:
                if j not in hashMapUniquesubjects:     

                    # remove the . from the last index (some data may contain . in its last postion), 
                    # and make a new string as Python strings are immutable in nature.

                    if j[-1] == ".":
                        newJ = j[:-1]
                    else:
                        newJ = j
                    
                    spaceRemove = newJ.replace(" ", "")

                    spaceRemove = spaceRemove.replace("(", "-")
                    spaceRemove = spaceRemove.replace(")", "-")

                    hashMapUniquesubjects[spaceRemove] = True

    return hashMapUniquesubjects