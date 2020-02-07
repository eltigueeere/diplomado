from cargar import cargarPoker

var01=cargarPoker.variables
cadena=""
punto = False


for i in range(len(var01)):
    lalo=str(var01[i][0])
    for j in range(len(lalo)):
        if(punto == True):
            cadena += lalo[j]
        if(lalo[j] == '.'):
            punto = True
    var01[i].append(cadena)
    punto=False
    cadena=""
  