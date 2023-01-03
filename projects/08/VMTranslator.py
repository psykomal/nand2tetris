import sys
import os

# read vm code file and parse content into a list
def parseVMCodeFile(file):
    vmCodeList = []

    with open(file, mode='r') as f:
        lines = f.read().splitlines()
        for line in lines:
            if not line: # ignore empty lines
                continue
            elif line[0:2] == '//': # ignore lines with comment comes first
                continue
            else:
                if '//' in line:
                    line = line.split('//')[0]
                    vmCodeList.append(line.strip()) # ignore comments inside a line
                else:
                    vmCodeList.append(line.strip())
    
    return vmCodeList

# main algorithm for generating Hack assembly program into a list
def generateHackAssembly(vmCodeList, fileName, addComment, translationHelperData):
    # transfer VM add command into Hack assembly code
    def transferAdd():
        hackAssemblyElementList = [    
            '@SP',
            'M=M-1',
            'A=M',
            'D=M',
            '@SP',
            'M=M-1',
            'A=M',
            'M=D+M',         
            '@SP',
            'M=M+1',
        ]

        return hackAssemblyElementList
    
    # transfer VM sub command into Hack assembly code
    def trasferSub():
        hackAssemblyElementList = [
            '@SP',
            'M=M-1',
            'A=M',
            'D=M',
            '@SP',
            'M=M-1',
            'A=M',
            'M=M-D',
            '@SP',
            'M=M+1',
        ]

        return hackAssemblyElementList

    # transfer VM neg command into Hack assembly code
    def transferNeg():
        hackAssemblyElementList = [
            '@SP',
            'M=M-1',
            'A=M',
            'D=-M',
            'M=D',
            '@SP',
            'M=M+1',
        ]

        return hackAssemblyElementList

    # transfer VM eq command into Hack assembly code
    def transferEq(customLabelIndex):
        hackAssemblyElementList = [
            '@SP',
            'M=M-1',
            'A=M',
            'D=M',
            '@SP',
            'M=M-1',
            'A=M',
            'D=D-M',
            '@EQUAL'+ customLabelIndex,
            'D;JEQ',
            'D=0',
            '@FINAL'+ customLabelIndex,
            '0;JEQ',
            '(EQUAL'+ customLabelIndex +')',
            'D=-1',
            '(FINAL'+ customLabelIndex +')',
            '@SP',
            'A=M',
            'M=D',
            '@SP',
            'M=M+1',
        ]

        return hackAssemblyElementList

    # transfer VM gt command into Hack assembly code
    def transferGt(customLabelIndex):
        hackAssemblyElementList = [
            '@SP',
            'M=M-1',
            'A=M',
            'D=M',
            '@SP',
            'M=M-1',
            'A=M',
            'D=M-D',
            '@GREATER_THAN'+ customLabelIndex,
            'D;JGT',
            'D=0',
            '@END'+ customLabelIndex,
            '0;JEQ',
            '(GREATER_THAN'+ customLabelIndex +')',
            'D=-1',
            '(END'+ customLabelIndex +')',
            '@SP',
            'A=M',
            'M=D',
            '@SP',
            'M=M+1',
        ]

        return hackAssemblyElementList

    # transfer VM lt command into Hack assembly code
    def transferLt(customLabelIndex):
        hackAssemblyElementList = [
            '@SP',
            'M=M-1',
            'A=M',
            'D=M',
            '@SP',
            'M=M-1',
            'A=M',
            'D=M-D',
            '@LESS_THAN'+ customLabelIndex,
            'D;JLT',
            'D=0',
            '@END'+ customLabelIndex,
            '0;JEQ',
            '(LESS_THAN'+ customLabelIndex +')',
            'D=-1',
            '(END'+ customLabelIndex +')',
            '@SP',
            'A=M',
            'M=D',
            '@SP',
            'M=M+1',
        ]

        return hackAssemblyElementList

    # transfer VM and command into Hack assembly code
    def transferAnd():
        hackAssemblyElementList = [
            '@SP',
            'M=M-1',
            'A=M',
            'D=M',
            '@SP',
            'M=M-1',
            'A=M',
            'D=D&M',
            'M=D',
            '@SP',
            'M=M+1',
        ]

        return hackAssemblyElementList

    # transfer VM or command into Hack assembly code
    def transferOr():
        hackAssemblyElementList = [
            '@SP',
            'M=M-1',
            'A=M',
            'D=M',
            '@SP',
            'M=M-1',
            'A=M',
            'D=D|M',
            'M=D',
            '@SP',
            'M=M+1',
        ]

        return hackAssemblyElementList

    # transfer VM not command into Hack assembly code
    def transferNot():
        hackAssemblyElementList = [
            '@SP',
            'M=M-1',
            'A=M',
            'D=!M',
            'M=D',
            '@SP',
            'M=M+1',
        ]

        return hackAssemblyElementList

    # transfer VM push command into Hack assembly code
    def transferPush(memorySegmentDict, memorySegmentAccess, fileName, offset):
        hackAssemblyElementList = []

        
        if 'constant' in parsedCode:
            # \*SP = i, SP++
            hackAssemblyElementList = [
                '@' + offset,
                'D=A',
                '@SP',
                'A=M',
                'M=D',
                '@SP',
                'M=M+1',
            ]
        elif memorySegmentAccess in memorySegmentDict.keys():
            # addr = segmentPointer + i, *SP = *addr, SP++
            hackAssemblyElementList = [
                '@' + offset,
                'D=A',
                '@' + memorySegmentDict[memorySegmentAccess],
                'A=D+M',
                'D=M',
                '@SP',
                'A=M',
                'M=D',
                '@SP',
                'M=M+1',
            ]
        elif 'temp' in parsedCode:
            # addr = 5 + i, *SP = *addr, SP++
            hackAssemblyElementList = [
                '@' + offset,
                'D=A',
                '@5',
                'A=D+A',
                'D=M',
                '@SP',
                'A=M',
                'M=D',
                '@SP',
                'M=M+1',
            ]
        elif 'pointer' in parsedCode:
            # \*SP = THIS/THAT, SP++
            if offset == '0':
                accessor = 'THIS'
            else:
                accessor = 'THAT'
            hackAssemblyElementList = [
                '@' + accessor,
                'D=M',
                '@SP',
                'A=M',
                'M=D',
                '@SP',
                'M=M+1',
            ]
        elif 'static' in parsedCode:
            hackAssemblyElementList = [
                '@' + fileName + '.' + offset,
                'D=M',
                '@SP',
                'A=M',
                'M=D',
                '@SP',
                'M=M+1',
            ]
    
        return hackAssemblyElementList

    # transfer VM pop command into Hack assembly code
    def transferPop(memorySegmentDict, memorySegmentAccess, fileName, offset):
        hackAssemblyElementList = []

        
        if memorySegmentAccess in memorySegmentDict.keys():
            # addr = segmentPointer + i, SP--, *addr = *SP
            hackAssemblyElementList = [
                '@' + offset,
                'D=A',
                '@' + memorySegmentDict[memorySegmentAccess],
                'D=D+M',
                '@frame',
                'M=D',
                '@SP',
                'M=M-1',
                'A=M',
                'D=M',
                '@frame',
                'A=M',
                'M=D',
            ]
        elif 'temp' in parsedCode:
            # addr = 5 + i, SP--, *addr = *SP
            hackAssemblyElementList = [
                '@' + offset,
                'D=A',
                '@5',
                'D=D+A',
                '@frame',
                'M=D',
                '@SP',
                'M=M-1',
                'A=M',
                'D=M',
                '@frame',
                'A=M',
                'M=D',
            ]
        elif 'pointer' in parsedCode:
            # SP--, THIS/THAT = *SP
            if offset == '0':
                accessor = 'THIS'
            else:
                accessor = 'THAT'
            hackAssemblyElementList = [
                '@SP',
                'M=M-1',
                'A=M',
                'D=M',
                '@' + accessor,
                'M=D',
            ]
        elif 'static' in parsedCode:
            hackAssemblyElementList = [
                '@SP',
                'M=M-1',
                'A=M',
                'D=M',
                '@' + fileName + '.' + offset,
                'M=D',
            ]
    
        return hackAssemblyElementList

    # transfer VM label command into Hack assembly code
    def transferLabel(labelName, functionList):
        hackAssemblyElementList = []            

        
        if len(functionList) > 0:
            functionName = functionList[-1]
            hackAssemblyElementList = [
                '(' + functionName + '$' + labelName + ')',
            ]
        else:
            hackAssemblyElementList = [ 
                '('+ labelName + ')', 
            ]
        
        return hackAssemblyElementList

    # transfer VM if-goto command into Hack assembly code
    def transferIfGoto(labelName, functionList):
        hackAssemblyElementList = [
            '@SP',
            'M=M-1',
            'A=M',
            'D=M',
        ]
        if len(functionList) > 0:
            functionName = functionList[-1]
            hackAssemblyElementList.append('@' + functionName + '$' + labelName)
        else:
            hackAssemblyElementList.append("@" + labelName)
        hackAssemblyElementList.append("D;JNE")

        return hackAssemblyElementList

    # transfer VM goto command into Hack assembly code
    def transferGoto(code, functionList):
        hackAssemblyElementList = []

        
        if len(functionList) > 0:
            functionName = functionList[-1]
            hackAssemblyElementList.append('@' + functionName + '$' + labelName)
        else:
            hackAssemblyElementList.append("@" + labelName)
        hackAssemblyElementList.append("0;JMP")

        return hackAssemblyElementList

    # transfer VM function command into Hack assembly code
    def transferFunction(functionName, numberOfVariables):
        hackAssemblyElementList = []

        
        hackAssemblyElementList.append("(" + functionName +")")
        for _ in range(numberOfVariables):
            hackAssemblyElementList += [
                '@0',
                'D=A',
                '@SP',
                'A=M',
                'M=D',
                '@SP',
                'M=M+1',
            ]

        return hackAssemblyElementList

    # transfer VM return command into Hack assembly code
    def transferReturn():
        hackAssemblyElementList = [
            # endFrame = LCL // endFrame is a temporary variable
            "@LCL",
            "D=M",
            "@frame",
            "M=D",
            # retAddr = *(endFrame - 5) // gets the return address
            "@5",
            'D=D-A',
            'A=D',
            "D=M",
            "@return",
            "M=D",
            # *ARG = pop()  // repositions the return value for the caller
            "@SP",
            "M=M-1",
            "A=M",
            "D=M",
            "@ARG",
            "A=M",
            "M=D",
            # SP = ARG + 1 // repositions SP of the caller
            "@ARG",
            "D=M+1",
            "@SP",
            "M=D",
            # THAT = *(endFrame - 1) // restores THAT of the caller
            "@frame",
            "D=M",
            "@1",
            'D=D-A',
            #'D=D-1',
            'A=D',
            "D=M",
            "@THAT",
            "M=D",
            # THIS = *(endFrame - 2) // restores THIS of the caller
            "@frame",
            "D=M",
            "@2",
            'D=D-A',
            'A=D',
            "D=M",
            "@THIS",
            "M=D",
            # ARG = *(endFrame - 3) // restores ARG of the caller
            "@frame",
            "D=M",
            "@3",
            'D=D-A',
            'A=D',
            "D=M",
            "@ARG",
            "M=D",
            # LCL = *(endFrame - 4) // restores LCL of the caller
            "@frame",
            "D=M",
            "@4",
            'D=D-A',
            'A=D',
            "D=M",
            "@LCL",
            "M=D",
            # goto retAddr // goes to return address in the caller's code
            "@return",
            "A=M",
            "0;JMP",
        ]

        return hackAssemblyElementList

    # transfer VM call command into Hack assembly code
    def transferCall(functionName, numberOfArguments, functionLabelIndex):
        hackAssemblyElementList = [
            # push return address
            '@'+ functionName + '$ret.' + functionLabelIndex,
            'D=A',
            '@SP',
            'A=M',
            'M=D',
            '@SP',
            'M=M+1',
            # push LCL
            '@LCL',
            'D=M',
            '@SP',
            'A=M',
            'M=D',
            '@SP',
            'M=M+1',
            # push ARG
            '@ARG',
            'D=M',
            '@SP',
            'A=M',
            'M=D',
            '@SP',
            'M=M+1',
            # push THIS
            '@THIS',
            'D=M',
            '@SP',
            'A=M',
            'M=D',
            '@SP',
            'M=M+1',
            # push THAT
            '@THAT',
            'D=M',
            '@SP',
            'A=M',
            'M=D',
            '@SP',
            'M=M+1',
            # ARG = SP - 5 - number of arguments
            'D=M',
            "@" + str(5+numberOfArguments),
            'D=D-A',
            '@ARG',
            'M=D',
            # LCL = SP
            '@SP',
            'D=M',
            '@LCL',
            'M=D',
            # goto functionName
            '@' + functionName,
            '0;JMP',
            # (return address)
            '('+ functionName +'$ret.' + functionLabelIndex + ')',
        ]

        return hackAssemblyElementList

    hackAssemblyList = []
    memorySegmentDict = {"local": "LCL", "argument": "ARG", "this": "THIS", "that": "THAT"}

    for code in vmCodeList:
        VMCommand = code.split(' ')[0]
        hackAssemblyElementList = ['//' + code] if addComment else []

        if 'add' == VMCommand:
            hackAssemblyElementList += transferAdd()
        elif 'sub' == VMCommand:
            hackAssemblyElementList += trasferSub()
        elif 'neg' == VMCommand:
            hackAssemblyElementList += transferNeg()
        elif 'eq' == VMCommand:
            hackAssemblyElementList += transferEq(str(translationHelperData["customLabelIndex"]))
            translationHelperData["customLabelIndex"] += 1
        elif 'gt' == VMCommand:
            hackAssemblyElementList += transferGt(str(translationHelperData["customLabelIndex"]))
            translationHelperData["customLabelIndex"] += 1
        elif 'lt' == VMCommand:
            hackAssemblyElementList += transferLt(str(translationHelperData["customLabelIndex"]))
            translationHelperData["customLabelIndex"] += 1
        elif 'and' == VMCommand:
            hackAssemblyElementList += transferAnd()
        elif 'or' == VMCommand:
            hackAssemblyElementList += transferOr()
        elif 'not' == VMCommand:
            hackAssemblyElementList += transferNot()
        elif 'push' == VMCommand:
            parsedCode = code.split(" ")
            memorySegmentAccess = parsedCode[1]
            offset = str(parsedCode[-1])

            hackAssemblyElementList += transferPush(memorySegmentDict, memorySegmentAccess, fileName, offset)
        elif 'pop' == VMCommand:
            parsedCode = code.split(" ")
            memorySegmentAccess = parsedCode[1]
            offset = str(parsedCode[-1])

            hackAssemblyElementList += transferPop(memorySegmentDict, memorySegmentAccess, fileName, offset)
        elif 'label' == VMCommand:
            parsedCode = code.split(" ")
            labelName = parsedCode[-1]

            hackAssemblyElementList += transferLabel(labelName, translationHelperData["functionList"])
        elif 'if-goto' == VMCommand:
            parsedCode = code.split(" ")
            labelName = parsedCode[-1]

            hackAssemblyElementList += transferIfGoto(labelName, translationHelperData["functionList"])
        elif 'goto' == VMCommand:
            parsedCode = code.split(" ")
            labelName = parsedCode[-1]

            hackAssemblyElementList += transferGoto(labelName, translationHelperData["functionList"])
        elif 'function' == VMCommand:
            parsedCode = code.split(" ")
            functionName = parsedCode[1]
            translationHelperData["functionList"].append(functionName)
            numberOfVariables = int(parsedCode[-1])

            hackAssemblyElementList += transferFunction(functionName, numberOfVariables)
        elif 'return' == VMCommand:
            hackAssemblyElementList += transferReturn()
            translationHelperData["functionList"].pop()
        elif 'call' == VMCommand:
            parsedCode = code.split(' ')
            functionName = parsedCode[1]
            numberOfArguments = int(parsedCode[-1])

            hackAssemblyElementList += transferCall(functionName, numberOfArguments, str(translationHelperData["functionLabelIndex"]))
            translationHelperData["functionLabelIndex"] += 1
        
        hackAssemblyList += hackAssemblyElementList

    # if len(translationHelperData["functionList"]) > 0:
        

    return hackAssemblyList
                    
