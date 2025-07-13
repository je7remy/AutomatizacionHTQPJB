import pandas as pd

# --------------------------------------
# 0. Instalar dependencias
# pip install openpyxl
# --------------------------------------

# --------------------------------------
# 1. Cargar archivos de origen
# --------------------------------------
csv_path   = "insumos medicos.csv"
excel_path = "PLANTILLA INVENTARIO JUNIO 2025.xlsx"

df_csv   = pd.read_csv(csv_path)
# Le indicamos que la fila de índice 2 (tercera fila) es el header real
df_excel = pd.read_excel(excel_path, header=2)

# --------------------------------------
# 2. Normalizar nombres para comparar
# --------------------------------------
# Quitar espacios y pasar a mayúsculas en ambos DataFrames
df_csv["Nombre_normalizado"]       = df_csv["Nombre"].str.strip().str.upper()
df_excel["Nombre_normalizado"]    = df_excel["DESCRIPCION ARTICULO"].str.strip().str.upper()

# --------------------------------------
# 3. Renombrar la columna de precio del Excel
# --------------------------------------
df_excel = df_excel.rename(columns={
    "COSTO UNITARIO EN RDS": "Precio de costo nuevo"
})

# --------------------------------------
# 4. Hacer el merge y actualizar sólo los precios coincidentes
# --------------------------------------
df_merged = pd.merge(
    df_csv,
    df_excel[["Nombre_normalizado", "Precio de costo nuevo"]],
    on="Nombre_normalizado",
    how="left"
)

# Si existe un nuevo precio, lo usamos; si no, mantenemos el original
df_merged["Precio de costo"] = (
    df_merged["Precio de costo nuevo"]
      .combine_first(df_merged["Precio de costo"])
)

# --------------------------------------
# 5. Limpiar sólo las columnas auxiliares
# --------------------------------------
# Eliminamos únicamente las columnas de normalización y del precio intermedio
df_merged = df_merged.drop(columns=["Nombre_normalizado", "Precio de costo nuevo"])

# --------------------------------------
# 6. Guardar resultado final
# --------------------------------------
df_merged.to_csv("insumos_actualizados.csv", index=False)
print("✅ Archivo actualizado guardado como 'insumos_actualizados.csv'")
