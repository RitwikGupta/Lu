import sys

if len(sys.argv) != 4:
	sys.stderr.write("The proper usage of this program is 'python normalExpressionExtractor.py [NormalSampleList] [ExpressionMatrix] [OutputFile]'\n")
	sys.exit()

normal = open(sys.argv[1], "r")
matrix = open(sys.argv[2], "r")				
out = open(sys.argv[3], "w")

header = matrix.readline()
out.write(header)

matDict = {}

for matLine in matrix:
	matDict[str(matLine[:matLine.find("\t")])] = str(matLine[matLine.find("\t"):])

for line in normal:
	if line.strip() in matDict.keys():
		out.write(line.strip() + matDict[line.strip()])

normal.close()
matrix.close()
out.close()