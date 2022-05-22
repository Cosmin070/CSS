import re

from application.exceptions import TagException, NonXMLFileTypeException

CLOSE_BRACKET, OPEN_BRACKET = ">", '<'


def find_nth(haystack, needle, n):
    assert len(haystack) > 0
    assert len(needle) > 0
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        assert start < len(haystack)
        start = haystack.find(needle, start + len(needle))
        n -= 1
    assert n >= 1
    return start


def get_symbols_position(string):
    assert len(string) > 0
    tag_start_position = []
    tag_end_position = []
    i = 1
    while find_nth(string, OPEN_BRACKET, i) != -1:
        tag_start_position.append(find_nth(string, OPEN_BRACKET, i))
        i += 1
    i = 1
    while find_nth(string, CLOSE_BRACKET, i) != -1:
        tag_end_position.append(find_nth(string, CLOSE_BRACKET, i))
        i += 1
    assert len(tag_start_position) > 0
    assert len(tag_end_position) > 0
    return tag_start_position, tag_end_position


def validate_tags(content):
    assert len(content) > 0
    tag_start_position, tag_end_position = get_symbols_position(content)
    # checks if the number of ">" equals the number of "<"
    if len(tag_start_position) == len(tag_end_position):
        # the occurrences of either ">" or "<" should always be even
        if len(tag_start_position) % 2 == 1 or len(tag_end_position) % 2 == 1:
            raise TagException("Tag unclosed or closed without being opened first")
        # checks if the symbol "<" comes always before ">"
        for i in range(0, len(tag_start_position)):
            assert len(tag_start_position) - i > 0
            if tag_start_position[i] > tag_end_position[i]:
                raise TagException("Tag enclosing positioned in wrong order")
        # checks if a tag is first opened and then closed
        open_tags_valid = True
        closed_tags_valid = True
        for i in range(1, len(tag_start_position) - 2, 1):
            if i % 2 == 1 and content[tag_start_position[i] + 1] == "/":
                open_tags_valid = False
            if i % 2 == 0 and content[tag_start_position[i] + 1] != "/":
                closed_tags_valid = False
        if not (open_tags_valid and closed_tags_valid):
            raise TagException("Invalid tags")
    else:
        raise TagException("Open tag length different than close tag length")


def check_for_tag_order(content, equation_tag, expression_tag):
    assert len(content) > 0
    assert len(equation_tag) > 0
    assert len(expression_tag) > 0
    equation_open_tag_found = False
    equation_close_tag_found = False
    expression_close_tag_found = False
    for each_line in content:
        wrong_tag_order = "Wrong tag enclosing order"
        if each_line.find(equation_tag[0]) != -1:
            if not equation_close_tag_found:
                equation_open_tag_found = True
            else:
                raise TagException(wrong_tag_order + " " + each_line)
        if each_line.find(expression_tag[0]) != -1:
            if not equation_open_tag_found:
                raise TagException(wrong_tag_order + each_line)
        if each_line.find(expression_tag[1]) != -1:
            expression_close_tag_found = True
        if each_line.find(equation_tag[1]) != -1:
            if not expression_close_tag_found:
                raise TagException(wrong_tag_order + each_line)
            else:
                equation_close_tag_found = True


def get_variables_and_values(string):
    assert len(string) > 0
    tag_start_position, tag_end_position = get_symbols_position(string)
    variables = {}
    for i in range(1, len(tag_start_position) - 2, 2):
        variables[string[tag_start_position[i] + 1:tag_end_position[i]]] = string[
                                                                           tag_end_position[i] + 1:tag_start_position[
                                                                               i + 1]]
    return variables


def get_expression(variables):
    assert variables != {}
    expression = variables["expression"]
    variable_keys = list(variables.keys())
    variable_values = list(variables.values())
    for i in range(0, len(variable_keys)):
        expression = expression.replace(variable_keys[i], variable_values[i])
    return expression


def parse(path):
    assert path != ''
    equation_tag = ["<equation>", "</equation>"]
    expression_tag = ["<expression>", "</expression>"]
    if not path.endswith(".xml"):
        raise NonXMLFileTypeException("File is not XML.")
    file = open(path, "r", encoding='utf-8')
    content = file.readlines()
    check_for_tag_order(content, equation_tag, expression_tag)
    file.close()
    file = open(path, "r", encoding='utf-8')
    content_string = re.sub(r"[^a-zA-Z0-9<>()+-/*√^]", "", file.read())
    validate_tags(content_string)
    substituted_expression = get_expression(get_variables_and_values(content_string))
    file.close()
    return substituted_expression
