from datetime import datetime


def write(result):
    now = datetime.now()
    print(result)
    dt_string = now.strftime("%d%m%Y-%H%M")
    f = open("results/result " + dt_string + ".xml", "w")
    f.write("<result>\n\t" + result + "\n</result>")
