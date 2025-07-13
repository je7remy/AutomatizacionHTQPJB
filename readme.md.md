
# 🛠️ Actualizador de Productos desde Inventario

Este script en Python toma un archivo de inventario en formato Excel y actualiza las columnas `name` y `list_price` de un archivo CSV de productos médicos.

---

## 📁 Archivos requeridos

- `PLANTILLA INVENTARIO JUNIO 2025 Original.xlsx`: Archivo Excel que contiene los nombres y precios actualizados.
- `PRODUCTOS DE INSUMO MEDICO.csv`: Archivo CSV con la estructura esperada, donde se actualizarán las columnas `name` y `list_price`.

---

## 📦 Requisitos

Asegúrate de tener Python instalado y los siguientes paquetes:

```bash
pip install pandas openpyxl
````

---

## ▶️ Uso

1. Coloca ambos archivos en el mismo directorio que el script.
    
2. Ejecuta el script:
    

```bash
python actualizar_productos.py
```

3. El archivo actualizado se guardará como:
    

```
PRODUCTOS_ACTUALIZADOS.csv
```

---

## 🔄 ¿Qué hace el script?

- Lee el archivo Excel (a partir de la fila 4).
    
- Extrae la descripción del artículo y el costo unitario.
    
- Sobrescribe las columnas `name` y `list_price` del archivo CSV.
    
- Guarda el archivo actualizado.
    

---

## 📌 Notas

- Asegúrate de que el archivo Excel tenga los encabezados correctos:
    
    - `DESCRIPCION ARTICULO`
        
    - `COSTO UNITARIO EN RDS`
        
- El número de filas en ambos archivos debe coincidir para evitar desalineación.
    

---

## 👨‍💻 Autor

Jeremy José de la Cruz Pérez  
Soporte Técnico – Hospital Regional Traumatológico Prof. Juan Bosch
