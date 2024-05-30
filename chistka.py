with open('123.txt', 'r', encoding="utf-8") as f:
    data = f.readlines()
data[0] = "q\n"
data[1] = "w\n"
data[2] = "e\n"
data[3] = "r\n"
data[4] = "t\n"
data[5] = "y\n"
data[6] = "u\n"
data[7] = "i\n"
data[8] = "o\n"
data[9] = "p\n"
data[10] = "a\n"
data[11] = "s\n"
data[12] = "00:00:00"
f.close()
save_changes = open('123.txt', 'w', encoding="utf-8")
save_changes.writelines(data)
save_changes.close()