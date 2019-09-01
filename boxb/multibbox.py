from .bbox import BBox


class MultiBBox(object):

    def clone(self):
        res = []
        for bbox in self.arr:
            res.append(bbox.clone())
        return res

    def __add__(self, other):
        if not isinstance(other, BBox):
            raise TypeError("Bounding box should be of type BBox")
        if other.empty():
            return self.clone()
        res = [other]
        for bbox in self.arr:
            res += bbox.subtract(other)
        return res

    def __sub__(self, other):
        if not isinstance(other, BBox):
            raise TypeError("Bounding box should be of type BBox")
        if other.empty():
            return self.clone()
        res = []
        for bbox in self.arr:
            res += bbox.subtract(other)
        return res

    def add_bbox(self, other):
        self.arr = self.__add__(other)

    def remove_bbox(self, other):
        self.arr = self.__sub__(other)

    def __init__(self, arr=None):
        if not isinstance(arr, list) and not isinstance(arr, tuple):
            raise TypeError("invalid bounding boxes")
        self.arr = []
        if arr:
            for bbox in arr:
                if not isinstance(bbox, BBox):
                    raise TypeError("Bounding boxes should be of type BBox")

    def to_json(self):
        return {"type": "MultiBBox", "coords": [list(bbox.arr) for bbox in self.arr]}

    @staticmethod
    def from_json(obj):
        if not isinstance(obj, dict) or obj.get("type") != "MultiBBox" or not obj.get("coords"):
            raise ValueError("Invalid multi-bbox json")
        res = []
        for coords in obj["coords"]:
            res.append(BBox(coords))
        return MultiBBox(res)
