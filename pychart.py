import matplotlib.pyplot as plt
category=['food','transport','rent','other']
cost=[5000,2000,8000,1000]
plt.pie(cost,labels=category,radius=1.5,autopct='%0.1f%%',explode=[0,0.1,0,0])
plt.show()