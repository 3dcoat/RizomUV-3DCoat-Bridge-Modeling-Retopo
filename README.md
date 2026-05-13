Important note for RizomUV:

Make sure the path in the Python script points to the .exe file you actually have installed (RizomUV or Unfold3D). This version is ready for RizomUV 2025.
In the folder /Addons/csan_rizom/Rizom/ there is 2 files: RizomSendRM.py and RizomSendUV.py. You must comment out the unfold3D.exe version and enable the rizomuv.exe version.
This addon installation is currently set to work witch RizomUV 2025.

If you need to change the version to another one or olders, check the rizom_exe executable line on line 14, select your version and comment the other (using "#"):: 
# your rizomuv installation folder
rizom_exe = "C:/Program Files/Rizom Lab/RizomUV 2025.0/rizomuv.exe" 

# your unfold3D installation folder
rizom_exe = r"C:/Program Files/Rizom Lab/Unfold3D VS 2018.0/unfold3d.exe"


Install: 
Drag the .3dcpack into 3DCoat 
or AddOns → Install Extension
or "File > Install > Install Extension"
then restart 3DC
After the install, you can find it in the Addon Menu.


There are 4 scripts. Send and get for Retopo/Modeling Room and for Paint/UV Room:
RizomSendRM.py and RizomSendUV.py: Exports the mesh, saves it to a fixed path, and automatically launches RizomUV. On Retopo/Modeling Room make sure the mesh you wish to send is selected.
RizomGetRM.py and RizomGetUV.py: Deletes the old mesh to avoid creating garbage, creates a new one, imports the processed model, and restores the UVs.

The bridge file (toRizomUV.obj and toRizomRM.obj) will be created in the folder \UserPrefs\Addons\csan_rizom\Rizom


The Paint/UV addon does not reproject textures after to get the mesh back with the new UV. 
If you see some transparencies in the mesh shader on Paint Room, select the Layer0 > Pick (C) the grey color and fill all the mesh/layer with that grey color.
