import arcpy,os
from os import path as p
source=arcpy.GetParameterAsText(0)
destination=arcpy.GetParameterAsText(1)
for filename in os.listdir(source):
    if filename.endswith('.dbf'):
        fc=os.path.join(source,filename)
        arcpy.AddMessage("Processing "+str(filename))
        CSVFile=os.path.join(destination,filename.replace(".dbf",".csv"))
        fields = [f.name for f in arcpy.ListFields(fc) if f.type <> 'Geometry']  
        with open(CSVFile, 'w') as f:  
            f.write(','.join(fields)+'\n') #csv headers  
            with arcpy.da.SearchCursor(fc, fields) as cursor:  
                for row in cursor:  
                    f.write(','.join([str(r) for r in row])+'\n')  
            arcpy.AddMessage('Created %s Successfully' %p.basename(CSVFile))
