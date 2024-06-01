def welcome (firstname, lastname, gender):
    if gender =="M":
        welcome = lastname + " " +firstname + "先生歡迎您"
    elif gender == "F":
        welcome = lastname + " " +firstname + "小姐歡迎您"
    return welcome

info1 = welcome("早安", "你好", "M")
info2 = welcome("晚安", "起床", "F")

print(info1)
print(info2)
