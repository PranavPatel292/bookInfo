# this file will generate all the CSS-style that is require for the 
# html file, retured as a styleArray. In this file all the CSS is done with the unique className with custom CSS properties.
# so, all the different Subjects () will get its own CSS values such as in this case only the color (RGB format) & text-decoration:hover properties.

import random

styleArray = ["<style>table{border-collapse: collapse;width: 100%;}td, th{text-align: center;padding: 8px; font-size: 20px;}.idBook{width: 10%;}.titleBook{width: 30%;} .typeBook{width: 10%;} .subjectBook{width: 35%} .subSubjectBook{padding: 3%; color: brown;} tr:nth-child(even) {background-color: #f2f2f2;} .authorBook{width: 15%;}"]

def styleArrayAddition(hashMapUniquesubjects):

    hashMapKeys = hashMapUniquesubjects.keys()

    for k in hashMapKeys:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        newK = k.replace("(", "-")
        newK = newK.replace(")", "-")

        styleArray.append("." + newK + "{ color: rgb(" + str(r) +", " + str(g) + ", " + str(b)  +"); }")
        styleArray.append("." + newK + ":hover{ text-decoration: underline; font-size: 25px; background-color: black; color: white; border-radius: 30px; width: auto; cursor:pointer;}")

    styleArray.append("</style>")

    return styleArray