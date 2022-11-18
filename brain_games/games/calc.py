from random import choice, randint
import operator


RULES = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 100
OPERATIONS = {
    '-': operator.sub,
    '+': operator.add,
    '*': operator.mul
}


def get_question_and_correct_answer():
    a = randint(MIN_NUMBER, MAX_NUMBER)
    b = randint(MIN_NUMBER, MAX_NUMBER)
    operation = choice(list(OPERATIONS.keys()))
    return f'{a} {operation} {b}', str(OPERATIONS[operation](a, b))
