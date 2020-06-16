print('Welcome to the Grade Sorter App')
grade=[]
f1g=int(input('What is ur first grade(0-100): '))
sg=int(input('What is ur second grade(0-100): '))
tg=int(input('What is ur third grade(0-100): '))
f4g=int(input('What is ur fourth grade(0-100): '))
grade.append(f1g)
grade.append(sg)
grade.append(tg)
grade.append(f4g)
print('\nYour unarranged grades are: ' + str(grade))
grade.sort() #permanently sort items in the list
print('\nYour grades are: ' + str(grade))
print('Your grades from highest to lowest are: ' + str(sorted(grade, reverse=True)))#temporarily sort items in the list
print('The lowest two grades will now be dropped.')
del_grade1=grade.pop(0)#this permanently remove an item of a list
del_grade2=grade.pop(0)
print('Removed grade: ' + str(del_grade1))
print('Removed grade: ' + str(del_grade2))
print('Your remaining grades are: ' + str(grade))
print('Nice work! Your highest grade is a ' + str(grade[-1]))