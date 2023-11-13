import random


def generate_random_integer(min_value, max_value):
    """
    Generate a random integer within the specified range.

    Parameters:
    - min_value (int): The minimum value of the range (inclusive).
    - max_value (int): The maximum value of the range (inclusive).

    Returns:
    int: A random integer within the specified range.
    """
    return random.randint(int(min_value), int(max_value))


def generate_random_operator():
    """
    Generate a random mathematical operator (+, -, *).

    Returns:
    str: A randomly selected operator.
    """
    return random.choice(['+', '-', '*'])

def create_problem(num1, num2, operator):
    """
    Perform a mathematical operation on two numbers.

    Parameters:
    - num1 (int): The first number.
    - num2 (int): The second number.
    - operator (str): The mathematical operator.

    Returns:
    tuple: A tuple containing the problem string and the calculated answer.
    """
    #String with question
    problem = f"{num1} {operator} {num2}"

    #Corresponding to the operator create the answer for the question
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return problem, answer

def math_quiz():
    """
    Conduct a math quiz game where the user answers random math problems.
    """

    #Initialise score and total_score variables with 0 and total number of questions
    #Give integer values to score and total_score
    score = 0
    total_score = 4

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    #Loop to create as number of question as in total_score
    for _ in range(total_score):

        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5.5)
        operator = generate_random_operator()

        #Calling create_problem function to create problems
        problem, answer = create_problem(num1, num2, operator)

        print(f"\nQuestion: {problem}")

        #Prompt user for answer to the problem
        user_answer = input("Your answer: ")

        #Try block to catch ValueError and display that user has entered in Invalid answer
        try:
            user_answer = int(user_answer)
        except ValueError:
            #Display that error message to user
            print("Lost your chance to answer, Please enter an integer as answer\n")

        #Check if the user_answer is equal to answer
        if user_answer == answer:
            #Correct Answer,increment the score by 1
            print("Correct! You earned an answer point.")
            score += 1
        else:
            #Display wrong answer message to user
            print(f"Wrong answer. The correct answer is {answer}.")

    #Display the final score to the user
    print(f"\nGame over! Your score is: {score}/{total_score}")
#Main function
if __name__ == "__main__":
    math_quiz()