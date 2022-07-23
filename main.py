def read_excel_and_collect_birthday_list():
    return [None]


def open_whatsapp_and_wish():
    print(bd_list)


if __name__ == "__main__":
    bd_list = read_excel_and_collect_birthday_list()
    if bd_list:
        open_whatsapp_and_wish()
    else:
        print("Oops!!.. Seems no friends having birthday today")
