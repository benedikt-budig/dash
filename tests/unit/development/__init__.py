import os

_dir = os.path.dirname(os.path.abspath(__file__))


def has_trailing_space(s):
    return any(line != line.rstrip() for line in s.splitlines())


expected_table_component_doc = [
    "A Table component.",
    "This is a description of the component.",
    "It's multiple lines long.",
    "",
    "Keyword arguments:",
    "",
    "- children (a list of or a singular dash component, string or number; optional)",
    "",
    "- id (string; optional)",
    "",
    "- aria-* (string; optional)",
    "",
    "- customArrayProp (list; optional)",
    "",
    "- customProp (optional)",
    "",
    "- data-* (string; optional)",
    "",
    "- in (string; optional)",
    "",
    "- optionalAny (boolean | number | string | dict | list; optional)",
    "",
    "- optionalArray (list; optional):",
    "    Description of optionalArray.  ",
    "",
    "- optionalArrayOf (list of numbers; optional)",
    "",
    "- optionalBool (boolean; optional)",
    "",
    "- optionalElement (dash component; optional)",
    "",
    "- optionalEnum (a value equal to: 'News'," " 'Photos'; optional)",
    "",
    "- optionalNode (a list of or a singular dash component, string or number; optional)",
    "",
    "- optionalNumber (number; default 42)",
    "",
    "- optionalObject (dict; optional)",
    "",
    "- optionalObjectOf (dict with strings as keys and values of type number; optional)",
    "",
    "- optionalObjectWithExactAndNestedDescription (dict; optional)  ",
    "",
    "    `optionalObjectWithExactAndNestedDescription` is a dict with keys:   ",
    "",
    "    - color (string; optional)  ",
    "",
    "    - figure (dict; optional):",
    "        Figure is a plotly graph object.    ",
    "",
    "        `figure` is a dict with keys:   ",
    "",
    "        - data (list of dicts; optional):",
    "            data is a collection of traces.    ",
    "",
    "        - layout (dict; optional):",
    "            layout describes the rest of the figure.    ",
    "",
    "    - fontSize (number; optional)",
    "",
    "- optionalObjectWithShapeAndNestedDescription (dict; optional)  ",
    "",
    "    `optionalObjectWithShapeAndNestedDescription` is a dict with keys:   ",
    "",
    "    - color (string; optional)  ",
    "",
    "    - figure (dict; optional):",
    "        Figure is a plotly graph object.    ",
    "",
    "        `figure` is a dict with keys:   ",
    "",
    "        - data (list of dicts; optional):",
    "            data is a collection of traces.    ",
    "",
    "        - layout (dict; optional):",
    "            layout describes the rest of the figure.    ",
    "",
    "    - fontSize (number; optional)",
    "",
    "- optionalString (string; default 'hello world')",
    "",
    "- optionalUnion (string | number; optional)",
]
