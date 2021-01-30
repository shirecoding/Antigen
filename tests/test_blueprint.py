import logging
import os
import re
import tempfile

import pytest

log = logging.getLogger(__name__)


@pytest.mark.report(
    specification="""
    """,
    procedure="""
    """,
    expected="""
    """,
)
def test_valid_component():
    """
    Test component validation function
    """
    from antigen import component_is_valid, components_dir, create_component

    c1 = {
        "component": "TextField",
        "id": "TextField1",
        "props": {},
        "children": "Hello World",
    }

    assert component_is_valid(c1) == True

    c2 = {"id": "TextField1", "props": {}, "children": "Hello World"}

    assert component_is_valid(c2) == False


@pytest.mark.report(
    specification="""
    """,
    procedure="""
    """,
    expected="""
    """,
)
def test_create_component():
    """
    Test component creation function
    """

    from antigen import components_dir, create_component

    c1 = {
        "component": "TextField",
        "id": "TextField1",
        "props": {},
        "children": "Hello World",
    }

    with tempfile.TemporaryDirectory() as folder:
        component_path = create_component(
            c1, os.path.join(folder, "c1"), components_dir
        )

        with open(component_path, "r") as file:
            data = file.read()
            assert re.match(r"^.*id=\"TextField1\".*$", data, re.DOTALL) != None
            assert re.match(r"^.*>Hello World<.*$", data, re.DOTALL) != None
            assert re.match(r"^.*TextField\(props\).*$", data, re.DOTALL) != None
