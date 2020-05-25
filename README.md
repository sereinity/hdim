# n-dimensional-cubes computer


## The subject

Studding number of object in each dimensions for a « cube ».
By example, a cube has 6 faces, 12 edges, 8 nodes.
An hypercube has 8 cubes, 24 faces, 32 edges, 16 nodes.
A 10-dimensional composed of 18 9-dimensional-cubes …

This program generates incrementally the number of each n-cube (and nodes, dimension 0) present in n-cubes.


## The original objective

The project has been created to see if a pattern was present on the maximal number of objects
(that's why some elements are highlighted).


## Cool implementation facts

Should keep a really low memory footprint, even when querying tons of elements.

```
usage: hdim.py [-h] [--cell-size SIZE] [--raw] [--no-highlight] [--force] [max_dim]

Compute size data about hypercube and other cool object

positional arguments:
  max_dim             Maximum dimension cardinality, horizontal fill if set to 0, infinite if set to -1 (default: 5)

optional arguments:
  -h, --help          show this help message and exit
  --cell-size SIZE    Maximum cell size for display, '0' means auto (default: 0)
  --raw, -r           Sets cell size to 1 and disable highlights (default: False)
  --no-highlight, -c  Do not highlight elements (default: False)
  --force, -f         Run, even if it breaks display (default: False)
```


## Next

I don't know, just sharing, create issues if you have any ideas.
