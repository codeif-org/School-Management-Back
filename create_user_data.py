# import django
# django.setup()
from django.contrib.auth.models import User
import names
import pandas as pd

print(User.objects.all())

username = []
for i in range(4000):
    if len(username) == 1150:
        break
    name = names.get_first_name().lower()
    if name not in username:
        username.append(name) 
    
print("length of username", len(username))        

ids = [x for x in range(101, 101+1150)]
user_df = pd.DataFrame({
    'id': ids,
    'username': username,
    'first_name': username,
})

arr_user = user_df.values
print(arr_user)
counter = 1
for item in arr_user:
    user = User.objects.create_user(
        id = item[0],
        username=item[1],
        password='test123',
        first_name=item[2],
        email=item[1] + '@gmail.com',
    )
    user.save()
    print('user created successfully..', counter)
    counter += 1