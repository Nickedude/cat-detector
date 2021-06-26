import os
import random
from typing import Tuple

import cv2
import xmltodict

class BoundingBox:

    def __init__(self, xmin: int, xmax: int, ymin: int, ymax: int):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax


def _read_annotation(annotation_path: str) -> BoundingBox:
    with open(annotation_path, "rt") as file:
        annotation = xmltodict.parse(file.read())

    bbox = annotation["annotation"]["object"]["bndbox"]


    return BoundingBox(int(bbox["xmin"]), int(bbox["xmax"]), int(bbox["ymin"]), int(bbox["ymax"]))


def _draw_bbox(img, bbox: BoundingBox):
    """Draw the bounding box in the image."""
    p1 = bbox.xmin, bbox.ymin
    p2 = bbox.xmax, bbox.ymax

    color = 255
    thickness = 5

    cv2.rectangle(img, p1, p2, color, thickness)


def main():
    """Show some randomly selected annotated images."""
    all_annotations = os.listdir("annotations/annotations/xmls")
    annotations = random.sample(all_annotations, k=5)

    for annotation_file in annotations:
        path = os.path.join("annotations/annotations/xmls", annotation_file)
        bbox = _read_annotation(path)

        name, _ = os.path.splitext(annotation_file)
        img_file = os.path.join("images/images", f"{name}.jpg")

        img = cv2.imread(img_file)
        _draw_bbox(img, bbox)
        cv2.imshow(name, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
