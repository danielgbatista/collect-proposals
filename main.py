from services import proposition
from validations import publicationType


def main():
    for page in range(2):
        page += 1
        list = proposition.list(page)
        for item in list[0]:
            print(item)
            exist = publicationType.isExist(item['siglaTipo'])
            print(exist)
    print("hello world")

if __name__ == "__main__":
    main()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
