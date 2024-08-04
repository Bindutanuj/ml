import csv

a = []
print("\nThe Given Training Data Set\n")
with open('1.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        a.append(row)
        print(row)

num_attributes = len(a[0]) - 1
print("\nThe initial value of hypothesis:")
hypothesis = ['0'] * num_attributes
print(hypothesis)

for j in range(0, num_attributes):
    hypothesis[j] = a[0][j]

print("\nFind S: Finding a Maximally Specific Hypothesis\n")
for i in range(0, len(a)):
    if a[i][num_attributes] == 'Yes':
        for j in range(0, num_attributes):
            if a[i][j] != hypothesis[j]:
                hypothesis[j] = '?'
            else:
                hypothesis[j] = a[i][j]
            print("For Training instance No:{0} the hypothesis is ".format(i), hypothesis)

print("\nThe Maximally Specific Hypothesis for a given Training Examples:\n")
print(hypothesis)
