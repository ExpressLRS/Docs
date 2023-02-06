# quick garbage script to take old nav lists (I just manually sanitized them because I was lazy)
# could have just used mkdocs.ymls reading all lines in the nav: section

import re

nav3 = open('tools/nav3', "r")
lines3 = re.findall("(?<=\: ).*", nav3.read())
nav3.close()

nav2 = open('tools/nav2', "r")
lines2 = re.findall("(?<=\: ).*", nav2.read())
nav2.close()

nav1 = open('tools/nav1', "r")
lines1 = re.findall("(?<=\: ).*", nav1.read())
nav1.close()

out = open('redirects.yml', "w")
out.write("plugins:\n" + "  redirects:\n" + "   redirect_maps:\n")
for line in lines3:
    line = line.replace("'","")
    out.write("     '3.0/" + line + "' : '" + line + "'\n")
for line in lines2:
    line = line.replace("'","")
    out.write("     '2.0/" + line + "' : '" + line + "'\n")
for line in lines1:
    line = line.replace("'","")
    out.write("     '1.0/" + line + "' : '" + line + "'\n")
out.close()
