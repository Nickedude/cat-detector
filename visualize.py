import os
import random

import cv2

from parse import parse_annotation, BoundingBox, Annotation


def _draw_bbox(img, bbox: BoundingBox):
    """Draw the bounding box in the image."""
    p1 = bbox.xmin, bbox.ymin
    p2 = bbox.xmax, bbox.ymax

    color = 255
    thickness = 5

    cv2.rectangle(img, p1, p2, color, thickness)


def _write_class_name(img, annotation: Annotation):
    """Write the class name besides the bounding box."""
    bbox = annotation.bbox
    margin = 25

    if bbox.ymin - margin > 0:
        ypos = bbox.ymin
    else:
        ypos = bbox.ymax + margin

    pos = (bbox.xmin, ypos)

    scale = 1
    thickness = 3
    color = 255
    cv2.putText(img, annotation.cls, pos, cv2.FONT_HERSHEY_SIMPLEX, scale, color, thickness)



def main():
    """Show some randomly selected annotated images."""
    all_annotations = os.listdir("annotations/annotations/xmls")
    annotations = random.sample(all_annotations, k=5)

    for annotation_file in annotations:
        path = os.path.join("annotations/annotations/xmls", annotation_file)
        annotation = parse_annotation(path)

        name, _ = os.path.splitext(annotation_file)
        img_file = os.path.join("images/images", f"{name}.jpg")

        img = cv2.imread(img_file)
        _draw_bbox(img, annotation.bbox)
        _write_class_name(img, annotation)
        cv2.imshow(name, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
