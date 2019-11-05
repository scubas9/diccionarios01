#10 programas con la operacion busqueda
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
print(medicina.get("cardiologia"))
#ejer2
print(departamentos.get("junin"))

#ejer3
print(eropeos.get("portugal"))

#ejer4
print(monedas.get("argentina"))

#ejer5
print(monedas_eropeas.get("españa"))

#ejer6
print(organismos_internacionales.get("unicef"))

#ejer7
print(maravillas.get("taj malhal"))

#ejer8
print(periodo_gestante.get("elefante"))

#ejer9
print(paises.get("nueva zelanda"))

#ejer10
print(americanos.get("canada"))


