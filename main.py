def read_excel_and_collect_birthday_list():
    pass

def open_whatsapp_and_wish(bd_list):
    pass

if __name__ == "__main__":
    bd_list = read_excel_and_collect_birthday_list()
    if bd_list:
        open_whatsapp_and_wish(bd_list)
    else:
        print("Oops!!.. Seems no friends having birthday today")
