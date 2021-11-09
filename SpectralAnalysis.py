SOL_NUM = input("Enter solution #: ")

def getAbsorptions():
    with open("Data/absorptions" + SOL_NUM + ".txt", 'r') as f:
        return [float(A.strip()) for A in f]

def beerLambertConcentration(A): 
    # wavelength of spectrophotometer light while measuring samples
    WAVELENGTH = 600 # nm
    # extinction coefficient for e. coli at 600nm
    e = 62720211.1528 # m2mol-1
    # optical path length (width of cuvette)
    l = 1 # cm
    # concentration of e. coli in solution (A = elc)
    c = A / (e * l)
    return c # M

def turbidityConversion(A):
    # wavelength of spectrophotometer light while measuring samples
    WAVELENGTH = 600 # nm
    # optical path length (width of cuvette)
    l = 1 # cm
    # turbidity of solution (SCALED)
    T = ((2.3 * A) / l) * 10
    return T # NTU

def output(data, ch):
    file = ""
    units = " "
    if ch == 'c':
        file = "Data/concentrations" + SOL_NUM + ".txt"
        units += "M"
    if ch == 't':
        file = "Data/turbidities" + SOL_NUM + ".txt"
        units += "NTU"
    with open(file, 'w') as f:
        f.write('\n'.join((str(data.index(pt)) + ".\t" + str(pt) + units) for pt in data))

def main():
    absorptions = getAbsorptions()
    concentrations = list(map(beerLambertConcentration, absorptions))
    turbidities = list(map(turbidityConversion, absorptions))
    output(concentrations, 'c')
    output(turbidities, 't')

if __name__ == "__main__":
    main()