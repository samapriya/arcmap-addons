import os
import arcpy
import csv
# Local variables:
in_folder = arcpy.GetParameterAsText(0)
out_csv=arcpy.GetParameterAsText(1)
fmt=arcpy.GetParameterAsText(2)
with open(out_csv,'wb') as completed:
    writer=csv.DictWriter(completed,fieldnames=["id_no","system:time_start","Sensor Name","Product Name","Acquisition Date","Cloud Cover","Sun Azimuth","Sun Elevation","Sensor Azimuth","Sensor Elevation","OffNadir"],delimiter=',')
    writer.writeheader()
for filename in os.listdir(in_folder):
    infilename = os.path.join(in_folder,filename)
    in_raster=infilename
    sysid=in_raster.strip(in_folder).strip('.'+fmt)
    p1= arcpy.GetRasterProperties_management(in_raster, "SENSORNAME", "")
    p2= arcpy.GetRasterProperties_management(in_raster, "PRODUCTNAME", "")
    p3= arcpy.GetRasterProperties_management(in_raster, "ACQUISITIONDATE", "")
    p4= arcpy.GetRasterProperties_management(in_raster, "CLOUDCOVER", "")
    p5 = arcpy.GetRasterProperties_management(in_raster, "SUNAZIMUTH", "")
    p6= arcpy.GetRasterProperties_management(in_raster, "SUNELEVATION", "")
    p7= arcpy.GetRasterProperties_management(in_raster, "SENSORAZIMUTH", "")
    p8= arcpy.GetRasterProperties_management(in_raster, "SENSORELEVATION", "")
    p9= arcpy.GetRasterProperties_management(in_raster, "OFFNADIR", "")
    date_time=str(p3).split(" ")[0]
    pattern = '%Y/%m/%d'
    epoch = int(time.mktime(time.strptime(date_time, pattern)))*1000
    with open(out_csv, 'a') as csvfile:
        writer=csv.writer(csvfile,delimiter=',',lineterminator='\n')
        writer.writerow([sysid,epoch,p1, p2, str(p3).split(" ")[0], p4, p5, p6, p7, p8, p9])
    csvfile.close()
