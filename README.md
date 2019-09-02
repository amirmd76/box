# BoxB
Python 2D bounding box library and utilities.

## Install
```shell script
pip install boxb
```

## Usages

```pythonstub
from boxb import BBox, MultiBBox
bbox = BBox([20, 40, 30, 50])
coords = bbox.arr
print(coords) 
>>> [20.0, 40.0, 30.0, 50.0]

bbox2 = BBox([10, 30, 25, 45])
multi_bbox = MultiBBox([bbox, bbox2])
print(multi_bbox)
>>> MultiBBox([BBox([10.0, 30.0, 25.0, 45.0]), BBox([25.0, 40.0, 30.0, 50.0]), BBox([20.0, 45.0, 25.0, 50.0])])

multi_bbox_2 = MultiBBox(bbox)
multi_bbox_2.add_bbox(bbox2) # or multi_bbox_2 += bbox2
print(multi_bbox.equals(multi_bbox_2))
>>> True

bbox_sub = bbox.subtract(bbox2) # returns list of BBox
multi_bbox_3 = MultiBBox(bbox_sub)
print(multi_bbox_3)
>>> MultiBBox([BBox([20.0, 45.0, 25.0, 50.0]), BBox([25.0, 40.0, 30.0, 50.0])])

multi_bbox_4 = MultiBBox(bbox)
multi_bbox_4.remove_bbox(bbox2) # or multi_bbox_4 -= bbox2
print(multi_bbox_3.equals(multi_bbox_4))
>>> True

from boxb import loads, dumps
print(dumps(multi_bbox_4))
>>> {"type": "MultiBBox", "coords": [[25.0, 40.0, 30.0, 50.0], [20.0, 45.0, 25.0, 50.0]]}
multi_bbox_5 = loads(dumps(multi_bbox_4))
print(multi_bbox_4.equals(multi_bbox_5))
>>> True
```

## API Reference

`boxb.loads`: Load BBox/MultiBBox from JSON string

`boxb.load`: Load BBox/MultiBBox from JSON file

`boxb.dumps`: Dump BBox/MultiBBox to JSON string

`boxb.dump`: Dump BBox/MultiBBox to JSON file

`boxb.BBox`: Bounding box object. 

BBox Methods:
- `__init__(arr=None)`: Construct from None (empty), list or tuple of 4 floats/integers
- `clone()`: Returns a replica of the BBox
- `empty()`: Is the BBox empty? return boolean
- `intersect(bbox)`: Returns intersection with another BBox as a BBox
- `union(bbox)`: Returns the smallest bounding box containing both bounding boxes as a BBox
- `contains(bbox)`: Does this BBox contain bbox? return boolean
- `subtract(bbox)`: Exclude bbox from this BBox, returns a list of BBoxes (possibly empty)
- `equals(bbox):` Does this BBox equal BBox? returns a boolean
- `to_json()`: Converts the BBox to a JSON-serializable object, returns a dict
- `from_json()`: Converts a JSON-serializable object of format `{"type": "BBox", "coords": [x, y, z, t]}` to a BBox, returns the BBox

BBox Properties:
- `arr`: List of coordinates (of length 4)

`boxb.MultiBBox`: An object representing multiple non-intersecting bounding boxes
MultiBBox Methods:
- `__init__(arr=None)`: Construct from None (empty), list or tuple of BBoxes, MultiBBox or a single BBox and transforms them into non-intersecting BBoxes
- `clone()`: Returns a replica of the MultiBBox
- `empty()`: Is the MultiBBox empty? return boolean
- `__add__(other)` (+ operation): Adds a BBox/MultiBBox to the MultiBBox and returns the resulting MultiBBox
- `add_bbox(other)`: Equivalent of +=
- `__sub__(other)` (- operation): Excludes a BBox/MultiBBox from the current MultiBBox and returns the resulting MultiBBox
- `equals(bbox):` Does this MultiBBox equal BBox? returns a boolean
- `to_json()`: Converts the MultiBBox to a JSON-serializable object, returns a dict
- `from_json()`: Converts a JSON-serializable object of format `{"type": "MultiBBox", "coords": [[x, y, z, t], [a, b, c, d]]}` to a MultiBBox, returns the MultiBBox

MultiBBox Properties:
- `arr`: List of BBoxes (of any length), guaranteed to be non-intersecting unless manipulated manually