# make a pagination button

# group the data into the 

from flask import *
import load_data
import unique_data
import style
import pageData


# this are some varible which are used in order to efficently run the program

# pageIndex: tells us which page are we on, if it is larger than the data size then we can pass the appropriate error
# contentPerPage: defines the total content information on a single page
# hashMap: is used to map the data's heading with its CSS class name.

pageIndex = 0
contentPerPage = 10
hashMap = {
    "biblionumber" : "idBook",
    "title" : "titleBook",
    "author" : "authorBook",
    "type" : "typeBook",
    "Subjects" : "subSubjectBook"
}

# loading the data into the memory
data = load_data.load_file()

# make a uniqueValue file
hashMapUniquesubjects = unique_data.findAllUniqueSubjects(data)

# make a style section file
styleArray = style.styleArrayAddition(hashMapUniquesubjects)

app = Flask(__name__)

# so idea here is that, every time only cotentPerPage worth of data will be display, so we will have an query param 
# which will tell us the page number, and based on that page number we will calcaute the amout of data to be
# display on the page!

@app.route("/getData", methods=["GET"])
def handlePageData():
    args = request.args.to_dict()

    pageIndex = int(args.get("pageNumber"))

    if pageIndex >= (len(data) / contentPerPage):
        return "Data Exhausted"

    return pageData.dataForThePage(pageIndex, styleArray, contentPerPage, data, hashMap)

if __name__ == '__main__':
    app.run()