import statsmodels as stats
import numpy as np
import matplotlib.pyplot as plt


def similarity(l):

  """
    Function that calculates the ui=q2−xi and the vi=x(n+1−i) for a list, Series Pandas DataFrame
    The first part is responsible to calcute the first part of the similarity functions: ui=q2−xi
    The second part is responsible to calculete the second part of the similarity formula: vi=x(n+1−i)

    It is extremely visual and helpful to see the distribution scatter os a list, Series or Pandas DataFrame.

  """

  u = []
  v = []
  q2 = np.median(l)

  for i in range(len(l)):

    if (q2 - l[i]) == 0:
    # add the index number when the q2 - l[i] is equal to zero  
      u.append(i)
      break

    else:
      u.append(q2 - l[i])


  for j in range(len(l) + 1):

    if (l[-j] - q2) == 0:
      v.append(i) ## add the index number when the l[-j] - q2 is equal to zero
      break

    else:
      v.append(l[-j] - q2)

  return u, v[1:], q2


u, v, q2 = similarity(l)


def plotting_similarity(u, v):
  fig, ax = plt.subplots(1, 2, figsize=(4.5,3.5), layout='constrained')

  ax[0].scatter(u, v, c='black', alpha=0.5)
  ax[0].axhline(u[-1], c="red")
  ax[0].grid(True)

  ax[1].bar(u, v)
  ax[1].grid(True)

  fig.show()

plotting_similarity(u, v);