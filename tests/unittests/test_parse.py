"""Unittests for annotation parsing."""
import pytest
from tempfile import NamedTemporaryFile


from parse import parse_annotation


class TestParseAnnotation:
    """Unittests for annotation parsing."""

    def test_missing_file(self):
        """Test that an error is raised when the file is missing."""
        with pytest.raises(FileNotFoundError):
            parse_annotation("missing.xml")

    def test_not_xml(self):
        """Test that an error is raised when the file is not an xml file."""
        annotation = NamedTemporaryFile(prefix="annotation", suffix=".txt")

        with pytest.raises(ValueError):
            parse_annotation(annotation.name)

        annotation.close()

    def test_leonberger_148(self):
        """Test parsing an annotation."""
        annotation = parse_annotation("annotations/annotations/xmls/leonberger_148.xml")

        assert annotation.cls == "dog"
        assert annotation.bbox.xmin == 270
        assert annotation.bbox.xmax == 381
        assert annotation.bbox.ymin == 17
        assert annotation.bbox.ymax == 87
