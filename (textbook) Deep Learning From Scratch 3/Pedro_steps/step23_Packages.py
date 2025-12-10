if '__file__' in globals():
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import numpy as np
import matplotlib.pyplot as plt
from Pedro_package import Pedro_Variable


x = Pedro_Variable(np.array(1.0))
y = (x + 3) ** 2
y.backward()

print(y)
print(x.grad)