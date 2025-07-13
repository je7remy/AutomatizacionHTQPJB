import pandas as pd

# --------------------------------------
# 1. Definir rutas de archivos
# --------------------------------------
excel_path = "PLANTILLA INVENTARIO JUNIO 2025 Original.xlsx"
csv_path   = "PRODUCTOS DE INSUMO MEDICO.csv"
output_path = "PRODUCTOS_ACTUALIZADOS.csv"

# --------------------------------------
# 2. Cargar Excel (cabecera real en fila 4 -> header=3)
# --------------------------------------
df_excel = pd.read_excel(excel_path, header=3)

# Limpiar espacios en los nombres de columna
df_excel.columns = df_excel.columns.str.strip()

# --------------------------------------
# 3. Extraer columnas requeridas y renombrar
# --------------------------------------
df_inventario = df_excel[["DESCRIPCION ARTICULO", "COSTO UNITARIO EN RDS"]].copy()
df_inventario.columns = ["name", "list_price"]

# --------------------------------------
# 4. Cargar CSV de destino
# --------------------------------------
df_csv = pd.read_csv(csv_path)

# --------------------------------------
# 5. Reemplazar columnas en el CSV
# --------------------------------------
df_csv["name"] = df_inventario["name"]
df_csv["list_price"] = df_inventario["list_price"]

# --------------------------------------
# 6. Guardar resultado final
# --------------------------------------
df_csv.to_csv(output_path, index=False)
print(f"✅ Archivo actualizado guardado como '{output_path}'")
