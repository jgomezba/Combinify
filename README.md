# Combinify

A simple package that provides combinatory functionality.

## Installation

You can install it via pip:

```bash
pip install Combinify
````

## Use

 ```` Python
from Combinify import Combinatory

Cmb = Combinatory(["Orange", "Banana", "Apple", "Watermelon"],3,True)
Cmb.get_groupings()
print(Cmb)
