import pandas as pd
import matplotlib.pyplot as plt 

data = pd.read_csv('Salary_dataset.csv')
# print(data)
# plt.scatter(data.YearsExp,data.Salary)
# plt.show()

# cost function

def cost_function(m,b,points):
    total_error = 0
    for i in range(len(points)):
        x = points.iloc[i].YearsExp
        y = points.iloc[i].Salary
        total_error += ((m * x + b) - y) ** 2
    
    total_error = total_error/(2*float(len(points)))
    
# gradient descent
def gradient_descent(m_now,b_now,points,learning_rate):
    m_gradient = 0
    b_gradient = 0
    
    n = len(points)
    
    for i in range(n):
        x = points.iloc[i].YearsExp
        y = points.iloc[i].Salary
        # derivative part
        m_gradient += (1/n) * ((m_now * x + b_now) -y) * x
        b_gradient += (1/n) * ((m_now * x + b_now) -y) 
    # algorithm   
    m = m_now - learning_rate * m_gradient 
    b = b_now - learning_rate * b_gradient 
    
    return m,b

def calculate_salary(m, b, exp):
    salary = m * exp + b
    print(f"Your salary would be approximately: {round(salary,3)}")

m=0
b=0
alpha = 0.0005
epochs = 300

for i in range(epochs):
    m,b = gradient_descent(m,b,data,alpha)
    
# print(f"{epochs} :m = {m} ,b = {b}")
# testing value
exp = int(input("Enter years of experience: "))
calculate_salary(m,b,exp)

plt.scatter(data.YearsExp,data.Salary , color="black")
plt.plot(list(range(0,18)),[m * x + b for x in range(0,18)],color = "red")

plt.show()
    