# booting code for Hack computer
def generateBootstrapCode(addComment):
    hackAssemblyElementList = [
        # SP=256
        '@256',
        'D=A',
        '@SP',
        'M=D',
        # call Sys.init
        # push return address
        '@Bootstrap$ret',
        'D=A',
        '@SP',
        'A=M',
        'M=D',
        '@SP',
        'M=M+1',
        # push LCL
        '@LCL',
        'D=M',
        '@SP',
        'A=M',
        'M=D',
        '@SP',
        'M=M+1',
        # push ARG
        '@ARG',
        'D=M',
        '@SP',
        'A=M',
        'M=D',
        '@SP',
        'M=M+1',
        # push THIS
        '@THIS',
        'D=M',
        '@SP',
        'A=M',
        'M=D',
        '@SP',
        'M=M+1',
        # push THAT
        '@THAT',
        'D=M',
        '@SP',
        'A=M',
        'M=D',
        '@SP',
        'M=M+1',
        # ARG = SP - 5
        '@SP',
        'D=M',
        '@5',
        'D=D-A',
        '@ARG',
        'M=D',
        # LCL = SP
        '@SP',
        'D=M',
        '@LCL',
        'M=D',
        # goto functionName
        '@Sys.init',
        '0;JMP',
        # (return address)
        '(Bootstrap' +'$ret)',
    ]
    return hackAssemblyElementList

