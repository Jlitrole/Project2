# Import random below:
import random

# Create random_list below:
random_list = [random.randint(1,101) for i in range(101)]

# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)


import codecademylib3_seaborn
from matplotlib import pyplot as plt
import random

# Add your code below:
numbers_a = range(1, 13)
numbers_b = random.sample(100)

plt.plot(numbers_a, numbers_b)

plt.show()