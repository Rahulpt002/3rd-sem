import matplotlib.pyplot as plt

data = {'Java': 27.2, 'Python': 17.6, 'PHP': 8.8, 'JavaScript': 18, 'C#': 7.7, 'C++': 6.7}

courses = list(data.keys())
values = list(data.values())

fig, ax = plt.subplots()
ax.pie(values, labels=courses, autopct='%1.1f%%', colors=['red', 'green', 'gray', 'yellow','pink','blue'])

plt.title("Programming languages popularity")

plt.show()
