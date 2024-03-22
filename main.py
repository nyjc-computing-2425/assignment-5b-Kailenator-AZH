# Part 1
def read_csv(filename:str) -> tuple:
    """
    Opens the specified file and reads its data.

    Parameters
    ---------
    filename: str
        The name of the file to be read

    Returns
    ---------
    tuple
        a tuple with file header, file data
    """
    data = []
    with open(filename,'r') as f:
      header = f.readline().strip("\n").split(',')
      for i in f:
        line_data = i.strip("\n").split(',')
        data.append([int(m) if m.isdecimal() else m for m in line_data])
      f.close()
    return header,data


# Part 2
def filter_gender(enrolment_by_age: list, sex: str) -> list:
    """
    Filters students based on their gender and outputs the students that match the specified sex.

    Parameters
    ---------
    enrolment_by_age: list
        List of student enrolments
    sex: str
        Sex to filter the students with

    Returns
    ---------
    list
        List of students that match the specified sex
    """
    matching = []
    for i in enrolment_by_age:
      if i[2] == sex:
        matching.append([i[0],i[1],i[3]])
    return matching


# Part 3
def sum_by_year(enrolment: list) -> list:
    """
    Finds the number of students enrolled in each year

    Parameters
    ---------
    enrolment: list
        List of student enrolments

    Returns
    ---------
    lista
        List of students that enrolled in each year
    """
    enrolled_per_year = []
    for i in range(1984,2018+1):
      enrolled_per_year.append([i,0])
      for m in enrolment:
        #print(m[-1])
        if int(m[0]) == i:
          enrolled_per_year[-1][1] += int(m[-1])
    return enrolled_per_year

# Part 4
def write_csv(filename: str, header: list, data: list) -> int:
    """
    Write a header and data on a specified file

    Parameters
    ---------
    filename: str
        The name of the file to write on
    header: list
        The header(s) to write on the file
    data: list
        The data to write on the file

    Returns
    ---------
    int
        The number of lines written on the file
    """
    n = 0
    with open(filename,'w') as f:
      f.write(','.join(header))
      f.write("\n")
      for i in range(len(data)):
        data[i] = [str(m) for m in data[i]]
        f.write(','.join(data[i]))
        f.write("\n")
        n += 1
      f.close()
    return n+1

# TESTING
# You can write code below to call the above functions
# and test the output

#head,enrolment_data = read_csv("pre-u-enrolment-by-age.csv")
#print(filter_gender(enrolment_data,"F"))
#print(sum_by_year(enrolment_data))
#write_csv("test.txt",["Yes","Sir"],enrolment_data)