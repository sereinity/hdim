# n-dimensional-cubes computer


## The subject

Studding number of object in each dimensions for a « cube ».
By example, a cube has 6 faces, 12 edges, 8 nodes.
A tesseract has 8 cubes, 24 faces, 32 edges, 16 nodes.
A 10-dimensional composed of 18 9-dimensional-cubes …

This program generates incrementally the number of each n-cube (and nodes, dimension 0) present in n-cubes.


## The original objective

The project has been created to see if a pattern was present on the maximal number of objects
(that's why some elements are highlighted).


## Implementation details

Should keep a really low memory footprint, even when querying tons of elements.

```
usage: hdim.py [-h] [--cell-size SIZE] [--raw] [--no-highlight] [--force] [max_dim]

Compute size data about tesseract and other n-dimensional-cubes

positional arguments:
  max_dim             Maximum dimension cardinality, horizontal fill if set to 0, infinite if set to -1 (default: 5)

optional arguments:
  -h, --help          show this help message and exit
  --cell-size SIZE    Maximum cell size for display, '0' means auto (default: 0)
  --raw, -r           Sets cell size to 1 and disable highlights (default: False)
  --no-highlight, -c  Do not highlight elements (default: False)
  --force, -f         Run, even if it breaks display (default: False)
```

```
./hdim.py 14
      1
      2       1
      4       4       1
      8      12       6       1
     16      32      24       8       1
     32      80      80      40      10       1
     64     192     240     160      60      12       1
    128     448     672     560     280      84      14       1
    256    1024    1792    1792    1120     448     112      16       1
    512    2304    4608    5376    4032    2016     672     144      18       1
   1024    5120   11520   15360   13440    8064    3360     960     180      20       1
   2048   11264   28160   42240   42240   29568   14784    5280    1320     220      22       1
   4096   24576   67584  112640  126720  101376   59136   25344    7920    1760     264      24       1
   8192   53248  159744  292864  366080  329472  219648  109824   41184   11440    2288     312      26       1
```


## Next

I don't know, just sharing, create issues if you have any ideas ; or even better: open merge requests.

If people ask for it, I could:

- start by providing a proper packaging
- add Windows compatibility (with little help to test)
- add some headings in the output
- add an index on each row
