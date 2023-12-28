import random

#Function for evaluation
def evaluate(input):
    #Process the input
    def process_variable(variable):
        # Remove whitespaces and split the variable by '='
        parts = variable.replace(" ", "").split('=')

        # Ensure there is an equal sign and at least two parts
        if len(parts) >= 2:
            # Return the part after the equal sign
            return parts[1]
        else:
            # If no equal sign is found or only one part is present, return the original variable
            return variable
    input = process_variable(input)
    
    # Lexer
    def tokenize_expression(expression):
        tokens = []
        current_token = ""

        for char in expression:
            if char.isspace():
                continue
            elif char.isdigit() or char == ".":
                current_token += char
            else:
                if current_token:
                    tokens.append(float(current_token))
                    current_token = ""
                tokens.append(char)

        if current_token:
            tokens.append(float(current_token))

        return tokens

    # Parser
    def parse_tokens(tokens):
        index = 0

        def parse_expression():
            nonlocal index
            left_operand = parse_term()

            while index < len(tokens) and tokens[index] in ["+", "-"]:
                operator = tokens[index]
                index += 1
                right_operand = parse_term()

                if operator == "+":
                    left_operand += right_operand
                else:
                    left_operand -= right_operand

            return left_operand

        def parse_term():
            nonlocal index
            left_operand = parse_factor()

            while index < len(tokens) and tokens[index] in ["*", "/"]:
                operator = tokens[index]
                index += 1
                right_operand = parse_factor()

                if operator == "*":
                    left_operand *= right_operand
                else:
                    left_operand /= right_operand

            return left_operand

        def parse_factor():
            nonlocal index
            if tokens[index] == "(":
                index += 1
                result = parse_expression()
                index += 1
                return result
            else:
                result = tokens[index]
                index += 1
                return result

        return parse_expression()


    # Evaluator
    def evaluate_math_expression(expression):
        tokens = tokenize_expression(expression)
        result = parse_tokens(tokens)
        return result


    # Evaluation
    answer = evaluate_math_expression(input)
    return round(answer, 3) #round the answer to the nearest thousandths

def the_game():
    # The quiz
    score = 0
    print("If the answer has decimal value, round to the nearest thousandths\nEx: 0.1236 = 0.124\n")
    questions = int(input("Enter the number of questions you want: "))
    difficulty = int(input("Choose difficulty from 1-3:\n1.) Easy (add and sub)\n2.) Medium (add, sub, and mul)\n3.) Hard (add, sub, mul, and div)\n"))
    for i in range(questions):
        
        # randomizing Expression
            #EASY
        if difficulty == 1:
            num1 = random.randint(1,1001)
            num2 = random.randint(1,1001)
            operator = random.choice(["+", "-"])
            #MEDIUM
        elif difficulty == 2:
            num1 = random.randint(1,1001)
            num2 = random.randint(1,1001)
            operator = random.choice(["+", "-", "*"])
            #HARD
        elif difficulty == 3:
            num1 = random.randint(1,1001)
            num2 = random.randint(1,1001)
            operator = random.choice(["+", "-", "*", "/"])
        
        #Constructing the expression
        expression = f"What is {num1} {operator} {num2}? " #this will be used for the user input
        expression_01 = "{} {} {}".format(str(num1), operator, str(num2)) #this one is for evaluating
        
        #Evaluating
        answer = evaluate(expression_01)
        
        while True: #this loop makes it so that if the user input is invalid, the program will keep asking the same question until a valid input is given
            inp = input(expression)
            
            try:
                inp = float(inp)
                break #break if the input is valid
            except ValueError:
                print("Input should be a number.\n")
                
        #checking
        if inp == answer:
            score+=1
            print("You got the correct answer: {}\n".format(answer))
        else:
            print("WRONG! The correct answer is: {}\n".format(answer))
            
    print(f"Your score is {score}/{questions}")
    

if __name__ == "__main__":
    # This block will be executed only if the module is run as the main program
    the_game()