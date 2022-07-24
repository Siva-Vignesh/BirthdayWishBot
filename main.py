from datetime import datetime


def read_excel_and_collect_birthday_list():
    current_day = datetime.now().day
    current_month = datetime.now().month
    birthday_list = list()
    with open("birthday_database.csv", "r") as data:
        data.readline()  # this will remove the first row (header)
        for each_row in data.readlines():
            dob = each_row.split(",")[2]
            if int(dob.split("-")[0]) == int(current_day) and int(dob.split("-")[1]) == int(current_month):
                birthday_list.append({"name": each_row.split(',')[1], "ph_no": each_row.split(',')[3]})

    return birthday_list


def open_whatsapp_and_wish():
    print(bd_list)


if __name__ == "__main__":
    bd_list = read_excel_and_collect_birthday_list()
    if bd_list:
        open_whatsapp_and_wish()
    else:
        print("Oops!!.. Seems no friends having birthday today")
