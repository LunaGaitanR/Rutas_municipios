import pandas as pd

def getGraph():
    graph={
        #'CiudadOrigen':{'Vecino1': distancia,'vecino2':d},
        'Acacías':{'San Martin': 33,'Tauramena':142},
        'Aguadas':{'Marmato': 22,'Villeta':128},
        'Aipe':{'Vistahermosa': 172,'Campoalegre':65},
        'Bogotá':{'Ibague': 133,'La Calera':12,'Salamina':175},
        'Campoalegre':{'Aipe':65,'Rivera':13,'Gigante':51},
        'Chía':{'La Calera':19,'Villeta':49,'Sopo':14},
        'Chocontá':{'Ubaté':26,'Villeta':49,'Sopo':38},        
        'Garzón':{'Pitalito':60,'Puerto Rico':61,'Gigante':14},
        'Gigante':{'Garzón':14,'Campoalegre':51},
        'Hato Corozal':{'Ubaté':246,'Paz de Ariporo':34},
        'Ibague':{'Bogotá': 133,'Palermo':174},
        'La Calera':{'Bogotá': 12,'Chía':19},
        'La Dorada':{'Neira':100,'Villeta':55},
        'Manizales':{'Neira':12,'Palermo':241},
        'Marmato':{'Aguadas':22,'Salamina':15},
        'Neira':{'La Dorada':100,'Manizales':12},
        'Palermo':{'Ibague':174,'Manizales':241,'Rivera':23},
        'Paz de Ariporo':{'Hato Corozal':34,'Pore':20},
        'Pitalito':{'Puerto Rico': 99,'Garzón':60},
        'Pore':{'Paz de Ariporo':20,'Yopal':62},
        'Puerto Rico':{'Pitalito':99,'Garzón':61},        
        'Rivera':{'Campoalegre':13,'Palermo':23},
        'Salamina':{'Marmato':15,'Bogotá':175},
        'San Martin':{'Acacías':33,'Vistahermosa':63},
        'Sopo':{'Chía':14,'Chocontá':38},
        'Tauramena':{'Acacías':142,'Yopal':84},
        'Ubaté':{'Chocontá': 26,'Hato Corozal':246},
        'Villeta':{'Aguadas':128,'Chía':49,'La Dorada':55},
        'Vistahermosa':{'San Martin':63,'Aipe': 172},
        'Yopal':{'Pore':62,'Tauramena':84}
    }
    return graph

def getPosition():    
    position={
        'Bogotá':0,
        'Acacías':270,
        'Aguadas':100,
        'Aipe':170,
        'Campoalegre':130,
        'Chía':40,
        'Chocontá':110,        
        'Garzón':200,
        'Gigante':160,
        'Hato Corozal':180,
        'Ibague':20,
        'La Calera':10,
        'La Dorada':120,
        'Manizales':190,
        'Marmato':60,
        'Neira':150,
        'Palermo':50,
        'Paz de Ariporo':220,
        'Pitalito':230,
        'Pore':260,
        'Puerto Rico': 240,  
        'Rivera':90,
        'Salamina':30,
        'San Martin':250,
        'Sopo':70,
        'Tauramena':290,
        'Ubaté':140,
        'Villeta':80,
        'Vistahermosa':210,
        'Yopal':280
    }
    return position

def getData():
    data = {'municipio': ['Bogotá', 'Acacías', 'Aguadas', 'Aipe', 'Campoalegre', 
                          'Chía', 'Chocontá', 'Garzón', 'Gigante', 'Hato Corozal', 
                          'Ibague', 'La Calera', 'La Dorada', 'Manizales', 'Marmato', 
                          'Neira', 'Palermo', 'Paz de Ariporo', 'Pitalito', 'Pore', 
                          'Puerto Rico', 'Rivera', 'Salamina', 'San Martin', 'Sopo', 
                          'Tauramena', 'Ubaté', 'Villeta', 'Vistahermosa', 'Yopal'],
        'latitud': [4.602063, 3.98695, 5.61161,3.22222,2.68489,
                    4.85876,5.14468,2.19593,2.38677,6.033591,
                    4.441879, 4.819197, 5.44783,5.06889,5.474703,
                    5.1665000,2.8916700,5.88111,1.85371,5.726564,
                    1.909939, 2.77717,5.40806,3.698531,4.90806,
                    5.01667,5.3093300,5.01278,2.7694498, 5.33775],
        'longitud': [-74.102579, -73.75797, -75.45624,-75.23667,-75.32311,
                     -74.05866,-73.68578,-75.62777,-75.54531,-71.603512,
                     -75.236949,-73.969131,-74.66311,-75.51738,-75.601047,
                      -75.5200100, -75.4375000,-71.8917,-76.05071,-71.993942,
                      -75.157217,-75.25642, -75.4878,-73.697350, -73.9403,
                      -72.75,-73.8157500,-74.4731,-73.6917796804736,-72.39586]}
    df=pd.DataFrame(data)
    return df
        