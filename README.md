# ArcMap Addons

[![DOI](https://zenodo.org/badge/90535170.svg)](https://zenodo.org/badge/latestdoi/90535170)

While working on different projects over sometime I had to create and use some tools which acted as valuable addons to arcmap toolbox. I am sharing a few and I will keep on updating these as I keep working on new models.This toolbox was created on ArcMap 10.4 and is not backward compatible. The toolbox can be downloaded and added to existing toolbox to create additional functionalities.

![GUI](http://i.imgur.com/F4kSftD.gif)
## Table of contents
* [Installation](#installation)
* [Usage examples](#usage-examples)
	* [Email Notification](#email-notification)
    * [Iterative Clip](#iterative-clip)
    * [MultiBand to Single Images](#multiband-to-single-images)
    * [Raster Properties as CSV](#raster-properties-to-csv)
    * [Raster Copy Iterative](#raster-copy-iterative)
	* [Feature Select and Copy](#feature-select-and-copy)
	* [Select and Calculate Field](#select-and-calculate-field)
* [Credits](#credits)

## Installation
We assume that the user already has a copy of ArcMap >=10.4. The toolbox can be downloaded along with adjoining script and added onto existing toolbox. You can keep this toolbox as part of the default toolboxes by clicking Save Settings>Save as Default

## Usage examples
Usage examples will vary and only continue to grow as new tools are added to the toolbox. 

### Email Notification
I found this to be one of the most useful tools when running a long process and not having to wait for your results. The tool makes use of the smtp library and allows the user to set up an email service for an email to be sent out after a process has been completed. 

![Email](http://i.imgur.com/Uj9m6II.gif)

### Iterative Clip
This tool does exactl what the name suggests it uses an iterator tool to clip a raster to different boundaries using shapefiles. Requires a single raster file and a folder with multiple polygons for clips.

![iterativeclip](http://i.imgur.com/na4VlTf.gif)

If using on a private machine the Key is saved as a csv file for all future runs of the tool.
 
### MultiBand to Single Images
The aoijson tab within the toolset allows you to create filters and structure your existing input file to that which can be used with Planet's API. The tool requires inputs with start and end date, along with cloud cover. You can choose from multiple input files types such as KML, Zipped Shapefile, GeoJSON, WKT or even Landsat Tiles based on PathRow numbers. The geo option asks you to select existing files which will be converted into formatted JSON file called aoi.json. If using WRS as an option just type in the 6 digit PathRow combination and it will create a json file for you.

![mbim](http://i.imgur.com/RIE2Obt.gif)

### Raster Properties as CSV
The activatepl tab allows the users to either check or activate planet assets, in this case only PSOrthoTile and REOrthoTile are supported because I was only interested in these two asset types for my work but can be easily extended to other asset types. This tool makes use of an existing json file sturctured for use within Planet API or the aoi.json file created earlier

![rasterprop](http://i.imgur.com/Ogs4xNU.gif)

### Raster Copy Iterative
Having metadata helps in organising your asstets, but is not mandatory - you can skip it.
The downloadpl tab allows the users to download assets. The platform can download Asset or Asset_XML which is the metadata file to desired folders.One again I was only interested in these two asset types(PSOrthoTile and REOrthoTile) for my work but can be easily extended to other asset types.

![rastercpy](http://i.imgur.com/8m1tkfr.gif)

### Feature Select and Copy
These tools allow the users to iteratively select features using a given SQL expression and then extract that as a new feature class. This can be done iteratively for all feature classes in the folder.

![Ftselect](http://i.imgur.com/vIxUSbv.png)

### Select and Calculate Field
This tool allows you to select a field and then recalculate or calculate it based on expressions. The user has the option of simply filling empty fields based on selection of a different field. Meaning I can calculate a field B based on a selection of a seperate field A if I want.

![Ftcalc](http://i.imgur.com/BjW5zJC.png)

# Credits
I would like to thank all those who bring me interesting problems to solve, there is little that is needed to keep one inspired.
