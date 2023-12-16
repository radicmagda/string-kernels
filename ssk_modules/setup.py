from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

# Specify the include directories for NumPy
include_dirs = [np.get_include()]

# Define the Cython extension
extensions = [
    Extension("string_kernel", ["string_kernel.pyx"], include_dirs=include_dirs),
]

# Setup script
setup(
    ext_modules=cythonize(extensions),
    include_dirs=[np.get_include()],  # This might not be necessary, but include it just in case
    name='ssk_modules'
)
