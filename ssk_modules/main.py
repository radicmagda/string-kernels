# How to run (linux):
# > python main.py
#
# If Cython can't find the NumPy libraries at compilation time:
# > CFLAGS=-I/usr/lib/python3.9/site-packages/numpy/core/include python main

import pyximport; pyximport.install()  # noqa: E702

from string_kernel import ssk, string_kernel
import numpy as np

def sskpy(a,b,k,lam):
        return ssk(a,b,k,lam)

if __name__ == '__main__':
    print("Testing...")
    lbda = .6
    # We can compute this kernel by hand and the result should be the thing on the
    # second column
    xs = np.array(["cat", "car", "cart", "camp", "shard"]).reshape((5, 1))
    ys = np.array(["a", "cd"]).reshape((2, 1))
    print(string_kernel(xs, ys, 2, 1.))

    test = "This is a very long string, just to test how fast this implementation " \
        "of ssk is. It should look like the computation tooks no time, unless you're" \
        " running this in a potato pc"
    print(ssk(test, test, 30, .8, accum=True))
