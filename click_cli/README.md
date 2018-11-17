# Click CLI

A basic [click](https://click.palletsprojects.com/en/7.x/) CLI (**C**ommand **L**ine **I**nterface)

## Basic Usage

Run the application directly.

```shell
$ python cli.py
Hello ✨
```

## Installation

Using the minimal `setup.py`, you can install this as a CLI

```shell
$ pip install -e .
$ sparkles
Hello ✨
```


## File Details

#### cli.py

The CLI itself. It imports `click`, defines a `@click.command`, and denotes the default method to run on execute (`cli()`).

#### setup.py

A standard configuration tool that uses `setuptools` to define an application. This file allows us to put our CLI in a place on our local file system that allows us to execute it more easily. Without this file, we would have to always call `python` on the `cli.py` file itself. 

#### requirements.txt

The requirements for running the application. Install using `pip install -r requirements.txt`

#### Files that will end up on your system

`__pycache__`: a folder containing the compiled code for `cli.py` (probably `cli.cpython-36.pyc`, if you ran the code in Python 3.6).

`sparkles.egg-info`: a folder containing all the generated files to run `sparkles` as a command. 


