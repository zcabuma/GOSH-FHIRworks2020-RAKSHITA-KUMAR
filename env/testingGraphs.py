import matplotlib.pyplot as plt
from krakenio import Client

plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.savefig('foo.png')


api = Client('1fefa2b086a5e2538e4e0499e76b3d7b', '36a93fa9921dff34665b8eaed2aa4913cfbb4b02')

data = {
    'wait': True
}

result = api.upload('foo.png', data)

print(result.get('kraked_url')) 



