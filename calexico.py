import numpy as np
import pandas as pd
import datetime as dt
import pickle
import matplotlib.pyplot as plt


fronteras=pd.read_csv('frontera.csv')

s_Cal = fronteras["Port Name"] == "Calexico"
es_PD = fronteras["Measure"] == "Pedestrians"

fronteras["Date"] = pd.to_datetime(fronteras["Date"], format="%m/%d/%Y")
es_2019 = fronteras["Date"].dt.strftime("%Y") == "2019"
es_2018 = fronteras["Date"].dt.strftime("%Y") == "2018"
es_2017 = fronteras["Date"].dt.strftime("%Y") == "2017"
es_2016 = fronteras["Date"].dt.strftime("%Y") == "2016"
es_2015 = fronteras["Date"].dt.strftime("%Y") == "2015"
es_2014 = fronteras["Date"].dt.strftime("%Y") == "2014"
es_2013 = fronteras["Date"].dt.strftime("%Y") == "2013"
es_2012 = fronteras["Date"].dt.strftime("%Y") == "2012"
es_2011 = fronteras["Date"].dt.strftime("%Y") == "2011"
es_2010 = fronteras["Date"].dt.strftime("%Y") == "2010"
es_2009 = fronteras["Date"].dt.strftime("%Y") == "2009"
es_2008 = fronteras["Date"].dt.strftime("%Y") == "2008"
es_2007 = fronteras["Date"].dt.strftime("%Y") == "2007"
es_2006 = fronteras["Date"].dt.strftime("%Y") == "2006"
es_2005 = fronteras["Date"].dt.strftime("%Y") == "2005"
es_2004 = fronteras["Date"].dt.strftime("%Y") == "2004"
es_2003 = fronteras["Date"].dt.strftime("%Y") == "2003"
es_2002 = fronteras["Date"].dt.strftime("%Y") == "2002"
es_2001 = fronteras["Date"].dt.strftime("%Y") == "2001"
es_2000 = fronteras["Date"].dt.strftime("%Y") == "2000"

es_enero = fronteras["Date"].dt.strftime("%m") == "01"
es_febrero = fronteras["Date"].dt.strftime("%m") == "02"
es_marzo = fronteras["Date"].dt.strftime("%m") == "03"
es_abril = fronteras["Date"].dt.strftime("%m") == "04"
es_mayo = fronteras["Date"].dt.strftime("%m") == "05"
es_junio = fronteras["Date"].dt.strftime("%m") == "06"
es_julio = fronteras["Date"].dt.strftime("%m") == "07"
es_agosto = fronteras["Date"].dt.strftime("%m") == "08"
es_septiembre = fronteras["Date"].dt.strftime("%m") == "09"
es_octubre = fronteras["Date"].dt.strftime("%m") == "10"
es_noviembre = fronteras["Date"].dt.strftime("%m") == "11"
es_diciembre = fronteras["Date"].dt.strftime("%m") == "12"

