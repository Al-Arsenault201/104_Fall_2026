with (open ("/Users/alfredarsenault/Downloads/Fall_2025.csv","r") as infile):
    """
    data = infile.read()  #reads in entire file as a single string
    print (data)

    # this is not useful. I have to split things
    # I'll start by splitting on newlines - \n

    data_list = data.split("\n")
    print (data_list)
    """

    # read the first two lines of the file and throw them away
    infile.readline()
    infile.readline()

    # use readlines() to read in a list
    data_lines = infile.readlines()
    for i in range(len(data_lines)):
        print (data_lines[i])

    # work with data_list[0]
    student_record_entry = data_lines[0].split(',')
    print (student_record_entry)

    #create a dictionary of Heisenberg's student record
    student_record = { }
    student_record['last_name'] = student_record_entry[0]
    student_record['first_name'] = student_record_entry[1]
    student_record["studentID"] = student_record_entry[2]
    # convert the rest into integers
    student_record["p1"] = int(student_record_entry[3])
    student_record["p2"] = int(student_record_entry[4])
    student_record["p3"] = int(student_record_entry[5])

    student_record["t1"] = int(student_record_entry[6])
    student_record["t2"] = int(student_record_entry[7])
    student_record["t3"] = int(student_record_entry[8])

    print (student_record)

    # add new key/value for total score
    student_record["total_score"] = student_record["p1"] + student_record["p2"] + student_record["p3"] + student_record["t1"] + student_record["t2"] + student_record["t3"]

    # assign a letter grade
    if student_record["total_score"] >= 500:
        student_record["letter_grade"] = "A"
    elif student_record["total_score"] >= 420:
        student_record["letter_grade"] = "B"
    elif student_record["total_score"] >= 360:
        student_record["letter_grade"] = "C"
    elif student_record["total_score"] >= 300:
        student_record["letter_grade"] = "D"
    else:
        student_record["letter_grade"] = "F"

    print (student_record)

