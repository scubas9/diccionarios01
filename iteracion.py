#10 progrogramas utilizando la funcion de iteracion
medicina={"cardiologia":"corazon","infectologo":"infecciones","gasterentologo":"estomago","neurologo":"cerebro"}

departamentos={"cantidad":24,"san martin":"moyobamba","cuscu":"cuscu","junin":"jauja","madre de dios":"puerto maldonado"}

eropeos={"francia":"paris","portugal":"lisboa","españa":"madrid","italia":"roma","bulgaria":"sofia"}

monedas={"brasil":"real","ecuador":"dolar USA","argentina":"peso argentino","bolivia":"boliviano","paraguay":"guarani"}

americanos={"canada":"catawa","puerto rico":"san juan","cuba":"la habana","rep dominicana":"santo domingo"}
monedas_eropeas={"españa":"euro","francia":"euro","italia":"euro","portugal":"euro","reino unido":"libra esterlina"}
periodo_gestante={"cuy":2,"armadillo":3,"caballo":12,"firafa":15,"morsa":16,"narval":15,"rinoceronte":15,"ballena":15,"elefante":22}
paises={"nueva zelanda":"wellington","australia":"canberra","ejipto":"el  cairo","gresia":"atenas"}
organismos_internacionales={"unicef":"niño","oms":"salud","oit":"trabajo","unesco":"cultura"}
maravillas={"machu picchu":"peru","cristo redentor":"brasil","taj malhal":"india","coliseo romano":"italia","chichen itza":"mexico"}
#ejer1
for key in medicina:
    print(key,medicina[key])
#jer2
for key in departamentos :
    print(key,departamentos[key])

#eje3
for key in eropeos:
    print(key,eropeos[key])

#ejer4
for key in monedas:
    print(key,monedas[key])

#ejer5
for key in americanos:
    print(key,americanos[key])

#ejer6
for key in monedas_eropeas:
    print(key,monedas_eropeas[key])

#eje7
for key in periodo_gestante:
    print(key,periodo_gestante[key])

#eje8
for key in paises:
    print(key,paises[key])

#ejer9
for key in organismos_internacionales:
    print(key,organismos_internacionales[key])

#ejer10
for key in maravillas:
    print(key,maravillas[key])

