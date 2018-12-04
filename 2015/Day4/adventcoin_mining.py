from hashlib import md5

print md5('abcdef609043').hexdigest()
print md5('pqrstuv1048970').hexdigest()
input = "yzbqklnj"

it = 0
for it in range(0, 1000000):
    hash = md5('yzbqklnj' + str(it)).hexdigest()
    if hash[:5] == '00000':
        print it
        break

it2 = 0
for it2 in range(0,  100000000):
    hash = md5('yzbqklnj' + str(it2)).hexdigest()
    if hash[:6] == '000000':
        print it2
        break
