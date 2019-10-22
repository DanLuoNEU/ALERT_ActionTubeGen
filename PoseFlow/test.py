import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import matplotlib.transforms as transforms
from scipy import random
from scipy.stats import wishart, chi2
# Generate Bi-Variate Gaussian Distribution samples
## MEAN IS 0
mean = [0,0]
cov = [[1,0],[0,36]]

N = 5000
x, y = np.random.multivariate_normal(mean, cov, 5000).T
plt.plot(x, y, 'x')
plt.axis('equal')
plt.show()

# Generate random scale matrix
W = random.rand(2,2)
W = np.dot(W, W.T)
print(W)

# Vary degrees of freedom of the prior, 
# keeping number of samples and scale ma-trix fixed

v = 2
N = 10

x,y = np.random.multivariate_normal(mean, cov, 10).T

v_new = N+v
W_new = np.linalg.inv(np.cov(x,y)+W)

w = wishart(df=v_new, scale=W)
w_samples = w.rvs(5)
# Compute eigenvalues and associated eigenvectors
ellipse_values,ellipse_vectors = np.linalg.eigh(w_samples)
# print(ellipse_values.shape[0])

ells = []
for i in range(ellipse_values.shape[0]):
    e_val = ellipse_values[i]
    e_vec = ellipse_vectors[i]
    # Compute "tilt" of ellipse using first eigenvector
    a, b = e_vec[:, 0]
    theta = np.degrees(np.arctan2(b, a))
    if theta < 0:
        theta = 360+theta
    # Eigenvalues give length of ellipse along each eigenvector
    wt, ht = 2 * np.sqrt(e_val)
    print(wt,ht, theta)
    ells.append(Ellipse((0,0), wt, ht, theta,fill=False, color=(0,0,i*0.2),linewidth=5))
    
fig, ax = plt.subplots()

for e in ells:
    ax.add_artist(e)
#     e.set_clip_box(ax.bbox)
    e.set_alpha(0.5)
#     e.set_facecolor(np.random.rand(3))

plt.show()