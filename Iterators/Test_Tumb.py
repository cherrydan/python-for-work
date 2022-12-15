from Iterators.Tumbochka import Tumbochka


def main():
    tumb = Tumbochka()
    tumb.add_to_box("ножницы", 1)
    tumb.add_to_box("карандаш", 2)
    tumb.add_to_box("яблоко", 3)
    tumb.add_to_box("книга", 1)
    print(tumb)

    my_shiny_list = [
        ["Это", "список", "внутри", "списка"],
        {"Это", "множество", "внутри", "списка"},
        "Это строка внутри списка",
        tumb,
    ]

    for some_collection in my_shiny_list:
        for el in some_collection:
            print(el)


if __name__ == "__main__":
    main()
