import xml.etree.ElementTree as ET

def compare_xml_files(file1, file2):
    tree1 = ET.parse(file1)
    tree2 = ET.parse(file2)
    root1 = tree1.getroot()
    root2 = tree2.getroot()
    if root1.tag != root2.tag:
        print("Root elements are different.")
        return
    if root1.attrib != root2.attrib:
        print("Root attributes are different.")
        return
    if root1.text != root2.text:
        print("Root text values are different.")
        return
    for child1, child2 in zip(root1, root2):
        compare_xml_files(child1, child2)

compare_xml_files(group1.xml, group2.xml)
