from glob import glob as G
from xml.dom import minidom as xdmd
import argparse, os

settingsDictionary = {"combine": True,
                      "scale by": "1.0000000000000000",
                      "compression tolerance": "0.01000000",
                      "auto compression tolerance": False,
                      "use uniform spacing": False,
                      "uniform spacing": "0.01000000",
                      "exclude intensity": False,
                      "exclude rgb": False,
                      "exclude normals": False,
                      "generate normals": False,
                      "rescale intensities": False,
                      "exclude classification": True,
                      "8bit colour": False}

def pointFile(ptCloudIndv):
	fileElement = xmld.createElement("setting")
	fileElement.setAttribute("name", "file")
	cdata = xmld.createCDATASection(ptCloudIndv)
	fileElement.appendChild(cdata)
	return fileElement

def initPBPXMLDoc():
	global xmld
	xmld = xdmd.Document()
	pbpElement = xmld.createElement("pbp")
	pbpElement.setAttribute("version", "1.0")
	batchElement = xmld.createElement("batch")
	xmld.appendChild(pbpElement)
	pbpElement.appendChild(batchElement)
	importElement = xmld.createElement("import")
	exportElement = xmld.createElement("export")
	batchElement.appendChild(importElement)
	batchElement.appendChild(exportElement)

def exportSection(ptCloudDir):
	exportElement = xmld.getElementsByTagName("export")[0]
	exportElement.appendChild(pointFile(ptCloudDir + "podex.pod"))
	settingsElement = xmld.createElement("setting")
	settingsElement.setAttribute("name", "pod export type")
	valueNode = xmld.createTextNode("2")
	settingsElement.appendChild(valueNode)
	exportElement.appendChild(settingsElement)	
	
def importLoop(ptCloudList):
	importElement = xmld.getElementsByTagName("import")[0]
	for i in ptCloudList:
		importElement.appendChild(pointFile(i))

def otherSettings():
	importElement = xmld.getElementsByTagName("import")[0]
	for i in settingsDictionary.keys():
		settingsElement = xmld.createElement("setting")
		settingsElement.setAttribute("name", i)
		if type(settingsDictionary[i]) == bool:
			valueNode = xmld.createTextNode(str(settingsDictionary[i]).lower())
		elif type(settingsDictionary[i]) == float:
			valueNode = xmld.createTextNode(str(settingsDictionary[i]))
		else:
			"uh oh" #FIX THIS
		importElement.appendChild(valueNode)

def saveFile():
	fns = ptCloudDir + "pod-convert-config.pbp"
	f = open(fns, "w")
	f.write(xmld.toprettyxml())
	f.close()
		
def cmdLineArgs():
	parser = argparse.ArgumentParser(description="create a pbp document for Bentley Pod Creator")
	parser.add_argument("-d", "--directory", help="Where are all the point cloud files")
	parser.add_argument("-t", "--type", help="What kind of point cloud file? las or laz")
	##Less changed options, can be changed when the program is opened
	# parser.add_argument("-us", "uniform spacing", default="0.01")
	# parser.add_argument("-c", "8bit colour", default="False")
	# parser.add_argument("-act", "auto compression tolerance", default="False")
	# parser.add_argument("-s", "scale by", default="1.0")
	# parser.add_argument("-co", "combine", default="True")
	# parser.add_argument("-gn", "generate normals", default="False")
	# parser.add_argument("-ct", "compression tolerance", default="0.01")
	# parser.add_argument("-ec", "exclude classification", default="True")
	# parser.add_argument("-en", "exclude normals", default="False")
	# parser.add_argument("-uus", "use uniform spacing", default="False")
	# parser.add_argument("-ei", "exclude intensity", default="False")
	# parser.add_argument("-rgb", "exclude rgb", default="False")
	# parser.add_argument("-ri", "rescale intensities", default="False")
	args = parser.parse_args()
	dir = args.directory + os.sep
	ptCloudType = args.type
	main(dir, ptCloudType)
	
def main(ptCloudDir, ptCloudType):
	initPBPXMLDoc()
	ptCloudList = G(ptCloudDir + "*.%s" % (ptCloudType))
	importLoop(ptCloudList)
	otherSettings()
	exportSection(ptCloudDir)
	
	
cmdLineArgs()
