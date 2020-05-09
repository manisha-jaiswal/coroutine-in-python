#coroutine example
def searcher():
    import time
    book = "This is Book assume bigger and will take time....."
    # time.sleep(4)  # just assume i m searching something
    #it will take time just once then will load faster from where loop...
    # we want to run this again from here next time...
    while True:
        text = (yield)    #Generator     # it means searcher is coroutine and will continue from here next time..
        if text in book:
            print("Found..")
        else:
            print("Not Found..")

search = searcher()                      # coroutine starts here
next(search)
import time
inp = input("what you want to search in book : ")
print("Search Started.. Plzz Wait...")
time.sleep(2)
search.send(inp)
print("Search Complete..")
inp1 = input("Press Other Keyword To Search Again : ")
print("Now Search Results Will Load Faster..")
time.sleep(1)
search.send(inp1)
print("Search Complete..")
inp2 = input("Press Other Keyword To Search Again : ")
search.send(inp2)
print("Search Complete..")
print("Search God Mode On : ")
inp3 = input("Aur Likh Kya Kuch Search Karu Bro Aane De ")
search.send(inp3)
print("Search Complete..")
print("Bas Aaj Itna Hi ...")
search.close()