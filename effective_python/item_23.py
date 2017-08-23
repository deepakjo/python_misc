from collections import defaultdict 

def log_missing():
    print('Key added')
    return 0

current = {'red':10, 'blue':20}
increments = [('red',17), ('green',13)]

result = defaultdict(log_missing, current)
print(current)
for key, amount in increments:
    result[key] += amount

print ('After', dict(result))

####increment with report####

current = {'red':10, 'blue':20}
increments = [('red',17), ('green',13)]

###count the missing reports
def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count 
        added_count += 1 
        return 0

    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount

    return result, added_count

result, count = increment_with_report(current, increments)
print (count)   
