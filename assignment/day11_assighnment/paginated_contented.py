# "Your task is to create a class to handle paginated content in a website.
# A pagination is used to divide long lists of content in a series of pages.
#
# Example
#
# The pagination class will accept 2 parameters:
#
# items (default: []): A list of contents to paginate.
#
# pageSize (default: 10): The amount of items to show in each page.
#
# So for example we could initialize our pagination like this:
#
# alphabetList = ""abcdefghijklmnopqrstuvwxyz"".split('')
#
# p = Pagination(alphabetList, 4)
# And then use the method getVisibleItems to show the contents of the paginated list.
#
# p.getVisibleItems() # ["a", "b", "c", "d"]
# You will have to implement various methods to go through the pages such as:
#
# prevPage
# nextPage
# firstPage
# lastPage
# goToPage
# Here's a continuation of the example above using nextPage and lastPage:
#
# p.nextPage()
#
# p.getVisibleItems()
# # ["e", "f", "g", "h"]
#
# p.lastPage()
#
# p.getVisibleItems()
# # ["y", "z"]


class Pagination:
    def __init__(self, items=[], pagesize=10):
        self.items = items
        self.pagesize = pagesize
        self.currentpage = 1

    def getVisibleItems(self):
        startIndex = (self.currentpage - 1) * self.pagesize
        endIndex = startIndex + self.pagesize
        return self.items[startIndex:endIndex]

    def prevPage(self):
        if self.currentpage > 1:
            self.currentpage -= 1

    def nextPage(self):
        if self.currentpage < self.getNumpages():
            self.currentpage = 1

    def firstPage(self):
        self.currentpage = 1

    def lastPage(self):
        self.currentpage = self.getNumpages()

    def goToPage(self):
        pass

    def getNumpages(self):
        return len(self.items) // self.pagesize + (len(self.items))


alphabetList = "abcdefghijklmnopqrstuvwxyz"
print(list(alphabetList))
p = Pagination(alphabetList, 4)
print(p.getVisibleItems())

print(p.getVisibleItems())
p.nextPage()
print(p.getVisibleItems())
p.lastPage()
print(p.getVisibleItems())
