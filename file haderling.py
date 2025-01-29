"""
6.	Write a Python program that prompts the user to enter the names, ages, and marks for a specific subject for a certain number of students. The program should store each student's data in a text file named students_data.txt, with each record stored as a comma-separated line in the format: name,age,mark
Sample output:
Enter the number of students: 3
Enter name of student 1: Alice
Enter age of Alice: 18
Enter mark of Alice: 85
Enter name of student 2: Bob
Enter age of Bob: 20
Enter mark of Bob: 78
Enter name of student 3: Charlie
Enter age of Charlie: 17
Enter mark of Charlie: 92
	Students_data.txt
Alice,18,85
Bob,20,78
Charlie,17,92
i.	Extend the program to read the student data from students_data.txt and determine the youngest student. Display the name and age of the youngest student.
ii.	Extend the program to read the student data from students_data.txt and determine the student with the minimum mark. Display the name and mark of the student with the lowest mark.
iii.	Extend the program to read the student data from students_data.txt and determine the student with the maximum mark. Display the name and mark of the student with the highest mark.
iv.	Extend the program to read the student data from students_data.txt and calculate the average mark of the class. Display the average mark.
v.	Extend the program to allow the user to search for a student by their name. The program should read the student data from students_data.txt, find the student with the matching name, and display their details. If the student is not found, notify the user.
Sample outputs:
Enter the name of the student to search: Charlie
Charlie, 17, 92

Enter the name of the student to search: Kate
Kate is not found.

vi.	Extend the program to allow the user to delete a student by their name. The program should read the student data from students_data.txt, remove the record of the student with the matching name, and overwrite the file with the remaining records. Notify the user if the student was deleted or if the student was not found.
Sample input/outputs:
Enter the name of the student to delete: Bob
Deleted Bob's record successfully.
Resulting Students_data.txt
Alice,18,85
Charlie,17,92

vii.	Extend the program to allow the user to update a student's mark by their name. The program should read the student data from students_data.txt, find the student with the matching name, and update their mark with the new value provided by the user. The program should then overwrite the file with the updated records.
Sample input/output:
Enter the name of the student to update: Alice
Enter the new mark for Alice: 90
Updated Alice's mark to 90.
Resulting Students_data.txt
Alice,18,90
Bob,20,78
Charlie,17,92



"""
def open_file():
    names = []
    ages= []
    marks = []
    try:
        with open("students_data.txt", "r") as file:
            data = file.readlines()
            
    except FileNotFoundError:
        print("Sorry file wasn't there someones has taken")
    for i in data:    
        name,mark,age = i.strip().split(",")
        names.append(name.strip())
        marks.append(mark.strip())
        ages.append(age.strip())
    return names,ages,marks   

def youngest(names,ages):
    young = min(ages)
    print(F"The younges person is {names[ages.index(young)]} and his age is {young}")
    
def minmark(names,marks):
    low = min(marks)
    print(F"The student who got minimum maeks is  {names[marks.index(low)]} and his age is {low}")
    
def maximum(names,marks):
    maxi = max(marks)
    print(F"The student who got maximum maeks is  {names[marks.index(maxi)]} and his age is {maxi}")
    
def average(marks):
    total = 0
    for i in marks:
        total += int(i)
        
    averag = total/(len(marks))
    print(f"the average mark {averag:.2f}")
        
def search(names,ages,marks):
    while True:
        who = input("ENTER THE person you looking for or to exit press 1 : ")
        if who == '1':
            break
        else:
            if who in names:
                print(f"{who}, {marks[names.index(who)]}, {ages[names.index(who)]}")
            else:
                print(f"{who} is not found")
def delet(names,ages,marks):
    while True:
        who = input("ENTER THE person delete or to exit press 1 : ")
        if who == '1':
            break
        else:
            if who in names:
                del ages[names.index(who)]
                del marks[names.index(who)]
                names.remove(who)
                print(f"Deleted {who}'s record successfully.")
            else:
                print(f"{who} is not found")
    return names,ages,marks

def main():
    names,ages,marks = open_file()
    youngest(names,ages)
    minmark(names,marks)
    maximum(names,marks)
    average(marks)
    search(names,ages,marks)
    names,ages,marks = delet(names,ages,marks)
main()
    
