def read_data():
    with open("data.txt", encoding='utf-8') as df:
        data = df.readlines()
    return data


def write_data(new_data):
    with open("data.txt", "w", encoding='utf-8') as df:
        df.writelines(new_data)

def new_todo(new_data):
    with open("data.txt", "a", encoding='utf-8') as df:
        df.writelines(new_data)

