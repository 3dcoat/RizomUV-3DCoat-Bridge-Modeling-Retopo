import coat
import os
import subprocess
from pathlib import Path

# Limpiar la consola para ver errores nuevos
# coat.io.showPythonConsole()

# 1. CONFIGURACIÓN DE RUTAS
base_path = Path(str(coat.io.documents(""))).resolve()
addon_path = base_path / "UserPrefs" / "Addons" / "csan_rizom" / "Rizom"
obj_export_path = addon_path / "toRizomUV.obj"

# RUTA DEL EJECUTABLE DE RIZOM
rizom_exe = "C:/Program Files/Rizom Lab/RizomUV 2025.0/rizomuv.exe"
# rizom_exe = "C:/Program Files/Rizom Lab/Unfold3D VS 2018.0/unfold3d.exe"

print("--- STARTING EXPORT (PAINT/UV ROOM) ---")

def export_callback():
    """Esta función rellena automáticamente el diálogo de exportación UV"""
    print("Configuring UV export dialog...")
    # Seteamos la ruta del archivo OBJ
    coat.ui.setEditBoxValue("$ExportOpt::PathForGeometry", str(obj_export_path))
    # Presionamos el botón 'OK'
    coat.ui.cmd("$DialogButton#1")

try:
    # 2. DETECCIÓN DE SALA Y SELECCIÓN
    room = str(coat.ui.currentRoom())
    print(f"Detected Room: {room}")

    # Aseguramos la selección total en la sala de Paint/UV
    print("Selecting all sub-objects...")
    coat.ui.cmd("$SelectAll")
    
    # 3. PREPARAR EL SISTEMA DE ARCHIVOS
    coat.ui.setFileForFileDialog(str(obj_export_path))
    
    # 4. EJECUTAR COMANDOS DE EXPORTACIÓN
    # Aplicar cambios de UV pendientes 
    print("Applying UVs...")
    coat.ui.cmd("$ApplyUV")
    
    # Ejecutar el comando específico de exportación UV 
    print(f"Launching command: $EXPORTUV")
    coat.ui.cmd("$EXPORTUV", export_callback)
    
    # Pausa de seguridad para la escritura del archivo
    coat.io.step(15)

    # 5. VERIFICACIÓN Y APERTURA DE RIZOM
    if obj_export_path.exists():
        size = obj_export_path.stat().st_size
        if size > 1500: 
            print(f"✅ File generated successfully: {size} bytes")
            
            if os.path.exists(rizom_exe):
                print(f"🚀 Opening RizomUV...")
                subprocess.Popen([rizom_exe, str(obj_export_path)])
                coat.ui.showInfoMessage("Sent to Rizom!", 3000)
            else:
                print(f"❌ Error: Rizom app not found at {rizom_exe}")
        else:
            print(f"❌ Error: File is too small ({size} bytes).")
            print("Ensure the object is visible and selected in the Paint/UV room.")
    else:
        print("❌ Error: toRizomUV.obj file was not created.")

except Exception as e:
    print(f"❌ Critical script failure: {e}")

print("-----------------------------------------------")