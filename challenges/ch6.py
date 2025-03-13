def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_line = ""
    second_line = ""
    dashes = ""
    answers = ""
    
    for problem in problems:
        parts = problem.split()
        
        if parts[1] not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        
        if not parts[0].isdigit() or not parts[2].isdigit():
            return "Error: Numbers must only contain digits."
        
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        first_number = parts[0]
        operator = parts[1]
        second_number = parts[2]
        
        if operator == "+":
            answer = str(int(first_number) + int(second_number))
        else:
            answer = str(int(first_number) - int(second_number))
        
        width = max(len(first_number), len(second_number)) + 2
        
        if first_line != "":
            first_line += "    "
            second_line += "    "
            dashes += "    "
            answers += "    "
        
        first_line += first_number.rjust(width)
        second_line += operator + second_number.rjust(width - 1)
        dashes += "-" * width
        answers += answer.rjust(width)
    
    if show_answers:
        arranged_problems = first_line + "\n" + second_line + "\n" + dashes + "\n" + answers
    else:
        arranged_problems = first_line + "\n" + second_line + "\n" + dashes
    
    return arranged_problems

    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')