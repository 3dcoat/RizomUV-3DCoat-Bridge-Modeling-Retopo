import coat
import os
from pathlib import Path

# 1. PATH CONFIGURATION
# coat.io.showPythonConsole()
base_path = Path(str(coat.io.documents(""))).resolve()
obj_import_path = base_path / "UserPrefs" / "Addons" / "csan_rizom" / "Rizom" / "toRizomRM.obj"

print("--- REPLACING RETOPO/MODELING MESH WITH RIZOM VERSION ---")

def confirm_callback():
    """Confirms 'Accept' or 'Yes' dialogs"""
    print("Confirming action...")
    coat.ui.cmd("$DialogButton#1")

def import_callback():
    """Configures the import settings for the newly created layer"""
    print("Configuring import options...")
    coat.ui.setBoolValue("$ImportOpt::CreateNewObject", False)
    coat.ui.setBoolValue("$ImportOpt::SnapToSurface", False)
    coat.ui.cmd("$DialogButton#1")

try:
    if obj_import_path.exists():
        coat.ui.toRoom("Retopo")

        # 2. CLEANUP: Delete the current layer (the old one)
        print("Deleting original Polygroup layer to avoid overlap...")
        # Execute deletion with callback to accept the warning dialog
        coat.ui.cmd("$RetopoVisualTree::DELETE_LAYER_HINT", confirm_callback)
        
        # 3. PREPARATION: Create a new layer
        print("Creating clean Polygroup layer...")
        coat.ui.cmd("$RetopoVisualTree::ADD_NEW_LAYER_HINT")

        # 4. IMPORT
        coat.ui.setFileForFileDialog(str(obj_import_path))
        print(f"Loading: {obj_import_path.name}")
        coat.ui.cmd("$ImportRetopoMesh", import_callback)
        
        # Short pause to allow geometry to settle
        coat.io.step(10)
        
        # 5. FINALIZATION: Select and Restore UV
        coat.ui.cmd("$SelectAllRetopo")
        print("Synchronizing UV coordinates...")
        coat.ui.cmd("$[Page3]Restore UV")
        
        print("✅ PROCESS COMPLETED: Layer replaced successfully.")
        coat.ui.showInfoMessage("Mesh replaced from Rizom", 3000)
        
    else:
        print(f"❌ Error: File not found at {obj_import_path}")

except Exception as e:
    print(f"❌ Script error: {e}")

print("-----------------------------------------")