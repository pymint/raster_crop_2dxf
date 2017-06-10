Crops a georeferenced raster image (must have world coordinates file) with the coordinates from a dxf file that contains a rectangle. 
Creates world coordinates tfw file for the cropped raster.
Additionally, creates another dxf file that includes the cropped raster (georeferenced).

Python dependencies: dxfgrabber, ezdxf
External dependencies: gdal_translate and listgeo (must be included in path system variable)
