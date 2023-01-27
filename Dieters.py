input = open('Dieters.txt', 'r')
output = open('Weightloss.txt', 'w')

num_people = 0
total_weight = 0

name = input.readline().rstrip('\n')
while name != "":
    num_people += 1
    start_weight = int(input.readline().rstrip('\n'))
    end_weight = int(input.readline().rstrip('\n'))
    net_weight = start_weight - end_weight
    output.write(name + " lost " + str(net_weight) + " pounds." + '\n')
    total_weight += net_weight
    name = input.readline().rstrip('\n')

print("The " + str(num_people) + " people dieting lost a total of " + str(total_weight) + " pounds.")
input.close()
output.close()
