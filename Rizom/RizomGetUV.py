import coat
import os
from pathlib import Path

# Limpiar la consola para diagnóstico
# coat.io.showPythonConsole()

# 1. CONFIGURACIÓN DE RUTAS
base_path = Path(str(coat.io.documents(""))).resolve()
obj_import_path = base_path / "UserPrefs" / "Addons" / "csan_rizom" / "Rizom" / "toRizomUV.obj"

print("--- ACTUALIZANDO MALLA Y UV DESDE RIZOM (PAINT/UV ROOM) ---")

def dialog_callback():
    """Confirma los diálogos de importación automáticamente"""
    print("Confirmando diálogo de 3DCoat...")
    coat.ui.cmd("$DialogButton#1")

try:
    if obj_import_path.exists():
        # Aseguramos que estamos en la sala de UV
        coat.ui.toRoom("UV")

        # 2. REEMPLAZAR GEOMETRÍA
        # Esto actualiza la malla base antes de importar los UVs
        coat.ui.setFileForFileDialog(str(obj_import_path))
        print("Ejecutando: $ReplaceGeometry")
        coat.ui.cmd("$ReplaceGeometry", dialog_callback)
        
        # Pausa breve para procesar la geometría
        coat.io.step(10)

        # 3. IMPORTAR UV
        # Aplicamos el nuevo comando para importar las coordenadas UV de Rizom
        coat.ui.setFileForFileDialog(str(obj_import_path))
        print("Ejecutando: $IMPORTUV")
        coat.ui.cmd("$IMPORTUV", dialog_callback)

        # 4. FINALIZACIÓN Y SINCRONIZACIÓN
        coat.io.step(10)
        print("Sincronizando coordenadas UV finales...")
        coat.ui.cmd("$RestoreUV")
        
        print("✅ PROCESO COMPLETADO: Malla y UVs actualizados.")
        coat.ui.showInfoMessage("UVs actualizados desde Rizom", 3000)
        
    else:
        print(f"❌ Error: No se encontró el archivo en {obj_import_path}")

except Exception as e:
    print(f"❌ Error en el script: {e}")

print("-----------------------------------------")