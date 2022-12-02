def get_final_exp(num:int())->(None):
    num_lst = [str(n) for n in str(num)]
    i = len(str(num))
    expression = []

    while i>0:
        expression.append(int("".join(num_lst[:i])))
        i-=1

    if sum(expression)>10:
        return expression[0]-int(expression[1])
    else:
        return sum(expression)


def diapozon(first, second, minimum, maximum):
    diapozon_num = [minimum, maximum]
    both = [first,second]
    if second>maximum:
        return maximum-1
    else:
        return second

def main(minimum, maximum)->(None):
    
    first_num_A = get_final_exp(minimum)
    second_num_A = get_final_exp(maximum)

    if minimum<=first_num_A and first_num_A<=maximum :
        return first_num_A,diapozon(first_num_A, second_num_A, minimum, maximum)
    elif first_num_A<minimum and first_num_A<second_num_A:
        return first_num_A,second_num_A

    else:
        return 0,0

                

both = input()
min_max = both.split(" ")
minimum = int(min_max[0])
maximum = int(min_max[1])


if minimum<=maximum :
    print(main(minimum, maximum))
