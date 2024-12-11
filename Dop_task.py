dict = {}
grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2], [4,4,3], [5,5,5,4,5]]
students = {'Johnny','Bilbo','Steve','Khendrik','Aaron'}
students2 = list(students)
list.sort(students2)
grade_total = (sum(grades[0]) / len(grades[0]),
               sum(grades[1]) / len(grades[1]),
               sum(grades[2]) / len(grades[2]),
               sum(grades[3]) / len(grades[3]),
               sum(grades[4]) / len(grades[4]))

dict[students2[0]] = grade_total[0]
dict[students2[1]] = grade_total[1]
dict[students2[2]] = grade_total[2]
dict[students2[3]] = grade_total[3]
dict[students2[4]] = grade_total[4]
print(dict)
