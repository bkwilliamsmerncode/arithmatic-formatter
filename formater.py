def arithmetic_arranger(problems, display_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_operands = []
    operators = []
    second_operands = []
    results = []

    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return 'Error: Invalid problem format.'

        first_operand, operator, second_operand = parts

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        if not first_operand.isdigit() or not second_operand.isdigit():
            return 'Error: Numbers must only contain digits.'
        
        if len(first_operand) > 4 or len(second_operand) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        first_operands.append(first_operand)
        operators.append(operator)
        second_operands.append(second_operand)

        if operator == '+':
            results.append(str(int(first_operand) + int(second_operand)))
        elif operator == '-':
            results.append(str(int(first_operand) - int(second_operand)))

    # Calculate widths
    widths = [max(len(first), len(second)) + 2 for first, second in zip(first_operands, second_operands)]

    # Prepare formatted lines
    first_line = '    '.join([first.rjust(width) for first, width in zip(first_operands, widths)])
    second_line = '    '.join([op + ' ' + second.rjust(width - 2) for op, second, width in zip(operators, second_operands, widths)])
    dash_line = '    '.join(['-' * width for width in widths])
    result_line = '    '.join([result.rjust(width) for result, width in zip(results, widths)])

    if display_answers:
        arranged_problems = '\n'.join([first_line, second_line, dash_line, result_line])
    else:
        arranged_problems = '\n'.join([first_line, second_line, dash_line])

    return arranged_problems

# Example usage:
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], display_answers=True))