frontCalenede5en5 = fronteras[s_Cal & (es_2019 | es_2018 | es_2015 | es_2010 | es_2005 | es_2000) & es_PD & es_enero]
frontCalfebde5en5 = fronteras[s_Cal & (es_2019 | es_2018 | es_2015 | es_2010 | es_2005 | es_2000) & es_PD & es_febrero]
frontCalmarde5en5 = fronteras[s_Cal & (es_2019 | es_2018 | es_2015 | es_2010 | es_2005 | es_2000) & es_PD & es_marzo]
frontCalabrde5en5 = fronteras[s_Cal & (es_2019 | es_2018 | es_2015 | es_2010 | es_2005 | es_2000) & es_PD & es_abril]
frontCalmayde5en5 = fronteras[s_Cal & (es_2019 | es_2018 | es_2015 | es_2010 | es_2005 | es_2000) & es_PD & es_mayo]
frontCaljunde5en5 = fronteras[s_Cal & (es_2019 | es_2018 | es_2015 | es_2010 | es_2005 | es_2000) & es_PD & es_junio]
frontCaljulde5en5 = fronteras[s_Cal & (es_2019 | es_2018 | es_2015 | es_2010 | es_2005 | es_2000) & es_PD & es_julio]
frontCalagode5en5 = fronteras[s_Cal & (es_2019 | es_2018 | es_2015 | es_2010 | es_2005 | es_2000) & es_PD & es_agosto]
frontCalsepde5en5 = fronteras[s_Cal & (es_2019 | es_2018 | es_2015 | es_2010 | es_2005 | es_2000) & es_PD & es_septiembre]
frontCaloctde5en5 = fronteras[s_Cal & (es_2019 | es_2018 | es_2015 | es_2010 | es_2005 | es_2000) & es_PD & es_octubre]
frontCalnovde5en5 = fronteras[s_Cal & (es_2019 | es_2018 | es_2015 | es_2010 | es_2005 | es_2000) & es_PD & es_noviembre]
frontCaldicde5en5 = fronteras[s_Cal & (es_2019 | es_2018 | es_2015 | es_2010 | es_2005 | es_2000) & es_PD & es_diciembre]

anioenede5en5=frontCalenede5en5.describe()
aniofebde5en5=frontCalfebde5en5.describe()
aniomarde5en5=frontCalmarde5en5.describe()
anioabrde5en5=frontCalabrde5en5.describe()
aniomayde5en5=frontCalmayde5en5.describe()
aniojunde5en5=frontCaljunde5en5.describe()
aniojulde5en5=frontCaljulde5en5.describe()
anioagode5en5=frontCalagode5en5.describe()
aniosepde5en5=frontCalsepde5en5.describe()
aniooctde5en5=frontCaloctde5en5.describe()
anionovde5en5=frontCalnovde5en5.describe()
aniodicde5en5=frontCaldicde5en5.describe()

print("\n Describe de cada mes de los años de 5 en 5 para mostrar la media")
print(anioenede5en5)
print(aniofebde5en5)
print(aniomarde5en5)
print(anioabrde5en5)
print(aniomayde5en5)
print(aniojunde5en5)
print(aniojulde5en5)
print(anioagode5en5)
print(aniosepde5en5)
print(aniooctde5en5)
print(anionovde5en5)
print(aniodicde5en5)

frontCalenede10 = fronteras[s_Cal & (es_2019 | es_2018 | es_2017 | es_2016  | es_2015 | es_2014 | es_2013 | es_2012 | es_2011 | es_2010) & es_PD & es_enero]
frontCalfebde10 = fronteras[s_Cal & (es_2019 | es_2018 | es_2017 | es_2016  | es_2015 | es_2014 | es_2013 | es_2012 | es_2011 | es_2010) & es_PD & es_febrero]
frontCalmarde10 = fronteras[s_Cal & (es_2019 | es_2018 | es_2017 | es_2016  | es_2015 | es_2014 | es_2013 | es_2012 | es_2011 | es_2010) & es_PD & es_marzo]
frontCalabrde10 = fronteras[s_Cal & (es_2019 | es_2018 | es_2017 | es_2016  | es_2015 | es_2014 | es_2013 | es_2012 | es_2011 | es_2010) & es_PD & es_abril]
frontCalmayde10 = fronteras[s_Cal & (es_2019 | es_2018 | es_2017 | es_2016  | es_2015 | es_2014 | es_2013 | es_2012 | es_2011 | es_2010) & es_PD & es_mayo]
frontCaljunde10 = fronteras[s_Cal & (es_2019 | es_2018 | es_2017 | es_2016  | es_2015 | es_2014 | es_2013 | es_2012 | es_2011 | es_2010) & es_PD & es_junio]
frontCaljulde10 = fronteras[s_Cal & (es_2019 | es_2018 | es_2017 | es_2016  | es_2015 | es_2014 | es_2013 | es_2012 | es_2011 | es_2010) & es_PD & es_julio]
frontCalagode10 = fronteras[s_Cal & (es_2019 | es_2018 | es_2017 | es_2016  | es_2015 | es_2014 | es_2013 | es_2012 | es_2011 | es_2010) & es_PD & es_agosto]
frontCalsepde10 = fronteras[s_Cal & (es_2019 | es_2018 | es_2017 | es_2016  | es_2015 | es_2014 | es_2013 | es_2012 | es_2011 | es_2010) & es_PD & es_septiembre]
frontCaloctde10 = fronteras[s_Cal & (es_2019 | es_2018 | es_2017 | es_2016  | es_2015 | es_2014 | es_2013 | es_2012 | es_2011 | es_2010) & es_PD & es_octubre]
frontCalnovde10 = fronteras[s_Cal & (es_2019 | es_2018 | es_2017 | es_2016  | es_2015 | es_2014 | es_2013 | es_2012 | es_2011 | es_2010) & es_PD & es_noviembre]
frontCaldicde10 = fronteras[s_Cal & (es_2019 | es_2018 | es_2017 | es_2016  | es_2015 | es_2014 | es_2013 | es_2012 | es_2011 | es_2010) & es_PD & es_diciembre]

