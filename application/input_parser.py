import re


def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start + len(needle))
        n -= 1
    return start


def get_symbols_position(string):
    tag_start_position = []
    tag_end_position = []
    i = 1
    while find_nth(string, "<", i) != -1:
        tag_start_position.append(find_nth(string, "<", i))
        i += 1
    i = 1
    while find_nth(string, ">", i) != -1:
        tag_end_position.append(find_nth(string, ">", i))
        i += 1
    return tag_start_position, tag_end_position


def validate_tags(content):
    tag_start_position, tag_end_position = get_symbols_position(content)
    # checks if the number of ">" equals the number of "<"
    if len(tag_start_position) == len(tag_end_position):
        # the occurences of either ">" or "<" should always be even
        if len(tag_start_position) % 2 == 1 or len(tag_end_position) % 2 == 1:
            print("tag unclosed or closed without being opened first")
        # checks if the symbol "<" comes always before ">"
        for i in range(0, len(tag_start_position)):
            if tag_start_position[i] > tag_end_position[i]:
                print("tag enclosing positioned in wrong order")
        print("enclosing order correct")
        # checks if a tag is first opened and then closed
        open_tags_valid = True
        closed_tags_valid = True
        for i in range(1, len(tag_start_position) - 2, 1):
            if i % 2 == 1:
                if content[tag_start_position[i] + 1] == "/":
                    open_tags_valid = False
            if i % 2 == 0:
                if content[tag_start_position[i] + 1] != "/":
                    closed_tags_valid = False
        if open_tags_valid and closed_tags_valid:
            print("tags valid")
        else:
            print("invalid tags")
    else:
        print("open tag length different than close tag length")


def check_for_tag_order(content, equation_tag, expression_tag):
    equation_open_tag_found = False
    expression_open_tag_found = False
    equation_close_tag_found = False
    expression_close_tag_found = False
    for each_line in content:
        if each_line.find(equation_tag[0]) != -1:
            if not equation_close_tag_found:
                equation_open_tag_found = True
            else:
                print("0wrong tag enclosing order" + each_line)
        if each_line.find(expression_tag[0]) != -1:
            if not equation_open_tag_found:
                print("1wrong tag enclosing order" + each_line)
            else:
                if not expression_close_tag_found:
                    expression_open_tag_found = True
        if each_line.find(expression_tag[1]) != -1:
            expression_close_tag_found = True
        if each_line.find(equation_tag[1]) != -1:
            if not expression_close_tag_found:
                print("2wrong tag enclosing order" + each_line)
            else:
                equation_close_tag_found = True
    if equation_open_tag_found and equation_close_tag_found and expression_open_tag_found and expression_close_tag_found:
        print("tag order correct")


def get_variables_and_values(string):
    tag_start_position, tag_end_position = get_symbols_position(string)
    variables = {}
    for i in range(1, len(tag_start_position) - 2, 2):
        variables[string[tag_start_position[i] + 1:tag_end_position[i]]] = string[
                                                                           tag_end_position[i] + 1:tag_start_position[
                                                                               i + 1]]
    return variables


def get_expression(variables):
    expression = variables["expression"]
    variable_keys = list(variables.keys())
    variable_values = list(variables.values())
    for i in range(0, len(variable_keys)):
        expression = expression.replace(variable_keys[i], variable_values[i])
    print("final expression: ", expression)
    return expression


def parse(path):
    equation_tag = ["<equation>", "</equation>"]
    expression_tag = ["<expression>", "</expression>"]
    if not path.endswith(".xml"):
        return
    file = open(path, "r", encoding='utf-8')
    content = file.readlines()
    print(content)
    check_for_tag_order(content, equation_tag, expression_tag)
    file = open(path, "r", encoding='utf-8')
    content_string = re.sub(r"[^a-zA-Z0-9<>()+-/*√^]", "", file.read())
    print(content_string)
    validate_tags(content_string)
    print("stripped input:", content_string)
    substituted_expression = get_expression(get_variables_and_values(content_string))
    return substituted_expression
