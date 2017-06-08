def filterCityFile():
    data = [line.strip() for line in open("worldcitiespop.txt", 'r')]
    cities = [line.split(",") for line in data]
    cities = cities[1:]

    filteredcities = []

    for line in cities:
        if line[4] != '':
            filteredcities.append(line)
    print len(filteredcities)
    f = open("filteredcities.txt", 'w')
    for line in filteredcities:
        line = ','.join(line)
        line = line + '\n'
        f.write(line)

    f.close()

filterCityFile()