anioenede10=frontCalenede10.describe()
aniofebde10=frontCalfebde10.describe()
aniomarde10=frontCalmarde10.describe()
anioabrde10=frontCalabrde10.describe()
aniomayde10=frontCalmayde10.describe()
aniojunde10=frontCaljunde10.describe()
aniojulde10=frontCaljulde10.describe()
anioagode10=frontCalagode10.describe()
aniosepde10=frontCalsepde10.describe()
aniooctde10=frontCaloctde10.describe()
anionovde10=frontCalnovde10.describe()
aniodicde10=frontCaldicde10.describe()

print("\n Describe de cada mes de los años 2012 a 2017 para mostrarlo como se pide y usarlo para sacar los datos de el centro de rango:")
print(anioenede10)
print(aniofebde10)
print(aniomarde10)
print(anioabrde10)
print(aniomayde10)
print(aniojunde10)
print(aniojulde10)
print(anioagode10)
print(aniosepde10)
print(aniooctde10)
print(anionovde10)
print(aniodicde10)

centroderangoene=(319138+415687)/2
centroderangofeb=(291959+405254)/2
centroderangomar=(346158+440551)/2
centroderangoabr=(322339+393583)/2
centroderangomay=(337402+448570)/2
centroderangojun=(307033+403800)/2
centroderangojul=(291081+373362)/2
centroderangoago=(278225+394447)/2
centroderangosep=(277382+389821)/2
centroderangooct=(318231+421711)/2
centroderangonov=(302181+432530)/2
centroderangodic=(314805+453626)/2

print("\n centro de rango de cada mes desde 2010 hasta 2019:")
print(centroderangoene)
print(centroderangofeb)
print(centroderangomar)
print(centroderangoabr)
print(centroderangomay)
print(centroderangojun)
print(centroderangojul)
print(centroderangoago)
print(centroderangosep)
print(centroderangooct)
print(centroderangonov)
print(centroderangodic)

