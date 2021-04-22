import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

#Dataset

x = ['Assignment', 'Quiz', 'S1', 'S2', 'Final','Project', 'Score' ]

x1= np.array([6.25,3.75,5.76,7.5,24.11,9,56.39])
y= np.array([6.25,3.75,5.76,7.5,24.11,9,56.39])
learning_rate = 0.001

plt.plot(x, y, label="Uzair")


#plt.plot(x, y)
plt.xlabel('x - axis') 
plt.ylabel('y - axis') 
plt.title("Cost Function")
plt.show()

def gradient_descent(x,y):
    m_curr = 0
    b_curr = 0
    n = len(x1)
    iterations = 10
    
    for i in range (iterations):
        
        print ([i])
        
        y_pred = m_curr * x1 + b_curr
        cost = (1/n) * sum([val**2 for val in (y - y_pred)])
        
        m_dx = -(2/n) * sum(x1 * (y-y_pred))
        b_dx = -(2/n) * sum(y-y_pred)
        
        m_curr = m_curr - learning_rate * m_dx
        b_curr = b_curr - learning_rate * b_dx
        
        
        
        print("m = {}, b = {}, iterations = {}, cost = {}".format(m_curr,b_curr,iterations,cost))

      
    pass


gradient_descent(x,y)



