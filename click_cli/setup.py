from setuptools import setup

setup(
    name="sparkles",
    version='0.0.1',
    py_modules=['sparkles'],
    install_requires=[
        'Click',
        'colorama'
    ],
    entry_points='''
        [console_scripts]
        sparkles=cli:cli
    ''',
)