# write hack assembly program into a file
def writeHackAssemblyToFile(fileName, hackAssemblyList):
    outputFileName = fileName + '.asm'

    with open(outputFileName, mode='w') as f:
        for line in hackAssemblyList:
            f.write(line + '\n')

def main():
    if len(sys.argv) == 2:
        addComment = True
        translationHelperData = {
            "customLabelIndex": 0,
            "functionLabelIndex": 0,
            "functionList": []
        }

        if sys.argv[1].endswith(".vm"):
            # read vm code file and parse content into a list
            vmCodeFile = sys.argv[1]
            fileName = vmCodeFile.split('/')[-1].split('.')[0]
            vmCodeList = parseVMCodeFile(vmCodeFile)

            # main algorithm for generating Hack assembly program into a list
            hackAssemblyList = generateHackAssembly(vmCodeList, fileName, addComment, translationHelperData)
        else:
            # read each vm code file in a directory
            vmCodeDirectory = sys.argv[1]
            hackAssemblyList =  generateBootstrapCode(addComment)
            
            for fileName in os.listdir(vmCodeDirectory):
                if fileName.endswith(".vm"):
                    vmCodeList = parseVMCodeFile(vmCodeDirectory + '/' + fileName)
                    fileName = fileName.split('.')[0]

                    # main algorithm for generating Hack assembly program into a list
                    hackAssemblyList += generateHackAssembly(vmCodeList, fileName, addComment, translationHelperData)

        # write hack assembly program into a file
        if sys.argv[1].endswith(".vm"):
            destinationFileName = sys.argv[1].split(".")[0]
        else:
            destinationDirectory = sys.argv[1]
            destinationFileName = destinationDirectory + '/' + destinationDirectory.split('/')[-1] # destination directory as file name
        writeHackAssemblyToFile(destinationFileName, hackAssemblyList)
    else:
        print("Usage: python VMTranslator.py [VMCodeFile].vm or python VMTranslator.py [VMDirectory]")

if __name__ == "__main__":
    main()