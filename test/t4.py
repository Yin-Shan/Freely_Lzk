def getinfo(name, age, hoppy=''):
    if hoppy:
        print("name:", name.title(), "age:", age, "hoppy:", hoppy)
        print(type(hoppy))
    else:
        print("name:", name.title(), "age:", age)

if __name__ == '__main__':
    getinfo('tom', 25)
    getinfo('tom', 25, 2)