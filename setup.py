from setuptools import setup

setup(
    name='jit',
    version='0.0.1',
    py_modules=['jit'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'jit = jit:cli',
        ],
    },
)

