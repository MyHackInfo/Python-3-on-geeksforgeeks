'''
    ### Closure in python ###
    A Closure is a function object that remembers values
    in enclosing scopes even if they are not present in memory.

'''
def name(text):
    text=text
    def last():
        print(text)

    return last

if __name__ == '__main__':
    get=name("Narsi-Gurjar")
    get()

