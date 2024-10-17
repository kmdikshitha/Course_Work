def spiritualArithmetic(incantation):
    def applyOperation(operator, secondOperand, firstOperand):
        if operator == '+':
            return firstOperand + secondOperand
        elif operator == '-':
            return firstOperand - secondOperand
        elif operator == '*':
            return firstOperand * secondOperand
        elif operator == '/':
            return int(firstOperand / secondOperand)

    stack = []
    
    for token in incantation:
        if token in {'+', '-', '*', '/'}:
            stack.append(applyOperation(token, stack.pop(), stack.pop()))
        else:
            stack.append(int(token))
    
    finalAns = stack[0]
    return finalAns

# incantations =  ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# print(spiritualArithmetic(incantations))