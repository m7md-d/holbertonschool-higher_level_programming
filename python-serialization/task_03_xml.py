#!/usr/bin/python3
"""
3. Serializing and Deserializing with XML
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    It takes a Python dictionary and a filename as parameters.
    """
    root = ET.Element("data")
    for i, j in dictionary.items():
        tmp = ET.SubElement(root, i)
        tmp.text = j
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    It takes a filename as its parameter, read the XML data from that file,
    and return a deserialized Python dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    data = {}
    for i in root:
        data[i.tag] = i.text
    return data
