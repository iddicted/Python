import random
import string
import pandas as pd   

# get random password pf length 16 with letters, digits, and symbols
characters = string.ascii_letters + string.digits + string.punctuation
n = 0
pw_list=[]
while n < 91:
    password = ''.join(random.choice(characters) for i in range(16))
    pw_list.append(password)
    n+=1
print(pw_list)
df = pd.DataFrame(pw_list)
df.to_csv('~/Desktop/passwords.csv', index=False)
