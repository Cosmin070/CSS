from datetime import datetime


def write(result):
    # datetime object containing current date and time
    now = datetime.now()

    # dd/mm/YYH:M:S
    dt_string = now.strftime("%d%m%Y-%H%M")
    f = open("result " + dt_string + ".xml", "w")
    f.write("<result>\n\t" + result + "\n</result>")


write("rezultat")
