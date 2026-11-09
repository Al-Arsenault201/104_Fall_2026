with open("/Users/alfredarsenault/Downloads/data_files/Fall_2026.csv", "r") as infile:
    reader = infile.readline()
    reader = infile.readline()
    reader = infile.readlines()
    for i in range(5):
        data = reader[i].split(',')
        print(data)

