# ticket-py

Python binding for [ticket](https://github.com/Hanaasagi/ticket).

### Main-Feature

- fast & unique
- thread-safe

Actually, the compile process is slow :)

### Install

It depends on [`pyo3`](https://github.com/PyO3/pyo3), so only supports python 2.7 as well as python 3.5 and up. The minimum required rust version is 1.30.0-nightly 2018-08-18.

make sure the dependence and run

```Bash
pip install git+https://github.com/Hanaasagi/ticket-py
```

### Usage

```Python
In [1]: import ticket

In [2]: ticketing = ticket.Ticketing()

In [3]: ticketing.gen()
Out[3]: [91, 187, 110, 255, 149, 82, 142, 95, 203, 237, 52, 123]

In [4]: ticket.encode(_)
Out[4]: 'betmtvslaa75vivd6htg'

In [5]: ticket.decode(_)
Out[5]: [91, 187, 110, 255, 149, 82, 142, 95, 203, 237, 52, 123]

In [6]: bytes(_)
Out[6]: b'[\xbbn\xff\x95R\x8e_\xcb\xed4{'

In [7]: len(_)
Out[7]: 12
```

### License
BSD 3-Clause License Copyright (c) 2018, Hanaasagi
