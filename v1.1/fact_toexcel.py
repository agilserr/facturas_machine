# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 09:56:33 2019

@author: aagils
"""

import pandas as pd
import string
from tabula import wrapper
import time

class PDF:
    
    def dataframe1(self):
        print("Leyendo datos basicos")
        
        df = wrapper.read_pdf('30708741163-201-00008-00000007.pdf',
                      multiple_tables=True, pages="all")
        return df[0]
    
    def dataframe2(self):
        print("Leyendo impuestos")
        
        df = wrapper.read_pdf('30708741163-201-00008-00000007.pdf',
                      multiple_tables=True, pages="all")
        return df[1]

class Del:
    
    def __init__(self, keep=string.digits):
        self.comp = dict((ord(c),c) for c in keep)
        
    def __getitem__(self, k):
        return self.comp.get(k)
    
    def cat_iva(str):
        if 'Responsable Inscripto' in str:
            return 'RI'
        elif 'Extento' in str:
            return 'EX'
        else:
            return 'CF'

class basic_data:
        
    def fecha_emi(self,df):
        return df.iloc[4,2].split(':')[1]
    
    def t_comp(self,df):
        return df1.iloc[0,2][0]
       
    def n_comp(self,df):
        DD = Del()
        pto_venta = df.iloc[3,2].translate(DD)
        aux = df1.iloc[0,2][0]
        n_comp = aux+ pto_venta
        return n_comp
            
    def razon_social(self,df):
        razon = df.iloc[10,2]
        return razon.split(':')[1]
    
    def cant_iva(self,df):
        return  Del.cat_iva(df.iloc[11,1])
    
    def identiftri(self,df):
        DD = Del()
        iden = df.iloc[10,0].translate(DD)
        return iden[0:2]+'-'+iden[3:len(iden)-1]+'-'+iden.strip()[-1]
    
class impuestos:
    
    def imp_extento(self):
        return 0
    
    def iva_func(self,df):
        imps = []
        iva_27 = df.iloc[3,2].translate(df)
        iva_21 = df.iloc[5,2].translate(df)
        amount_iva_27 = float(df.iloc[3,3].replace(',', '.'))
        amount_iva_21 = float(df.iloc[5,3].replace(',', '.'))
        if amount_iva_27 > 0:
            imps.append(iva_27)
            imps.append(amount_iva_27)
            return imps 
        else:
            imps.append(iva_21)
            imps.append(amount_iva_21)
            return imps 
    
    def porc_iva(self,df):
        DD = Del()
        porc_iva = impuestos().iva_func(df)
        return porc_iva[0].translate(DD)
    
    def iva(self, df):
        return impuestos().iva_func(df)[1]
    
    def imp_gravad(self,df):
        return df.iloc[2,3]
    
    def importe(self,df):
        return df.iloc[13,3]
    
    def sobre_iva(self):
        return 0
    
    def sub_iva(self):
        return 0
    
    def imp_int(self):
        return 0
    
    def ing_bru(self):
        return 0
    
    def otr_imp(self):
        return 0 
    
    def imp_rni(self):
        return 0
    
    def iva_lib(self):
        return 0
    
if __name__ == "__main__":
    
    print("Ejecutando el programa")
    time.sleep(1)
    print("Buscando Facturas")
    time.sleep(1)
    
    GetData = PDF()
    df1 = GetData.dataframe1()
    df2 = GetData.dataframe2()
    datos_basicos = basic_data()
    bottom_fact = impuestos()
    print("preparando la estructura de datos para exportar")
    factura = {"fecha_emi": datos_basicos.fecha_emi(df1),
       "t_comp": datos_basicos.t_comp(df1),
       "n_comp": datos_basicos.n_comp(df1),
       "n_comp_has": datos_basicos.n_comp(df1),
       "razon_soc":datos_basicos.razon_social(df1),
       "cat_iva": datos_basicos.cant_iva(df1),
       "identiftri": datos_basicos.identiftri(df1),
       "n_ing_bru": bottom_fact.ing_bru(),
       "imp_extento": bottom_fact.imp_extento(),
       "imp_gravad": bottom_fact.imp_gravad(df2),
       "porc_iva": bottom_fact.porc_iva(df2),
       "iva": bottom_fact.iva(df2),
       "sobre_iva": bottom_fact.sobre_iva(),
       "sub_iba": bottom_fact.sub_iva(),
       "imp_int": bottom_fact.imp_int(),
       "ing_bru": bottom_fact.ing_bru(),
       "otr_imp": bottom_fact.otr_imp(),
       "imp_rni": bottom_fact.imp_rni(),
       "iva_lib": bottom_fact.iva_lib(),
       "importe": bottom_fact.importe(df2)}
    time.sleep(2)
    fact_pd = pd.DataFrame.from_dict(factura,orient = 'index')
    fact_pd_t = fact_pd.T
    print("Exportando factura")
    fact_pd_t.to_excel("Factura_1.xlsx")
    time.sleep(2)
    print("Factura exportada con exito")
    

    
    
    
    