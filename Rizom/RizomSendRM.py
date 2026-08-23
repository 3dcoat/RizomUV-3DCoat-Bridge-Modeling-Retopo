import coat
import os
import subprocess
from pathlib import Path

# Clear the console to see new errors
# coat.io.showPythonConsole()

# 1. PATH CONFIGURATION
base_path = Path(str(coat.io.documents(""))).resolve()
addon_path = base_path / "UserPrefs" / "Addons" / "csan_rizom" / "Rizom"
obj_export_path = addon_path / "toRizomRM.obj"

# RIZOM EXECUTABLE PATH (Verify this matches your PC)
rizom_exe = "C:/Program Files/Rizom Lab/RizomUV 2025.0/rizomuv.exe"
# rizom_exe = "C:/Program Files/Rizom Lab/Unfold3D VS 2018.0/unfold3d.exe"

print("--- STARTING EXPORT (RETOPO/MODELING) ---")

def export_callback():
    """This function auto-fills the 3DCoat export dialog"""
    print("Configuring export dialog automatically...")
    # Set the OBJ file path
    coat.ui.setEditBoxValue("$ExportOpt::PathForGeometry", str(obj_export_path))
    # Press the 'OK' button
    coat.ui.cmd("$DialogButton#1")

try:
    # 2. ROOM DETECTION AND SELECTION
    room = str(coat.ui.currentRoom())
    print(f"Detected Room: {room}")

    # Select the mesh to avoid a 1KB empty file
    if "Retopo" in room or "Modeling" in room:
        print("Selecting Polygroup Retopo mesh...")
        coat.ui.cmd("$SelectAllRetopo")
    else:
        print("Selecting everything...")
        coat.ui.cmd("$SelectAll")
    
    # 3. PREPARE FILE SYSTEM
    # Pre-configure the file name for the next dialog that opens
    coat.ui.setFileForFileDialog(str(obj_export_path))
    
    # 4. EXECUTE EXPORT COMMAND
    print(f"Launching command: $ExportSelected")
    coat.ui.cmd("$ExportSelected", export_callback)
    
    # Safety pause to allow 3DCoat to write the file to disk
    coat.io.step(15)

    # 5. VERIFICATION AND OPENING RIZOM
    if obj_export_path.exists():
        size = obj_export_path.stat().st_size
        if size > 1500: # If larger than 1.5KB, it contains geometry
            print(f"✅ File generated successfully: {size} bytes")
            
            if os.path.exists(rizom_exe):
                print(f"🚀 Opening RizomUV...")
                subprocess.Popen([rizom_exe, str(obj_export_path)])
                coat.ui.showInfoMessage("Sent to Rizom!", 3000)
            else:
                print(f"❌ Error: Rizom app not found at {rizom_exe}")
        else:
            print(f"❌ Error: File is too small ({size} bytes).")
            print("Make sure the mesh is visible and selected.")
    else:
        print("❌ Error: toRizomRM.obj file was not created.")

except Exception as e:
    print(f"❌ Critical script failure: {e}")

print("-----------------------------------------------")