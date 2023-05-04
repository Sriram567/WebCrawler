import sys
for line in sys.stdin:
    line = line.strip().split()
    if line[1] == '-1':
        # print(line[0], line[0])
        continue
    if line[1] not in {'0', '1'}:
        for url in line[1:]:
            print(line[0], url)