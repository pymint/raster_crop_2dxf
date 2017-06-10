import dxfgrabber
from PIL import Image as img
import ezdxf
import os

areadxf = "myarea.dxf"
myraster = "myraster.tif" #can be any type supported by gdal
raster_cropped = "raster_cropped.tif"
dxf_output = "cropped_raster.dxf"

dxf = dxfgrabber.readfile(areadxf)

pl=dxf.entities[0].points

x = [ttt[0] for ttt in pl]
y = [tt[1] for tt in pl]
georef = '%f %f %f %f' %(min(x),max(y),max(x),min(y))

cmd = 'gdal_translate -projwin %s -of GTiff %s %s' %(georef,myraster,raster_cropped)
os.system(cmd)

os.system('listgeo -tfw %s'%raster_cropped)

f = open('raster_cropped.tfw', 'r')
wld = f.readlines()
wld = [x.strip() for x in wld]
wld = [float(l) for l in wld]
f.close()

im = img.open('raster_cropped.tif')

dwg = ezdxf.new('AC1015')

my_image_def = dwg.add_image_def(filename=raster_cropped, size_in_pixel=im.size)
msp = dwg.modelspace()

size = (float(im.size[0])/2, float(im.size[1])/2)

x1 = wld[0] * (-0.5) + wld[2] * size[1] + wld[4]
y1 = wld[1] * (-0.5) + wld[3] * (-0.5) + wld[5] - size[1]

msp.add_image(insert=(x1, y1), size_in_units=size, image_def=my_image_def, rotation=0)
image_defs = dwg.objects.query('IMAGEDEF')
dwg.saveas(dxf_output)
