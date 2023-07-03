try:
    data = open("data.txt","r+")
except:
    data = open("data.txt","x")

def save_data():
    save = "dic15 =" + dic15 "," + "dic10 =" dic10 + "," + "count =" + count
    data.write(save)

def load_data():
    pass

