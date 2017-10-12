import arcpy,os
source = arcpy.GetParameterAsText(0)
destination=arcpy.GetParameterAsText(1)
fmt=arcpy.GetParameterAsText(2)
# Set the current workspace
arcpy.env.workspace = source

# Get and print a list of GRIDs from the workspace
rasters = arcpy.ListRasters("*", fmt)
for raster in rasters:
    filename=raster
    arcpy.AddMessage("Processing "+str(filename))
    arcpy.RasterToPoint_conversion(os.path.join(source,filename),os.path.join(destination,filename.replace(fmt,'.shp')))
    arcpy.AddMessage("Created new point shapefile")
