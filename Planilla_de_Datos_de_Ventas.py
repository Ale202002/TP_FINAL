import pandas as pd 

Planilla_de_Datos_de_Ventas= {"Mes": ["Enero","Febrero","Marzo","Abril"],
              "Ventas": [30500,35600,28300,33900],
              "Gastos": [22000,23400,18100,20700]}

print(pd.DataFrame(Planilla_de_Datos_de_Ventas))
