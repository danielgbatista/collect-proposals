from services import publicationType

def isExist(search):
    print(search)
    type = publicationType.find(search)
    return len(type)
