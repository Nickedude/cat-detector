import os
import xmltodict

class BoundingBox:
    """Class to represent a bounding box."""

    def __init__(self, xmin: int, xmax: int, ymin: int, ymax: int):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax


class Annotation:
    """An annotation with a bounding box and a class."""

    def __init__(self, bbox: BoundingBox, cls: str):
        self.bbox = bbox
        self.cls = cls



def parse_annotation(annotation_path: str) -> Annotation:
    """Read and parse annotation given a path."""
    if os.path.splitext(annotation_path)[1] != ".xml":
        raise ValueError("Annotation must be .xml file.")

    with open(annotation_path, "rt") as file:
        annotation = xmltodict.parse(file.read())

    obj = annotation["annotation"]["object"]
    bbox = obj["bndbox"]
    bbox = BoundingBox(int(bbox["xmin"]), int(bbox["xmax"]), int(bbox["ymin"]), int(bbox["ymax"]))

    return Annotation(bbox, obj["name"])