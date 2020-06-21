# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 19:17:48 2019

@author: Salim
"""
import numpy as np
import random
import sys
class Array():
    def liste(self):
        con_3=np.array([0.000000,17.441360,44.725970,62.719330,16.893600,14.338010,50.145510,38.597610,55.251690,8.725719,57.534000,51.575570,6.735546,53.410430,18.036370,12.321110,15.766080,10.487350,16.510170,44.110700,12.810270,15.072460,8.935379,17.444950,14.147550,7.837661,45.727540,55.729640,34.894070,47.260680,13.393080,28.105960,10.416400,2.904094,13.671980,7.094555,13.429530,10.505730,13.347480,51.588650,40.373110,5.200551,16.253710,34.614060,15.315650,15.175810,25.752660,54.019210,14.705660,38.908190,14.263400,
                    17.441360,0.000000,29.126060,59.024190,16.699790,31.763990,51.976720,31.525700,40.475570,9.150531,71.683600,46.049410,14.911510,70.836860,33.749370,12.661290,24.760360,18.989370,13.601780,35.235570,28.318090,4.562924,8.692504,14.218470,28.090530,22.740180,53.129960,54.617100,52.264110,42.572100,28.290740,13.962190,7.032325,15.341120,22.544650,15.354710,30.585810,18.998900,21.813840,39.095820,33.503280,22.411490,22.493330,32.950620,32.293880,31.377990,32.306150,67.202990,4.645046,50.514450,5.411783,
                    44.725970,29.126060,0.000000,47.324300,32.884310,58.069470,76.421450,24.056750,41.734660,36.106970,88.077240,34.336320,39.490880,96.051500,56.618800,41.610000,53.817100,40.609970,41.516430,21.520030,56.890990,33.481500,36.066950,41.818830,50.112060,51.320970,60.835910,48.366000,77.394230,62.126910,51.206780,16.689490,35.092090,41.995210,42.306550,44.342110,56.065720,48.124840,41.649020,47.100270,52.405360,48.797360,39.958350,34.039440,60.036640,55.241300,44.974250,96.312340,33.651200,64.959980,30.544130,
                    62.719330,59.024190,47.324300,0.000000,46.300350,68.209030,110.428800,27.864590,88.320990,58.408580,68.742530,13.569080,56.165830,93.772010,60.369910,69.078970,78.117400,52.494660,71.733500,26.578640,74.262210,62.864070,58.997070,72.549580,55.911230,70.364620,36.975700,10.404050,78.717540,101.319400,57.849770,47.857290,59.688610,60.210290,50.328980,67.600000,65.150020,72.120760,50.321480,92.033360,91.883550,62.996410,47.098180,28.105290,73.417710,61.490310,40.865350,114.366000,62.727590,50.023950,55.518860,
                    16.893600,16.699790,32.884310,46.300350,0.000000,26.836130,64.625950,21.802230,56.376000,12.402190,57.440280,34.738740,10.159630,63.367180,23.814440,23.299970,31.853750,8.377082,26.557820,27.561540,29.403280,18.845510,13.076060,27.477010,17.297600,24.728540,36.469410,40.152870,44.833710,58.025140,18.545840,17.162920,14.186150,14.158260,9.424003,21.301710,24.322490,25.821480,8.778733,55.715920,49.477440,18.708320,7.341645,18.386280,30.380720,22.719580,15.839440,70.651810,18.578210,35.130730,11.485510,
                    14.338010,31.763990,58.069470,68.209030,26.836130,0.000000,53.906950,47.918530,68.653070,22.837720,46.884320,58.959390,18.578870,39.074590,9.689996,24.819820,20.802660,18.464600,28.658130,54.027710,10.546990,29.293380,23.156570,29.437710,12.305300,12.426210,43.206810,59.701410,20.584360,55.770550,10.363370,41.391020,24.731900,16.554680,18.813770,19.092100,3.071381,19.456600,19.109210,64.044500,50.603070,9.444302,22.181950,41.076660,5.968090,7.231863,27.571870,46.177600,28.935840,32.539650,28.186330,
                    50.145510,51.976720,76.421450,110.428800,64.625950,53.906950,0.000000,83.406010,52.289730,52.245570,99.316380,97.828210,55.696380,77.333240,63.220760,41.408820,34.736560,60.434570,38.739610,87.178020,43.475300,47.783540,51.603680,37.963670,62.656860,44.184810,95.374200,104.778700,65.963600,19.017050,61.155470,65.207860,50.773780,51.922950,63.812290,43.808680,56.088100,39.682030,63.458390,42.333310,26.206780,52.422130,66.206320,82.966550,48.361890,60.258200,75.895420,41.861870,47.876710,86.285920,54.940150,
                    38.597610,31.525700,24.056750,27.864590,21.802230,47.918530,83.406010,0.000000,61.924930,32.468810,66.936730,14.563430,31.878860,81.435800,42.757220,42.518780,52.826150,29.752170,44.704150,6.389984,51.203040,35.622570,32.932450,45.452180,36.700570,46.427430,37.522810,25.661680,63.708710,73.513990,38.400530,20.045090,33.243600,35.777160,29.170970,42.075560,45.135970,46.635610,28.822830,64.722430,64.036240,40.423760,25.862340,11.089080,51.981920,42.613750,25.694280,92.453200,35.531570,44.001760,28.645700,
                    55.251690,40.475570,41.734660,88.320990,56.376000,68.653070,52.289730,61.924930,0.000000,48.877030,111.983600,74.882830,54.972080,106.253500,73.119930,43.841580,51.845920,59.414990,40.167550,61.773600,61.098790,40.714450,48.219280,39.493940,68.081470,56.708290,92.491580,87.585830,88.773000,33.389170,67.965370,43.158220,46.341540,54.191790,63.018640,49.561260,68.475620,49.919430,62.289010,10.085070,27.199750,60.412320,62.836560,68.547360,66.767200,70.384680,72.212450,87.535030,41.091650,90.972860,45.837250,
                    8.725719,9.150531,36.106970,58.408580,12.402190,22.837720,52.245570,32.468810,48.877030,0.000000,63.108780,46.329150,6.107328,61.855510,24.665480,10.900430,20.383930,10.924810,14.322600,37.413090,20.887160,8.277115,0.760732,15.271890,19.230850,15.394210,46.936140,52.542980,43.224890,46.068920,19.271400,19.591420,2.564218,6.287942,14.760920,9.641353,21.495950,14.180580,14.100680,46.460330,37.942840,13.407810,15.703190,30.722760,24.007140,22.238690,25.999940,61.472740,7.911581,42.654550,5.568200,
                    57.534000,71.683600,88.077240,68.742530,57.440280,46.884320,99.316380,66.936730,111.983600,63.108780,0.000000,68.365170,57.011570,36.195720,39.584500,69.800540,67.681380,52.704800,73.960350,72.719230,57.240780,71.314930,63.773800,74.863730,43.954370,58.995840,32.126940,58.443110,34.761150,102.654700,44.260760,74.258760,65.651120,58.066010,49.308640,64.218120,45.699520,65.824250,50.055480,109.069600,97.177440,52.715630,50.213730,55.855870,51.588380,42.601090,43.143840,76.981990,70.939990,23.143500,66.470520,
                    51.575570,46.049410,34.336320,13.569080,34.738740,58.959390,97.828210,14.563430,74.882830,46.329150,68.365170,0.000000,44.867370,88.665140,52.229090,56.713330,66.482700,41.839720,59.091750,13.114910,63.743560,50.070920,46.857280,59.865510,46.928220,59.379800,36.475110,14.847300,72.137280,88.057850,48.804700,34.389340,47.351490,48.890170,40.322940,55.791850,55.984260,60.356390,40.165340,78.468810,78.550460,52.595400,36.957360,17.904920,63.683910,52.788130,33.034770,104.642800,49.963570,47.000680,42.927030,
                    6.735546,14.911510,39.490880,56.165830,10.159630,18.578870,55.696380,31.878860,54.972080,6.107328,57.011570,44.867370,0.000000,57.081890,18.904350,15.382250,22.000680,5.162592,19.315500,37.455650,19.384350,14.371870,6.798824,20.292620,13.197830,14.572790,41.555310,49.458290,38.369640,51.067780,13.397610,22.813190,8.665969,4.046890,9.007251,11.889450,16.697370,16.193550,8.426597,52.515890,43.350720,9.409357,10.655150,28.079170,21.042200,16.712140,20.830450,60.652730,14.002840,36.631860,10.215640,
                    53.410430,70.836860,96.051500,93.772010,63.367180,39.074590,77.333240,81.435800,106.253500,61.855510,36.195720,88.665140,57.081890,0.000000,39.568070,62.884820,54.740840,55.441560,66.221150,87.825660,45.163220,68.263310,62.206070,66.828820,46.076970,49.839280,58.408190,83.592460,18.715600,86.724430,44.865760,79.599560,63.804530,55.569330,54.015020,57.428030,40.437270,56.391000,54.615090,100.339200,84.460110,48.453600,56.794300,71.830950,39.636310,40.812060,56.141780,44.862840,67.914210,44.223930,67.077220,
                    18.036370,33.749370,56.618800,60.369910,23.814440,9.689996,63.220760,42.757220,73.119930,24.665480,39.584500,52.229090,18.904350,39.568070,0.000000,30.232150,29.240720,16.143920,34.381560,49.096530,19.758470,32.499610,25.227590,35.281040,6.517211,19.948830,33.554870,51.362140,21.170080,63.753500,5.573754,40.388950,27.069450,18.940260,14.447530,24.633840,7.143085,26.467310,15.049150,69.622630,57.734620,13.131320,17.317540,34.420460,15.652630,3.101796,19.534400,54.688180,32.121680,23.065440,29.091890,
                    12.321110,12.661290,41.610000,69.078970,23.299970,24.819820,41.408820,42.518780,43.841580,10.900430,69.800540,56.713330,15.382250,62.884820,30.232150,0.000000,12.224820,20.524830,4.191802,46.938850,18.045660,8.153533,10.226650,5.139704,26.400630,13.045590,56.907370,63.422040,45.015100,35.691370,25.713590,26.551950,9.391809,12.500230,24.318680,5.754277,24.827370,7.090201,23.779560,39.489990,28.236110,17.116950,25.971970,41.574700,23.253490,27.271590,36.207110,54.740740,8.023494,51.064780,13.889200,
                    15.766080,24.760360,53.817100,78.117400,31.853750,20.802660,34.736560,52.826150,51.845920,20.383930,67.681380,66.482700,22.000680,54.740840,29.240720,12.224820,0.000000,26.249080,13.442710,57.779850,10.605850,20.336060,19.976550,13.645110,27.976310,9.512626,60.645980,71.419280,38.303460,34.984200,26.553090,38.453630,20.021660,17.986340,29.360250,10.751550,22.321770,6.206908,29.080330,45.598680,30.413270,17.692100,32.019790,50.062480,16.560530,26.166210,41.333180,42.516060,20.173820,52.111750,24.947560,
                    10.487350,18.989370,40.609970,52.494660,8.377082,18.464600,60.434570,29.752170,59.414990,10.924810,52.704800,41.839720,5.162592,55.441560,16.143920,20.524830,26.249080,0.000000,24.477460,35.715980,21.915900,19.153740,11.667200,25.454700,9.770262,17.892200,36.395100,45.278040,36.798110,56.215850,10.631100,24.255690,13.465970,8.523816,3.863689,16.703230,15.955060,20.766910,3.264030,57.350030,48.507880,10.775730,5.786211,24.440460,22.229750,14.634310,15.732340,62.903150,18.796960,31.769200,13.780420,
                    16.510170,13.601780,41.516430,71.733500,26.557820,28.658130,38.739610,44.704150,40.167550,14.322600,73.960350,59.091750,19.315500,66.221150,34.381560,4.191802,13.442710,24.477460,0.000000,48.737570,21.100740,9.158908,13.591440,0.977800,30.590220,16.542400,60.870050,66.477910,48.606080,31.810140,29.903220,27.469410,12.377020,16.634090,28.306010,9.787571,28.833650,9.843779,27.740970,35.455070,24.111470,21.254010,29.791890,44.595630,26.628280,31.401940,40.074230,55.439020,9.205262,55.236920,16.215370,
                    44.110700,35.235570,21.520030,26.578640,27.561540,54.027710,87.178020,6.389984,61.773600,37.413090,72.719230,13.114910,37.455650,87.825660,49.096530,46.938850,57.779850,35.715980,48.737570,0.000000,56.839410,39.579200,37.803320,49.414750,42.986380,51.894390,42.543400,26.851500,70.081510,76.190410,44.657170,22.337640,37.889530,41.242970,35.364390,47.052960,51.293990,51.573020,34.982780,65.529990,66.549090,46.267990,32.093270,16.986200,57.911690,48.884160,32.024560,98.108220,39.537800,49.944190,33.089740,
                    12.810270,28.318090,56.890990,74.262210,29.403280,10.546990,43.475300,51.203040,61.098790,20.887160,57.240780,63.743560,19.384350,45.163220,19.758470,18.045660,10.605850,21.915900,21.100740,56.839410,0.000000,24.696040,20.854060,21.677460,20.127130,5.590368,52.645730,66.563990,28.001880,45.519510,18.372850,40.472570,21.817990,15.713630,23.969240,13.170640,12.617800,11.257110,23.944140,55.536030,40.948930,11.266100,27.164120,46.308240,5.984415,16.846430,34.969320,41.270900,24.404170,42.820770,26.395410,
                    15.072460,4.562924,33.481500,62.864070,18.845510,29.293380,47.783540,35.622570,40.714450,8.277115,71.314930,50.070920,14.371870,68.263310,32.499610,8.153533,20.336060,19.153740,9.158908,39.579200,24.696040,0.000000,7.573043,9.850127,27.375970,19.203330,54.718450,58.017390,49.877170,39.326010,27.262680,18.524270,5.712964,13.574650,22.952800,11.534430,28.498070,14.756400,22.269590,38.197870,30.635070,20.254140,23.563770,36.187980,29.125640,29.877840,33.750490,62.836820,0.378122,50.914820,7.578344,
                    8.935379,8.692504,36.066950,58.997070,13.076060,23.156570,51.603680,32.932450,48.219280,0.760732,63.773800,46.857280,6.798824,62.206070,25.227590,10.226650,19.976550,11.667200,13.591440,37.803320,20.854060,7.573043,0.000000,14.537320,19.869790,15.322010,47.696860,53.198760,43.599940,45.322670,19.866220,19.626880,1.877763,6.654852,15.508460,9.266692,21.898200,13.769700,14.851390,45.738030,37.183720,13.753900,16.463740,31.363420,24.145120,22.757810,26.760070,61.273380,7.204202,43.381700,5.541492,
                    17.444950,14.218470,41.818830,72.549580,27.477010,29.437710,37.963670,45.452180,39.493940,15.271890,74.863730,59.865510,20.292620,66.828820,35.281040,5.139704,13.645110,25.454700,0.977800,49.414750,21.677460,9.850127,14.537320,0.000000,31.539740,17.247850,61.846850,67.356750,49.296130,30.841710,30.837300,28.009890,13.291460,17.603980,29.283710,10.662410,29.670890,10.439490,28.718280,34.633260,23.137000,22.150360,30.762960,45.474810,27.275020,32.291410,41.047230,55.378910,9.923049,56.198860,17.033700,
                    14.147550,28.090530,50.112060,55.911230,17.297600,12.305300,62.656860,36.700570,68.081470,19.230850,43.954370,46.928220,13.197830,46.076970,6.517211,26.400630,27.976310,9.770262,30.590220,42.986380,20.127130,27.375970,19.869790,31.539740,0.000000,18.479140,32.755520,47.426160,27.612650,61.270100,1.942989,33.942060,21.746380,14.190280,7.955299,21.211190,9.240363,23.995830,8.538875,65.204930,54.520660,10.348190,10.963540,29.024120,17.775900,5.931709,15.317670,58.482650,26.999890,24.782020,23.168950,
                    7.837661,22.740180,51.320970,70.364620,24.728540,12.426210,44.184810,46.427430,56.708290,15.394210,58.995840,59.379800,14.572790,49.839280,19.948830,13.045590,9.512626,17.892200,16.542400,51.894390,5.590368,19.203330,15.322010,17.247850,18.479140,0.000000,51.194120,63.111000,32.064770,43.838500,17.040500,34.948800,16.236350,10.658590,20.551810,7.753275,13.303450,7.037968,20.380410,51.724930,38.249240,8.277568,23.493920,42.275700,10.213320,16.850140,32.256310,46.313010,18.900550,42.658500,20.860730,
                    45.727540,53.129960,60.835910,36.975700,36.469410,43.206810,95.374200,37.522810,92.491580,46.936140,32.126940,36.475110,41.555310,58.408190,33.554870,56.907370,60.645980,36.395100,60.870050,42.543400,52.645730,54.718450,47.696860,61.846850,32.755520,51.194120,0.000000,26.580840,46.027460,92.594100,34.357370,50.260140,49.324410,44.590740,32.589160,52.661270,40.421070,56.167050,33.133600,92.185330,84.843170,42.954310,31.236150,26.821940,49.173420,36.070240,20.970790,86.945990,54.401230,14.322740,47.801700,
                    55.729640,54.617100,48.366000,10.404050,40.152870,59.701410,104.778700,25.661680,87.585830,52.542980,58.443110,14.847300,49.458290,83.592460,51.362140,63.422040,71.419280,45.278040,66.477910,26.851500,66.563990,58.017390,53.198760,67.356750,47.426160,63.111000,26.580840,0.000000,68.941380,97.185930,49.366980,45.241620,54.151100,53.440000,42.650240,61.233820,56.630090,65.640060,42.756820,90.193880,88.054790,55.356200,39.617140,21.882320,65.157490,52.755950,32.130350,105.839400,57.828900,39.687870,50.467470,
                    34.894070,52.264110,77.394230,78.717540,44.833710,20.584360,65.963600,63.708710,88.773000,43.224890,34.761150,72.137280,38.369640,18.715600,21.170080,45.015100,38.303460,36.798110,48.606080,70.081510,28.001880,49.877170,43.599940,49.296130,27.612650,32.064770,46.027460,68.941380,0.000000,72.256100,26.289250,60.902360,45.237810,36.948840,35.567310,39.396730,21.754040,38.919780,36.134970,83.522800,68.674080,29.852860,38.487530,54.712200,22.110810,22.166300,39.129860,43.194050,49.520010,31.939050,48.393570,
                    47.260680,42.572100,62.126910,101.319400,58.025140,55.770550,19.017050,73.513990,33.389170,46.068920,102.654700,88.057850,51.067780,86.724430,63.753500,35.691370,34.984200,56.215850,31.810140,76.190410,45.519510,39.326010,45.322670,30.841710,61.270100,43.838500,92.594100,97.185930,72.256100,0.000000,60.217820,53.870960,43.932630,48.054370,60.005420,40.174560,57.099950,37.388400,59.470830,23.367030,9.766177,51.104950,61.599780,75.449490,51.369500,60.651790,71.872850,57.976570,39.553180,86.026590,46.900440,
                    13.393080,28.290740,51.206780,57.849770,18.545840,10.363370,61.155470,38.400530,67.965370,19.271400,44.260760,48.804700,13.397610,44.865760,5.573754,25.713590,26.553090,10.631100,29.903220,44.657170,18.372850,27.262680,19.866220,30.837300,1.942989,17.040500,34.357370,49.366980,26.289250,60.217820,0.000000,34.885860,21.728390,13.823410,9.401124,20.349130,7.300321,22.853170,9.907978,64.810100,53.680130,9.122973,12.570520,30.899900,15.851640,4.247010,17.253340,56.540280,26.884760,25.821810,23.551320,
                    28.105960,13.962190,16.689490,47.857290,17.162920,41.391020,65.207860,20.045090,43.158220,19.591420,74.258760,34.389340,22.813190,79.599560,40.388950,26.551950,38.453630,24.255690,27.469410,22.337640,40.472570,18.524270,19.626880,28.009890,33.942060,34.948800,50.260140,45.241620,60.902360,53.870960,34.885860,0.000000,18.868100,25.339620,26.384380,28.357850,39.436900,32.463480,25.681010,44.976190,44.263720,32.107990,24.494390,25.389150,43.395600,38.813350,31.481850,80.623280,18.588990,51.525490,14.089470,
                    10.416400,7.032325,35.092090,59.688610,14.186150,24.731900,50.773780,33.243600,46.341540,2.564218,65.651120,47.351490,8.665969,63.804530,27.069450,9.391809,20.021660,13.465970,12.377020,37.889530,21.817990,5.712964,1.877763,13.291460,21.746380,16.236350,49.324410,54.151100,45.237810,43.932630,21.728390,18.868100,0.000000,8.358136,17.287670,9.540352,23.585570,13.857440,16.617250,43.900990,35.640590,15.388240,18.093540,32.276230,25.427960,24.567290,28.363550,61.795360,5.347975,45.211830,4.938620,
                    2.904094,15.341120,41.995210,60.210290,14.158260,16.554680,51.922950,35.777160,54.191790,6.287942,58.066010,48.890170,4.046890,55.569330,18.940260,12.500230,17.986340,8.523816,16.634090,41.242970,15.713630,13.574650,6.654852,17.603980,14.190280,10.658590,44.590740,53.440000,36.948840,48.054370,13.823410,25.339620,8.358136,0.000000,12.092490,8.188496,15.244870,12.288950,11.646740,51.028040,40.733230,7.119957,14.283700,32.119340,18.057720,16.306760,24.186190,56.906380,13.197430,38.633690,11.678280,
                    13.671980,22.544650,42.306550,50.328980,9.424003,18.813770,63.812290,29.170970,63.018640,14.760920,49.308640,40.322940,9.007251,54.015020,14.447530,24.318680,29.360250,3.863689,28.306010,35.364390,23.969240,22.952800,15.508460,29.283710,7.955299,20.551810,32.589160,42.650240,35.567310,60.005420,9.401124,26.384380,17.287670,12.092490,0.000000,20.265360,15.973340,24.141200,0.748420,61.133210,52.357760,12.718750,3.378186,22.560980,23.363410,13.646500,12.115730,64.355490,22.600370,28.028820,17.223340,
                    7.094555 ,15.354710,44.342110,67.600000,21.301710,19.092100,43.808680,42.075560,49.561260,9.641353,64.218120,55.791850,11.889450,57.428030,24.633840,5.754277,10.751550,16.703230,9.787571,47.052960,13.170640,11.534430,9.266692,10.662410,21.211190,7.753275,52.661270,61.233820,39.396730,40.174560,20.349130,28.357850,9.540352,8.188496,20.265360,0.000000,19.078950,4.567841,19.833160,45.217950,33.334110,11.504380,22.437230,39.643050,17.893960,21.632230,32.370430,52.270160,11.251130,45.987820,14.464790,
                    13.429530,30.585810,56.065720,65.150020,24.322490,3.071381,56.088100,45.135970,68.475620,21.495950,45.699520,55.984260,16.697370,40.437270,7.143085,24.827370,22.321770,15.955060,28.833650,51.293990,12.617800,28.498070,21.898200,29.670890,9.240363,13.303450,40.421070,56.630090,21.754040,57.099950,7.300321,39.436900,23.585570,15.244870,15.973340,19.078950,0.000000,20.151610,16.316100,64.287250,51.498130,8.247208,19.319750,38.089860,8.841387,4.351112,24.500720,49.245530,28.129740,30.202990,26.642100,
                    10.505730,18.998900,48.124840,72.120760,25.821480,19.456600,39.682030,46.635610,49.919430,14.180580,65.824250,60.356390,16.193550,56.391000,26.467310,7.090201,6.206908,20.766910,9.843779,51.573020,11.257110,14.756400,13.769700,10.439490,23.995830,7.037968,56.167050,65.640060,38.919780,37.388400,22.853170,32.463480,13.857440,12.288950,24.141200,4.567841,20.151610,0.000000,23.777240,44.718400,31.353920,13.730620,26.548770,44.125730,16.851490,23.375240,36.244140,48.231200,14.543410,48.674960,18.793630,
                    13.347480,21.813840,41.649020,50.321480,8.778733,19.109210,63.458390,28.822830,62.289010,14.100680,50.055480,40.165340,8.426597,54.615090,15.049150,23.779560,29.080330,3.264030,27.740970,34.982780,23.944140,22.269590,14.851390,28.718280,8.538875,20.380410,33.133600,42.756820,36.134970,59.470830,9.907978,25.681010,16.617250,11.646740,0.748420,19.833160,16.316100,23.777240,0.000000,60.439670,51.769660,12.678580,3.234008,22.464030,23.525790,14.142810,12.540160,64.484610,21.919080,28.742260,16.485380,
                    51.588650,39.095820,47.100270,92.033360,55.715920,64.044500,42.333310,64.722430,10.085070,46.460330,109.069600,78.468810,52.515890,100.339200,69.622630,39.489990,45.598680,57.350030,35.455070,65.529990,55.536030,38.197870,45.738030,34.633260,65.204930,51.724930,92.185330,90.193880,83.522800,23.367030,64.810100,44.976190,43.900990,51.028040,61.133210,45.217950,64.287250,44.718400,60.439670,0.000000,18.033230,56.569450,61.492340,69.950160,61.415610,66.715480,71.401980,78.723180,38.557160,89.112110,44.480500,
                    40.373110,33.503280,52.405360,91.883550,49.477440,50.603070,26.206780,64.036240,27.199750,37.942840,97.177440,78.550460,43.350720,84.460110,57.734620,28.236110,30.413270,48.507880,24.111470,66.549090,40.948930,30.635070,37.183720,23.137000,54.520660,38.249240,84.843170,88.054790,68.674080,9.766177,53.680130,44.263720,35.640590,40.733230,52.357760,33.334110,51.498130,31.353920,51.769660,18.033230,0.000000,44.717290,53.636250,66.453480,46.931640,54.662210,63.938350,60.690090,30.899240,79.262830,38.132240,
                    5.200551,22.411490,48.797360,62.996410,18.708320,9.444302,52.422130,40.423760,60.412320,13.407810,52.715630,52.595400,9.409357,48.453600,13.131320,17.116950,17.692100,10.775730,21.254010,46.267990,11.266100,20.254140,13.753900,22.150360,10.348190,8.277568,42.954310,55.356200,29.852860,51.104950,9.122973,32.107990,15.388240,7.119957,12.718750,11.504380,8.247208,13.730620,12.678580,56.569450,44.717290,0.000000,15.898230,35.065850,11.725400,10.154950,24.079270,52.130240,19.885040,34.944690,18.744520,
                    16.253710,22.493330,39.958350,47.098180,7.341645,22.181950,66.206320,25.862340,62.836560,15.703190,50.213730,36.957360,10.655150,56.794300,17.317540,25.971970,32.019790,5.786211,29.791890,32.093270,27.164120,23.563770,16.463740,30.762960,10.963540,23.493920,31.236150,39.617140,38.487530,61.599780,12.570520,24.494390,18.093540,14.283700,3.378186,22.437230,19.319750,26.548770,3.234008,61.492340,53.636250,15.898230,0.000000,19.231960,26.726590,16.808800,10.303180,67.703900,23.234650,28.208210,17.081880,
                    34.614060,32.950620,34.039440,28.105290,18.386280,41.076660,82.966550,11.089080,68.547360,30.722760,55.855870,17.904920,28.079170,71.830950,34.420460,41.574700,50.062480,24.440460,44.595630,16.986200,46.308240,36.187980,31.363420,45.474810,29.024120,42.275700,26.821940,21.882320,54.712200,75.449490,30.899900,25.389150,32.276230,32.119340,22.560980,39.643050,38.089860,44.125730,22.464030,69.950160,66.453480,35.065850,19.231960,0.000000,45.905920,34.892400,15.693270,86.912670,35.989230,32.975730,28.620490,
                    15.315650,32.293880,60.036640,73.417710,30.380720,5.968090,48.361890,51.981920,66.767200,24.007140,51.588380,63.683910,21.042200,39.636310,15.652630,23.253490,16.560530,22.229750,26.628280,57.911690,5.984415,29.125640,24.145120,27.275020,17.775900,10.213320,49.173420,65.157490,22.110810,51.369500,15.851640,43.395600,25.427960,18.057720,23.363410,17.893960,8.841387,16.851490,23.525790,61.415610,46.931640,11.725400,26.726590,45.905920,0.000000,13.151570,33.087290,41.015090,28.800790,38.372530,29.566290,
                    15.175810,31.377990,55.241300,61.490310,22.719580,7.231863,60.258200,42.613750,70.384680,22.238690,42.601090,52.788130,16.712140,40.812060,3.101796,27.271590,26.166210,14.634310,31.401940,48.884160,16.846430,29.877840,22.757810,32.291410,5.931709,16.850140,36.070240,52.755950,22.166300,60.651790,4.247010,38.813350,24.567290,16.306760,13.646500,21.632230,4.351112,23.375240,14.142810,66.715480,54.662210,10.154950,16.808800,34.892400,13.151570,0.000000,20.665300,53.090850,29.501100,26.045470,26.924640,
                    25.752660,32.306150,44.974250,40.865350,15.839440,27.571870,75.895420,25.694280,72.212450,25.999940,43.143840,33.034770,20.830450,56.141780,19.534400,36.207110,41.333180,15.732340,40.074230,32.024560,34.969320,33.750490,26.760070,41.047230,15.317670,32.256310,20.970790,32.130350,39.129860,71.872850,17.253340,31.481850,28.363550,24.186190,12.115730,32.370430,24.500720,36.244140,12.540160,71.401980,63.938350,24.079270,10.303180,15.693270,33.087290,20.665300,0.000000,73.717610,33.431870,20.129230,26.931480,
                    54.019210,67.202990,96.312340,114.366000,70.651810,46.177600,41.861870,92.453200,87.535030,61.472740,76.981990,104.642800,60.652730,44.862840,54.688180,54.740740,42.516060,62.903150,55.439020,98.108220,41.270900,62.836820,61.273380,55.378910,58.482650,46.313010,86.945990,105.839400,43.194050,57.976570,56.540280,80.623280,61.795360,56.906380,64.355490,52.270160,49.245530,48.231200,64.484610,78.723180,60.690090,52.130240,67.703900,86.912670,41.015090,53.090850,73.717610,0.000000,62.661850,73.772600,66.685840,
                    14.705660,4.645046,33.651200,62.727590,18.578210,28.935840,47.876710,35.531570,41.091650,7.911581,70.939990,49.963570,14.002840,67.914210,32.121680,8.023494,20.173820,18.796960,9.205262,39.537800,24.404170,0.378122,7.204202,9.923049,26.999890,18.900550,54.401230,57.828900,49.520010,39.553180,26.884760,18.588990,5.347975,13.197430,22.600370,11.251130,28.129740,14.543410,21.919080,38.557160,30.899240,19.885040,23.234650,35.989230,28.800790,29.501100,33.431870,62.661850,0.000000,50.555000,7.369691,
                    38.908190,50.514450,64.959980,50.023950,35.130730,32.539650,86.285920,44.001760,90.972860,42.654550,23.143500,47.000680,36.631860,44.223930,23.065440,51.064780,52.111750,31.769200,55.236920,49.944190,42.820770,50.914820,43.381700,56.198860,24.782020,42.658500,14.322740,39.687870,31.939050,86.026590,25.821810,51.525490,45.211830,38.633690,28.028820,45.987820,30.202990,48.674960,28.742260,89.112110,79.262830,34.944690,28.208210,32.975730,38.372530,26.045470,20.129230,73.772600,50.555000,0.000000,45.136610,
                    14.263400,5.411783,30.544130,55.518860,11.485510,28.186330,54.940150,28.645700,45.837250,5.568200,66.470520,42.927030,10.215640,67.077220,29.091890,13.889200,24.947560,13.780420,16.215370,33.089740,26.395410,7.578344,5.541492,17.033700,23.168950,20.860730,47.801700,50.467470,48.393570,46.900440,23.551320,14.089470,4.938620,11.678280,17.223340,14.464790,26.642100,18.793630,16.485380,44.480500,38.132240,18.744520,17.081880,28.620490,29.566290,26.924640,26.931480,66.685840,7.369691,45.136610,0.000000,
                    ])
        return con_3
    """def carplazlama(self,p1,p2):
        try:
            s1=random.randint(0,20)
            s2=random.randint(25,50)
            while (s1 is s2):
                s1=random.randint(0,20)
                s2=random.randint(25,50)
            p1.remove(1)
            p2.remove(1)
            p1.remove(1)
            p2.remove(1)
            c=list(range(len(p2)))
            for i in range(len(c)):
                c[i]="_"
            yavru1=p1[s1:s2]
            yavru2=p2[s1:s2]
            c[s1:s2]=p1[s1:s2]
            index=[]
            for i in yavru1:
                for j in p2:
                    if i is j:
                        ind=p2.index(i)
                        index.append(ind)
            for i in range(len(index)):
                c[index[i]]=yavru2[i]
            index2=[]
            for i in range(len(c)):
                if c[i]=="_":
                    index2.append(i)  
            for i in range(len(index2)):
                c[index2[i]]=p2[index2[i]]        
            c.insert(0,1)
            c.insert(len(c),1)
            return c
        except Exception as e:
            print("Error p1 ")
            print(p1)
            print("------------ p2")
            print(p2)
            print("------------ s1")
            print(s1)
            print("------------ s2")
            print(s2)
            print(e)"""
    def carplazlama(self,p1, p2):
        s1=random.randint(0,20)
        s2=random.randint(25,50)
        while (s1 is s2):
            s1=random.randint(0,20)
            s2=random.randint(25,50)
        p1.remove(1)
        p2.remove(1)
        p1.remove(1)
        p2.remove(1)
        p1[s1:s2]=p2[s1:s2]
        olmayan_elemanlar=[]
        for i in range(len(p2)):
            if not(p2[i] in p1):
                olmayan_elemanlar.append(p2[i])
        p3=p1.copy()
        for i in range(len(p3)+2):
            if i in p3:
                p3.remove(i)
            else:
                continue
        for i in range(len(p3)):
            ind=p1.index(p3[i])
            p1[ind]=olmayan_elemanlar[i]
        p1.insert(0,1)
        p1.insert(len(p1),1)
        return p1        
        

    def mutasyon(self,p1):
        p1.remove(1)
        p1.remove(1)
        ind1=random.randint(0,len(p1))
        sayı=random.choice(p1)
        ind=p1.index(sayı)
        while (ind is ind1):
            ind1=random.randint(0,len(p1))
        p1.remove(sayı)
        p1.insert(ind1,sayı)
        p1.insert(0,1)
        p1.insert(len(p1),1)
        return p1
            