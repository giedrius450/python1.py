start = 170849
end = 189965
count = 0

def check_if_lucky(number):
    number_str = str(number)
    return number_str[:3]==number_str[3:]

for i in range(start,end+1):
    if check_if_lucky(i):
        count=count + 1

print(count) 



