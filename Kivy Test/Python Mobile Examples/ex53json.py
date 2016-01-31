#ex53json.py
import json
A=[
    { "type": "title",
      "title": "Shape"},
    
    { "type": "bool",
      "title": "Circle",
      "key": "circle",
      "section": "shape"},

    { "type": "bool",
      "title": "Square",
      "key": "square",
      "section": "shape"},

    { "type": "bool",
      "title": "Up Triangle",
      "key": "up_triangle",
      "section": "shape"},

    { "type": "bool",
      "title": "Down Triangle",
      "key": "down_triangle",
      "section": "shape"},

    { "type": "title",
      "title": "Size"},

    { "type": "numeric",
      "title": "Pixels",
      "key": "pixels",
      "section": "size",
      "desc": "Size of shapes"}
]
json_data = json.dumps(A)