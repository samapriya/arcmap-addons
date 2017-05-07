import arcpy
import smtplib
arcpy.env.workspace="C:/EmailServer"

#Script arguments
fromemailid=arcpy.GetParameterAsText(0)
passwd=arcpy.GetParameterAsText(1)
toemailid=arcpy.GetParameterAsText(2)
Emailmsg = arcpy.GetParameterAsText(3)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromemailid, passwd)
server.sendmail(fromemailid, toemailid, Emailmsg)
server.quit()