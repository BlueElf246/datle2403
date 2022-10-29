import randomuser
import matplotlib.pyplot as plt
user=randomuser.RandomUser()
user_lst=user.generate_users(5)
print(user_lst[1].get_picture())