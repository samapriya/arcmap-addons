import arcpy, os  
arcpy.env.overwriteOutput = True
in_raster = arcpy.GetParameterAsText(0)
if in_raster == '#' or not in_raster:
    in_raster="C:\\Users\\samapriya\\Downloads\\Multiband\multiband.tif"

out_folder = arcpy.GetParameterAsText(1)
if out_folder == '#' or not out_folder:
    out_folder="C:\\Users\\samapriya\\Downloads\\Multiband"

desc = arcpy.Describe(in_raster)  
  
for band in desc.children:  
    bandName = band.name  
    band_path = os.path.join(in_raster, bandName)  
    dest_path = os.path.join(out_folder, bandName + '.tif')  
    arcpy.CopyRaster_management(band_path, dest_path, "", "", "", "NONE", "NONE", "") # change parameters her
