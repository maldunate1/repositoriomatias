###### Pregunta CASEN ***
import pandas as pd
import os
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf


def q1(df):

	poorGroup = df.groupby('pobreza')
	byPoorness = poorGroup[['folio']].count()
	byPoorness_exp = poorGroup[['expr']].sum()
	byPoorness_exp.plot.pie(y='expr', legend=True, figsize=(8,8), startangle=45)
	byPoorness.plot.pie(y='expr', legend=True, figsize=(8,8), startangle=45)
	plt.show()
	return

def q2(df):

	#total = df.groupby('region')
	totalSum = (df.groupby('region'))[['expr']].sum()
	#print(totalSum)

	df['pobres'] = (df.pobreza != 'No pobres')
	df['pobres_aumentada'] = df.expr * df['pobres']
	#print(df.groupby(['region']).sum()['pobres_aumentada'])
	#by region
	poorsByRegion = df.groupby(['region'])
	dataByRegion = poorsByRegion[['expr', 'pobres_aumentada']].sum()
	
	#calc percentage
	dataByRegion['Porcentaje pobres region'] = (dataByRegion.pobres_aumentada / dataByRegion.expr) #totalSum.expr)

	#graficamos
	dataByRegion['Porcentaje pobres region'].plot.bar()

	#grafico que nos piden
	graph = dataByRegion['Porcentaje pobres region'].plot.bar()

	dataByRegion['pais 8.6'] = 0.09

	dataByRegion.plot(y='pais 8.6', ax=graph)

	plt.show()
	return


def q3(df):

	df2 = df.drop_duplicates(subset='folio')
	
	df2['asis_aum'] = df2.expr*df2['hh_d_asis']
	avgAsisAum = (df2['asis_aum'].sum()/df2.expr.sum())*100
	round(avgAsisAum,1)

	df2['rez_aum'] = df2.expr*df2['hh_d_rez']
	avgRezAum = (df2['rez_aum'].sum()/df2.expr.sum())*100
	round(avgRezAum,1)
	
	df2['esc_aum'] = df2.expr*df2['hh_d_esc']
	avgEscAum = (df2['esc_aum'].sum()/df2.expr.sum())*100
	round(avgEscAum,1)
	
	df2['mal_aum'] = df2.expr*df2['hh_d_mal']
	avgMalAum = (df2['mal_aum'].sum()/df2.expr.sum())*100
	round(avgMalAum,1)
	
	df2['prevs_aum'] = df2.expr*df2['hh_d_prevs']
	avgPrevsAum = (df2['prevs_aum'].sum()/df2.expr.sum())*100
	round(avgPrevsAum,1)
	
	df2['acc_aum'] = df2.expr*df2['hh_d_acc']
	avgAccAum = (df2['acc_aum'].sum()/df2.expr.sum())*100
	round(avgAccAum,1)
	
	df2['accesi_aum'] = df2.expr*df2['hh_d_accesi']
	avgAccesiAum = (df2['accesi_aum'].sum()/df2.expr.sum())*100
	round(avgAccesiAum,1)
	
	df2['medio_aum'] = df2.expr*df2['hh_d_medio']
	avgMedioAum = (df2['medio_aum'].sum()/df2.expr.sum())*100
	round(avgMedioAum,1)
	
	df2['appart_aum'] = df2.expr*df2['hh_d_appart']
	avgAppartAum = (df2['appart_aum'].sum()/df2.expr.sum())*100
	round(avgAppartAum,1)
	
	df2['tsocial_aum'] = df2.expr*df2['hh_d_tsocial']
	avgTsocialAum = (df2['tsocial_aum'].sum()/df2.expr.sum())*100
	round(avgTsocialAum,1)
	
	df2['seg_aum'] = df2.expr*df2['hh_d_seg']
	avgSegAum = (df2['seg_aum'].sum()/df2.expr.sum())*100
	round(avgSegAum,1)

	df2['act_aum'] = df2.expr*df2['hh_d_act']
	avgActAum = (df2['act_aum'].sum()/df2.expr.sum())*100
	round(avgActAum,1)
	
	df2['cot_aum'] = df2.expr*df2['hh_d_cot']
	avgCotAum = (df2['cot_aum'].sum()/df2.expr.sum())*100
	round(avgCotAum,1)
	
	df2['jub_aum'] = df2.expr*df2['hh_d_jub']
	avgJubAum = (df2['jub_aum'].sum()/df2.expr.sum())*100
	round(avgJubAum,1)
	
	df2['habitab_aum'] = df2.expr*df2['hh_d_habitab']
	avgHabitabAum = (df2['habitab_aum'].sum()/df2.expr.sum())*100
	round(avgHabitabAum,1)
	
	df2['hacina_aum'] = df2.expr*df2['hh_d_hacina']
	avgHacinaAum = (df2['hacina_aum'].sum()/df2.expr.sum())*100
	round(avgHacinaAum,1)
	
	df2['estado_aum'] = df2.expr*df2['hh_d_estado']
	avgEstadoAum = (df2['estado_aum'].sum()/df2.expr.sum())*100
	round(avgEstadoAum,1)
	
	df2['servbas_aum'] = df2.expr*df2['hh_d_servbas']
	avgServbasAum = (df2['servbas_aum'].sum()/df2.expr.sum())*100
	round(avgServbasAum,1)
	
	df2['entorno_aum'] = df2.expr*df2['hh_d_entorno']
	avgEntornoAum = (df2['entorno_aum'].sum()/df2.expr.sum())*100
	round(avgEntornoAum,1)

	df3 = pd.DataFrame({'Dimensión':['Educación']*3+['Salud']*3+['Trabajo y seguridad Social']*3+['Vivienda y entorno']*3+['Redes y Cohesión Social']*3,'Indicador':['Asistencia','Rezago','Escolaridad','Malnutrición','Adscripción al Sistema de Salud','Atención en Salud','Ocupación','Seguridad Social','Jubilación','Habitabilidad','Servicios Básicos','Entorno','Apoyo y participación social','Trato igualitario','Seguridad'], '2017':[round(avgAsisAum,1),round(avgRezAum,1),round(avgEscAum,1),round(avgMalAum,1),round(avgPrevsAum,1),round(avgAccAum,1),round(avgActAum,1),round(avgCotAum,1),round(avgJubAum,1),round(avgHabitabAum,1),round(avgServbasAum,1),round(avgEntornoAum,1),round(avgAppartAum,1),round(avgTsocialAum,1),round(avgSegAum,1)]})
	print(df3)
	return

