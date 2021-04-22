import random as rd 


corpus = [
  39,  144,
  47,  220,
  45,  138,
  47,  145,
  65,  162,
  46,  142,
  67,  170,
  42,  124,
  67,  158,
  56,  154,
  64,  162,
  56,  150,
  59,  140,
  34,  110,
  42,  128,
  48,  130,
  45,  135,
  17,  114,
  20,  116,
  19,  124,
  36,  136,
  50,  142,
  39,  120,
  21,  120,
  44,  160,
  53,  158,
  63,  144,
  29,  130,
  25,  125,
  69,  175
  ]


m = int(len(corpus)/2) # rows in data entries

X = [ corpus[i] for i in range(0,m*2,2) ]
Y = [ corpus[i] for i in range(1,m*2,2)]     
theta = []
for i in range(m):
  # theta.append([random.uniform(0,5),random.uniform(0,5)]) 
  # theta0 =random, theta1=random
  theta.append([0,random.uniform(0,5)])    
  # theta0 is considered = 0 and theta1 = random




# def hypothesis()

def hypothesis(x, t):
    return [(t[0]+i*t[1]) for i in x]


def cost(m, X, y):
    total = 0
    for i in range(m):
        squared_error = (y[i] - X[i]) ** 2
        total += squared_error
    
    return total * (1 / (2*m))


result=[]
for i in range(m):
    approximate_values = hypothesis(X, theta[i])

    print("Theta = ", theta[i])
    print("Cost = ", cost(m, Y, approximate_values), '\n')
    result.append(cost(m, Y, approximate_values))

print("Theta with  : ",theta[result.index(min(result))], 
      " is having minimum cost which is  ",min(result))
