from setuptools import setup

setup(
    name='qetag',
    version='0.1.0',
    py_modules=['qetag'],
    install_requires=[
        "requests"
    ],
    entry_points='''
        [console_scripts]
        qetag=qetag:qetag
    ''',
)