def q4(df):
	df['pobres'] = (df.pobreza != 'No pobres')
	df['pobres_aumentada'] = df.expr * df['pobres']
	
	#byComuna
	dataByComuna = (df.groupby(['comuna']))[['expc', 'pobres_aumentado']].sum()
	
	#calculamos porcentaje
	dataByComuna['Porcentaje Pobres Comuna'] = (dataByComuna.pobres_aumentado / dataByComuna.expc)
	dataByComuna.sort_values(by=['Porcentaje Pobres Comuna'], ascending=False, inplace=True)
	#print(dataByComuna)
	
	## aquí vemos las 5 primeras
	fivePoorest = dataByComuna.nlargest(5, 'Porcentaje Pobres Comuna')
	fiveRichest = dataByComuna.nsmallest(5, 'Porcentaje Pobres Comuna')
	print('Cinco comunas con menor incidencia de pobreza') # Camina, Porvenir, Pichilemu, Nunoa, Providencia
	print(fiveRichest.loc)
	print('Cinco comunas con mayor incidencia de pobreza') # Cholchol, Tolten, Cobquecura, Galvarino, San Juan de la Costa
	print(fivePoorest['comuna'])
	
	return


def q5(df):
	#lm = smf.ols(formula='variable respuesta~ var1+var2+var3', data = nombre_base_datos).fit()
	#lm = smf.ols(formula='pobreza~ comuna + y2_hrs', data = df).fit() #y1 salario - o10 horas de trabajo semanal - comuna
	#print(smf.ols)

	# Para crear la variable pobreza, esta puede estar fabricada a partir de la cantidad de horas de trabajo semanal y el ingreso total. Teoricamente, a medida que mas se trabaja, deberian ser menos pobres y si gana mas dinero tambien.
	#Para desarrollar el alogritmo de pobreza, hacemos una regresion lineal multiple siendo la variable dependiente la pobreza y las variables independientes todas las que tengan relacion con la pobreza (ingreso, comuna, dias y horas trabajadas por periodo de tiempo, etc), dada la correlacion de las variables explicativas con respecto a la variable dependiente que es la variable que queremos crear (pobreza) vamos a poder hacer el algoritmo de esta variable.

	#A mayor correlacion con la variable dependiente mayor va a ser la significancia de esta variable con respecto a la variable que queremos crear, por lo que vamos a poder hacer el algoritmo de esta nueva variable en base a las que ya tenemos en la encuesta casen.
	

	dataByComuna = (df.groupby(['comuna']))['pobreza']
	dataHorasDeTrabajo = (df.groupby(['y2_hrs']))['pobreza']
	
	#lm = smf.ols('pobreza ~ ytot + y2_hrs', data = df).fit()
	#print(lm.summary())
	#print(dataByComuna)
	#print(dataHorasDeTrabajo)

	return

def q6(df):
	##Answer
	#Utilizaremos ch1: mes pasado salario líquido trabajo principal y región
	
	df['asalariados'] = ('ch1' == 1)
	df['asalariados_aumentado'] = df.expr * df['asalariados']

	groupByRegion = df.groupby(['region'])
	dataByRegion = groupByRegion[['expr', 'asalariados_aumentado']].sum()
	dataByRegion['Porcentaje Asalariados'] = (dataByRegion.asalariados_aumentado / dataByRegion.expr)*100
	dataByRegion['Porcentaje Asalariados'].plot.bar()
	plt.show()	

	return

def q7(df):

# #Luego de un analisis previo, se llego a la conclusion de que las regiones con mayor porcentaje de población asalariada se encuentraen las regiones de Magallanes, Metropolitana y O'Higgins. Ademas, las regiones con menor porcentaje de población asalariada son: Arica y Parinacota, La Araucanía y Coquimbo. Estos resultados tienen sentido con el gráfico de pobreza por ingresos hecho anteriormente, en donde en el caso de la región de Magallanes es la con menor pobreza y la Region de La Araucanía es la region con mayor indice de pobreza porcentual. Esto nos demuestra en cierto grado que el empleo con contrato es un indicador de desarrollo al estar la pobreza por ingresos de cierta forma correlacionada con el porcentaje de población asalariada por región. Los resultados en este caso no estan en el mismo orden, pero hay algunos casos como por ejemplo los casos extremos que nos permiten poder analizar y verificar una correlacion entre las variables estudiadas en la encuesta y en la tarea.
# '''

	return

if __name__ == '__main__':
	filename = 'Casen 2017small.dta'
	dirname = os.path.dirname(__file__)
	directory =  os.path.join(dirname, filename)
	df = pd.read_stata(directory)
	
	#q1(df)  ##lista
	#q2(df)  ##lista
	#q3(df)
	#q4(df)
	#q5(df)
	q6(df)
	#q7(df)

	## LA BASE DE DATOS CASEN DEBE ESTAR EN LA MISMA CARPETA QUE ESTE SCRIPT
	## FIN DEL PROGRAMA