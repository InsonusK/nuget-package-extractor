import xml.etree.ElementTree as ET
import os
import pathlib
import numpy as np

class NugetExtractor:
  def __init__(self, filePath):
      self.filePath = filePath

  def extract(self):
      tree = ET.parse(self.filePath)
      root = tree.getroot()
      returnArr = []
      for pack in root.iter('PackageReference'):
          packName = pack.attrib['Include']+":"+pack.attrib['Version']
          returnArr.append(packName)
      return returnArr

curDir = pathlib.Path(__file__).parent.absolute()

packArr = []
for path, subdirs, files in os.walk(curDir):
    for filename in files:
        if filename.endswith(".csproj"): 
            file = NugetExtractor(os.path.join(path, filename))
            for pack in file.extract():
                packArr.append(pack)

packArr.sort()
packArr = list(dict.fromkeys(packArr))
print("=======")
print("Result:")
print("=======")
for pack in packArr:
    print(pack)
