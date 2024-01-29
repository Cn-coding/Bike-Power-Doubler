# This script is used to double the power values in a .gpx file.

# Write file name here, include the .gpx extension
FILENAME = ""

# Creates new file name
NEW_FILENAME = FILENAME[:-4] + "_doubled.gpx"


# Doubles a single power value
def double_power(line):
    if "<power>" in line and "</power>" in line:
        start_index = line.index("<power>") + 7
        end_index = line.index("</power>")
        power = line[start_index:end_index]
        if power != "":
            power = str(int(power) * 2)
            line = line[:start_index] + power + line[end_index:]
    return line


# Reads and doubles power values
with open(FILENAME, "r") as f:
    lines = [double_power(x) for x in f.readlines()]
    f.close()

# Writes new file with doubled power values
with open(NEW_FILENAME, "w") as f:
    f.writelines(lines)
    f.close()
