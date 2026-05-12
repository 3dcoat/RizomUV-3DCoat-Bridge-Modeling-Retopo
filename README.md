# RizomUV-3DCoat-Bridge-Modeling-Retopo
Bridge between RizomUV and 3DCoat for Retopo &amp; Modeling Rooms

Important note:

Make sure the path in the Python script points to the .exe file you actually have installed.
In your /addons/Rizom/RizomSend.py file, you must comment out the unfold3D.exe version and enable the rizomuv.exe version.

Check the rizom_exe executable line on line 14, select your version and comment the other (using "#"):: 
# your rizomuv installation folder
rizom_exe = "C:/Program Files/Rizom Lab/RizomUV 2025.0/rizomuv.exe" 

# your unfold3D installation folder
rizom_exe = r"C:/Program Files/Rizom Lab/Unfold3D VS 2018.0/unfold3d.exe"

The scripts:
RizomSend.py: Exports the Retopo/Modeling Polygroup selection, saves it to a fixed path, and automatically launches RizomUV. Make sure the mesh you wish to send is selected.
RizomGet.py: Deletes the old Polygroup layer to avoid creating garbage, creates a new one, imports the processed model, and restores the UVs.

-----------------
Nota importante: 

Asegúrate de que la ruta en el script de Python apunte al .exe que realmente tienes instalado.
En tu archivo /addons/Rizom/RizomSend.py debes comentar la versión unfold3D.exe y activar la versión rizomuv.exe

Revisa la línea del ejecutable de rizom_exe en la linea 14. Selecciona tu version
# el folder de instalacion de tu version de rizomuv
rizom_exe = "C:/Program Files/Rizom Lab/RizomUV 2025.0/rizomuv.exe" 

# el folder de instalacion de tu version de unfold3D
rizom_exe = r"C:/Program Files/Rizom Lab/Unfold3D VS 2018.0/unfold3d.exe"

Los scripts: 
RizomSend.py: Exporta la selección de Retopo, la guarda en una ruta fija y lanza RizomUV automáticamente. Asegurate que la malla que deseas enviar este seleccionada.
RizomGet.py: Borra la capa vieja para evitar basura, crea una nueva, importa el modelo procesado y restaura las UVs.
