input_number = int(input())

number_list = []
for i in range(0, input_number):
    number = int(input())
    number_list.append(number)

number_list.sort()

for j in range(len(number_list)):
    print(number_list[j])
