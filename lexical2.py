KEYWORDS = ("break","case","char","const","do","else","enum","float","for","if","int","double long","struct","return","static","while")
OPERATORS = ('+','-','*','/','++','--','==','<','>','<=','>=','=')
BRACKETS = {'(':" LeftPar",')':"RightPar",'{':" LeftCurlyBracket",'}':"RightCurlyBracket"}
COMMENTS = ("/*","*/","//")

Stack = list()


tempStack = list()
def lex_analiyser(line):
    for keyword in KEYWORDS:
        if keyword in line:
            Stack.append(keyword)
    for operator in OPERATORS:
        if operator in line:
            Stack.append(operator)
    for bracket in list(BRACKETS.keys()):
        if bracket in line:
            Stack.append(bracket)
    if ';' in line:
        Stack.append(';')
    for comment in COMMENTS:
        if comment in line:
            Stack.append(comment)
    
    for char in line:
        tempStack.append(char)
        for element in Stack:
            if element in tempStack:
                tempStack.remove(element)
                
    
def main():
    file = open("code_file.ceng","r")
    lines = file.readlines()
    
    for line in lines:
        line = line.replace('\n','')
        lex_analiyser(line)
    
        
        
        
if __name__ == '__main__':
    main()