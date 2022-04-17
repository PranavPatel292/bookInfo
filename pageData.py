# this file is responsible for creating the entire data for a page and sending them via HTML entity so that browser can render
# that code. The code first has some preFillHTML array, then it will dynamically generate all the table data based
# on the pagination conditions and append it to the table via rows. Also, some extra precautions are taken to ensure that
# HTML that is returned to the browser has some meaningful information.

# this code returns a string that is a HTML dom version which browser can render!

import subjectSplit

def dataForThePage(page, styleArray, contentPerPage, data, hashMap):

    preFillHtmlText = ["<html><head></head><body>", "".join(styleArray), "<div><table><tr><th>Id Number</th><th>Book title</th><th>Author</th><th>Type</th><th>Subjects</th></tr>"]
    
    dataArray = []

    for i in range(page * contentPerPage, min(((page * contentPerPage) + contentPerPage), len(data))):\

        individualRow = ["<tr>"]

        for dK in hashMap:

            if data[i][dK] != None:

                # if title is the key add the copyright symbol if avaible
                if dK == "title" and data[i][dK] != None:
                    element = "<td class='" + hashMap[dK] + "'>" + data[i][dK]+ " &copy"+ str(data[i]["copyrightdate"]) +"</td>"

                elif dK == "Subjects":
                    splitData = data[i][dK].split(";")
                    
                    splitData.sort()

                    pushElement = subjectSplit.subjectOperations(splitData)

                    element = "<td class='" + hashMap[dK] + "'>" + " ".join(pushElement) + "</td>"

                else:

                    element = "<td class='" + hashMap[dK] + "'>" + str(data[i][dK])+ "</td>"

            else:
                element = "<td>-</td>"

            individualRow.append(element)

        individualRow.append("</tr>")

        dataArray.append("".join(individualRow))

    preFillHtmlText.append("".join(dataArray))

    preFillHtmlText.append("</table></div></body></html>")
    
    return "".join(preFillHtmlText)