eneMR = fronteras[s_Cal & (es_2017 | es_2016  | es_2015 | es_2014 | es_2013 | es_2012) & es_PD & es_enero]
febMR = fronteras[s_Cal & (es_2017 | es_2016  | es_2015 | es_2014 | es_2013 | es_2012) & es_PD & es_febrero]
marMR = fronteras[s_Cal & (es_2017 | es_2016  | es_2015 | es_2014 | es_2013 | es_2012) & es_PD & es_marzo]
abrMR = fronteras[s_Cal & (es_2017 | es_2016  | es_2015 | es_2014 | es_2013 | es_2012) & es_PD & es_abril]
mayMR = fronteras[s_Cal & (es_2017 | es_2016  | es_2015 | es_2014 | es_2013 | es_2012) & es_PD & es_mayo]
junMR = fronteras[s_Cal & (es_2017 | es_2016  | es_2015 | es_2014 | es_2013 | es_2012) & es_PD & es_junio]
julMR = fronteras[s_Cal & (es_2017 | es_2016  | es_2015 | es_2014 | es_2013 | es_2012) & es_PD & es_julio]
agoMR = fronteras[s_Cal & (es_2017 | es_2016  | es_2015 | es_2014 | es_2013 | es_2012) & es_PD & es_agosto]
sepMR = fronteras[s_Cal & (es_2017 | es_2016  | es_2015 | es_2014 | es_2013 | es_2012) & es_PD & es_septiembre]
octMR = fronteras[s_Cal & (es_2017 | es_2016  | es_2015 | es_2014 | es_2013 | es_2012) & es_PD & es_octubre]
novMR = fronteras[s_Cal & (es_2017 | es_2016  | es_2015 | es_2014 | es_2013 | es_2012) & es_PD & es_noviembre]
dicMR = fronteras[s_Cal & (es_2017 | es_2016  | es_2015 | es_2014 | es_2013 | es_2012) & es_PD & es_diciembre]

anioeneMR=eneMR.describe()
aniofebMR=febMR.describe()
aniomarMR=marMR.describe()
anioabrMR=abrMR.describe()
aniomayMR=mayMR.describe()
aniojunMR=junMR.describe()
aniojulMR=julMR.describe()
anioagoMR=agoMR.describe()
aniosepMR=sepMR.describe()
aniooctMR=octMR.describe()
anionovMR=novMR.describe()
aniodicMR=dicMR.describe()

print("\n Describe de cada mes de los años 2012 a 2017 usado para sacar los datos de Media Recortada:")
print(anioeneMR)
print(aniofebMR)
print(aniomarMR)
print(anioabrMR)
print(aniomayMR)
print(aniojunMR)
print(aniojulMR)
print(anioagoMR)
print(aniosepMR)
print(aniooctMR)
print(anionovMR)
print(aniodicMR)

sumaeneMR  = eneMR.cumsum()
sumafebMR  = febMR.cumsum()
sumamarMR  = marMR.cumsum()
sumaabrMR  = abrMR.cumsum()
sumamayMR  = mayMR.cumsum()
sumajunMR  = junMR.cumsum()
sumajulMR  = julMR.cumsum()
sumaagoMR  = agoMR.cumsum()
sumasepMR  = sepMR.cumsum()
sumaoctMR  = octMR.cumsum()
sumanovMR  = novMR.cumsum()
sumadicMR  = dicMR.cumsum()

print(sumaeneMR)
print(sumafebMR)
print(sumamarMR)
print(sumaabrMR)
print(sumamayMR)
print(sumajunMR)
print(sumajulMR)
print(sumaagoMR)
print(sumasepMR)
print(sumaoctMR)
print(sumanovMR)
print(sumadicMR)

mediarecortadaene=2325257/6
mediarecortadafeb=2185960/6
mediarecortadamar=2399971/6
mediarecortadaabr=2237579/6
mediarecortadamay=2405584/6
mediarecortadajun=2192586/6
mediarecortadajul=2059628/6
mediarecortadaago=2054468/6
mediarecortadasep=2072267/6
mediarecortadaoct=2361686/6
mediarecortadanov=2394664/6
mediarecortadadic=2539465/6

print("\n media recortada de cada mes desde 2010 hasta 2019:")
print(mediarecortadaene)
print(mediarecortadafeb)
print(mediarecortadamar)
print(mediarecortadaabr)
print(mediarecortadamay)
print(mediarecortadajun)
print(mediarecortadajul)
print(mediarecortadaago)
print(mediarecortadasep)
print(mediarecortadaoct)
print(mediarecortadanov)
print(mediarecortadadic)

##---------------gráficas de cada mes de 5 en 5 años

