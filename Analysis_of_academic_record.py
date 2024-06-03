import csv

with open('fahad_data.csv', 'r') as data:
    data_s = data.read()



# print(data_s)
data = data_s.split(',')
print(data)
A_plus = []
A = []
B_plus = []
B = []
C_plus = []:
C = []
D_plus = []
D = []
F = []

for i in data:

    if i == 'A+':
        A_plus.append(i)

    elif i == 'A':
        A.append(i)

    elif i == ('B+'):
        B_plus.append(i)

    elif i == ('B'):
        B.append(i)

    elif i == ('C+'):
        C_plus.append(i)

    elif i == ('C'):
        C.append(i)

    elif i == ('D+'):
        D_plus.append(i)

    elif i == ('D'):
        D.append(i)

    elif i == ('F'):
        F.append(i)

print('Marks A+: ', A_plus)
print('Marks A: ', A)
print('Marks B+: ', B_plus)
print('Marks B: ', B)
print('Marks C+: ', C_plus)
print('Marks C: ', C)
print('Marks D+: ', D_plus)
print('Marks D: ', D)
print('Marks F: ', F)

calculate_data = len(A_plus) + len(A) + len(B_plus) + len(B) + len(C_plus) + len(C) + len(D_plus) + len(D) + len(F)
print(calculate_data)

