

# Lexical Analyser for Ceng#
# Programming Languages Project 1

# Project defination : The Program should accept a source file called 
# code_file.ceng and produce a text file named as code.lex that contains 
# all the tokens of the code.lex listed one after the other.


# Token words for using lexical analysis.
KEYWORDS = ("break", "case", "char", "const", "do", "else", "enum", "float"
            "for", "if", "int", "double long", "struct", "return", "static", "while")
OPERATORS = ('+', '-', '*', '/', '++', '--', '==', '<', '>', '<=', '>=', '=')
BRACKETS = {'(': "LeftPar", ')': "RightPar",
            '{': "LeftCurlyBracket", '}': "RightCurlyBracket"}
ENDOFLINE = ';'
COMMENTS = ("/*", "*/", "//")
DIGITS = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
DIGITS_MAX_LENGTH = 10
IDENTIFIER_MAX_LENGTH = 25

# Lexical analysis code file : code_file.ceng
# Lexical analysis output file : code.lex
rFile = open("code_file.ceng", "r")
wFile = open("code.lex", "w")

# Finds descriptive identifier other than tokens.

# Word matcher
def id_matcher(id):
    if id != "":
        # Matches words their tokens and, writes matching tokens to file.
        # When there are tokens that do not comply with the rule,
        # It will terminate the transaction and give a warning message.
        if id in KEYWORDS:
            print("Keyword: " + id)
            wFile.write("Keyword: " + id+"\n")
        elif id[0] in DIGITS:
            if len(id) > DIGITS_MAX_LENGTH:
                print("Error: Integer size error!!!")
                wFile.write("Error: Integer size error!!!"+"\n")
                exit(1)
            for char in id:
                if char not in DIGITS:
                    print("Error: Identifier defination error!!!")
                    wFile.write("Error: Identifier defination error!!!"+"\n")
                    exit(1)
            print("Integer Constant: " + id)
            wFile.write("Integer Constant: " + id+"\n")
        else:
            if len(id) > IDENTIFIER_MAX_LENGTH:
                print("Error: Size of identifier must lower than 25 characters!!!")
                wFile.write("Error: Size of identifier must lower than 25 characters!!!"+"\n")
                exit(1)
            print("Identifier: " + id)
            wFile.write("Identifier: " + id+"\n")

# Lexical Analyser recursive method.
def lex(line):
    # tempStr called a string like works stack.
    # When a new character is iterated from the line, it is added to tempStr.
    tempStr = ""
    # Line is enumerated for the next character check.
    for i, char in enumerate(line):
        # Beginning of Operator Condition...
        if char in OPERATORS:
            if i < len(line)-1 and line[i+1] in OPERATORS:
                opr = line[i] + line[i+1]
                # Beginning of Comment Condition....
                if opr == "//":
                    id_matcher(tempStr)
                    temp = line.split(opr, 1)
                    temp2 = temp[1].split('\n', 1)
                    print("Comment")
                    wFile.write("Comment"+"\n")
                    tempStr = ""
                    return lex(temp2[1])
                elif opr == "/*":
                    id_matcher(tempStr)
                    temp = line.split(opr, 1)
                    # Unclosed comment situation...
                    if not "*/" in temp[1]:
                        tempStr = ""
                        print("Error: Unclosed comment")
                        wFile.write("Error: Unclosed comment"+"\n")
                        exit(1)
                    else:
                        temp2 = temp[1].split("*/", 1)
                        print("Comment")
                        wFile.write("Comment"+"\n")
                        tempStr = ""
                        return lex(temp2[1])
                # End of Comment Condition...
                elif opr in OPERATORS:
                    id_matcher(tempStr)
                    print("Operator: "+opr)
                    wFile.write("Operator: "+opr+"\n")
                    temp = line.split(opr, 1)
                    tempStr = ""
                    return lex(temp[1])
                else:
                    id_matcher(tempStr)
                    print("Operator: "+char)
                    wFile.write("Operator: "+char+"\n")
                    temp = line.split(char, 1)
                    tempStr = ""
                    return lex(temp[1])
            else:
                id_matcher(tempStr)
                print("Operator: "+char)
                wFile.write("Operator: "+char+"\n")
                temp = line.split(char, 1)
                tempStr = ""
                return lex(temp[1])
        # End of Operator Condition...
        # Beginning of "End of Line" Condition...
        if char == ENDOFLINE:
            id_matcher(tempStr)
            print("End Of Line")
            wFile.write("End Of Line"+"\n")
            temp = line.split(ENDOFLINE, 1)
            tempStr = ""
            return lex(temp[1])
        # End of the "End of Line" Condition...
        # Beginning of Spacing Condition...
        if char == " ":
            id_matcher(tempStr)
            temp = line.split(' ', 1)
            tempStr = ""
            return lex(temp[1])
        # Beginning of Brackets Condition...
        if char in BRACKETS:
            id_matcher(tempStr)
            print(BRACKETS[char])
            wFile.write(BRACKETS[char]+"\n")
            temp = line.split(char, 1)
            tempStr = ""
            return lex(temp[1])
        # End of Brackets Condition...
        # Beginning of String Condition...
        if char == '"':
            id_matcher(tempStr)
            temp = line.split('"', 1)
            # Unclosed double quotes situation...
            if not '"' in temp[1]:
                tempStr = ""
                print("Error: Unclosed double quotes !!!!!")
                wFile.write("Error: Unclosed double quotes !!!!!"+"\n")
                exit(1)
            else:
                temp2 = temp[1].split('"', 1)
                print("String Constant: " + temp2[0])
                wFile.write("String Constant: " + temp2[0]+"\n")
                tempStr = ""
                return lex(temp2[1]) 
        # End of Brackets Condition...
        # Character is pushed to tempStr when it can't find token.
        tempStr += char
    # The end of 'for' loop.
    # If has the last word tempStr
    id_matcher(tempStr)
# The end of lex() function.

def main():
    line = ""
    f = rFile.readlines()
    for temp in f:
        if "//" in temp:
            arr = temp.replace("\n", "").split("//", 1)
            line += arr[0]
            line += "// "+arr[1] + "\n"
        else:
            line += temp.replace("\n", "")
    lex(line)


if __name__ == '__main__':
    main()