print("\n Tabulados de las gráficas por mes de 5 en 5")
print(frontCalenede5en5)
print(frontCalfebde5en5)
print(frontCalmarde5en5)
print(frontCalabrde5en5)
print(frontCalmayde5en5)
print(frontCaljunde5en5)
print(frontCaljulde5en5)
print(frontCalagode5en5)
print(frontCalsepde5en5)
print(frontCaloctde5en5)
print(frontCalnovde5en5)
print(frontCaldicde5en5)

#x=frontCalenede5en5['Date']
#y=frontCalenede5en5['Value']
#plt.plot(x,y)
#plt.show()

#x=frontCalfebde5en5['Date']
#y=frontCalfebde5en5['Value']
#plt.plot(x,y)
#plt.show()

#x=frontCalmarzde5en5['Date']
#y=frontCalmarde5en5['Value']
#plt.plot(x,y)
#plt.show()

#x=frontCalabde5en5['Date']
#y=frontCalabde5en5['Value']
#plt.plot(x,y)
#plt.show()

#x=frontCalmayde5en5['Date']
#y=frontCalmayde5en5['Value']
#plt.plot(x,y)
#plt.show()

#x=frontCaljunde5en5['Date']
#y=frontCaljunde5en5['Value']
#plt.plot(x,y)
#plt.show()

#x=frontCaljulde5en5['Date']
#y=frontCaljulde5en5['Value']
#plt.plot(x,y)
#plt.show()

#x=frontCalagode5en5['Date']
#y=frontCalagode5en5['Value']
#plt.plot(x,y)
#plt.show()

#x=frontCalseptde5en5['Date']
#y=frontCalseptde5en5['Value']
#plt.plot(x,y)
#plt.show()

#x=frontCaloctde5en5['Date']
#y=frontCaloctde5en5['Value']
#plt.plot(x,y)
#plt.show()

#x=frontCalnovde5en5['Date']
#y=frontCalnovde5en5['Value']
#plt.plot(x,y)
#plt.show()

#x=frontCaldicde5en5['Date']
#y=frontCaldicde5en5['Value']
#plt.plot(x,y)
#plt.show()

#2000,2005,2010,2015,2018,2019

##---------------gráficas de cada mes por 10 años (2010 a 2019)

print("\n Tabulados de las gráficas por mes de 2012 a 2017")
print(frontCalenede10)
print(frontCalfebde10)
print(frontCalmarde10)
print(frontCalabrde10)
print(frontCalmayde10)
print(frontCaljunde10)
print(frontCaljulde10)
print(frontCalagode10)
print(frontCalsepde10)
print(frontCaloctde10)
print(frontCalnovde10)
print(frontCaldicde10)

#x=frontCalenede10['Date']
#y=frontCalenede10['Value']
#plt.plot(x,y)
#plt.show()

#x=frontCalfebde10['Date']
#y=frontCalfebde10['Value']
#plt.plot(x,y)
#plt.show()

#x=frontCalmarzde10['Date']
#y=frontCalmarde10['Value']
#plt.plot(x,y)
#plt.show()

#x=frontCalabde10['Date']
#y=frontCalabde10['Value']
#plt.plot(x,y)
#plt.show()

#x=frontCalmayde10['Date']
#y=frontCalmayde10['Value']
#plt.plot(x,y)
#plt.show()

#x=frontCaljunde10['Date']
#y=frontCaljunde10['Value']
#plt.plot(x,y)
#plt.show()

#x=frontCaljulde10['Date']
#y=frontCaljulde10['Value']
#plt.plot(x,y)
#plt.show()

#x=frontCalagode10['Date']
#y=frontCalagode10['Value']
#plt.plot(x,y)
#plt.show()

#x=frontCalseptde10['Date']
#y=frontCalseptde10['Value']
#plt.plot(x,y)
#plt.show()

#x=frontCaloctde10['Date']
#y=frontCaloctde10['Value']
#plt.plot(x,y)
#plt.show()

#x=frontCalnovde10['Date']
#y=frontCalnovde10['Value']
#plt.plot(x,y)
#plt.show()

#x=frontCaldicde10['Date']
#y=frontCaldicde10['Value']
#plt.plot(x,y)
#plt.show()
