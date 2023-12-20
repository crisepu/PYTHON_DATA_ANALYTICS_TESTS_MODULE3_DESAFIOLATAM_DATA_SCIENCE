import pandas as pd

def dataframe_filtrado_fecha(df, columna, fecha_inicio, fecha_fin):
    df[columna] = pd.to_datetime(df[columna])
    df_filtrado = df[(df[columna] >= fecha_inicio) & (df[columna] <= fecha_fin)]
    return df_filtrado

def reporte_pivot(df, index, aggfunc):
    
    df_reporte = pd.pivot_table(
                            data = df,
                            index = index,
                            values = ['venta', 'costo', 'ganancia'],
                            aggfunc = aggfunc,
                            fill_value = 0,
                            margins = False
    )

    df_reporte = df_reporte.sort_values(by = 'venta', ascending = False)
    
    return df_reporte.head(10)

def save_database(df, name_table, engine, if_table_exists):
    df.to_sql(name = name_table, con = engine, if_exists = if_table_exists)
    return 'Table correctly stored in database.'