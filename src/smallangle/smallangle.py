"""Generate lists of numbers between 0 and 2π and their repesctive sine or tangent values.
"""
import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def smallangle():
    """Make a group of commands using the @click.group() decorator.
    """
    pass

@smallangle.command()
@click.option(
    "-n",
    "--count",
    default = 1,
)
def sin(count):
    """Generate list of numbers between 0 and 2π with their respective sine values.

    Args:
        count (int): number of x-values between 0 and 2π.
    """
    x = np.linspace(0, 2 * pi, count)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})

    print(df)

@smallangle.command()
@click.option(
    "-n",
    "--count",
    default = 1,
)
def tan(count):
    """Generate list of numbers between 0 and 2π with their respective tangent values.

    Args:
        count (int): number of x-values between 0 and 2π.
    """
    x = np.linspace(0, 2 * pi, count)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})

    print(df)

if __name__ == "__main__":

    smallangle()