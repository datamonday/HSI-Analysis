# 打开 IDE，在Ipython中依次输入：
import spectral as hsi

rootdir = 'D:/Py Project/ML Course/03 FeatureSelection/spectral_data/'
img = hsi.open_image(rootdir + '92AV3C.lan')

print(img)

arr = img.load()
print(arr.__class__)

print(arr.info())

indian_view = hsi.imshow(img, (29, 19, 9))

print(indian_view)

gt = hsi.open_image(rootdir + '92AV3GT.GIS').read_band(0)
gt_view = hsi.imshow(classes=gt)

mask_view = hsi.imshow(img, (30, 20, 10), classes=gt)
mask_view.set_display_mode('overlay')
mask_view.class_alpha = 0.5  # 透明度

import spectral.io.aviris as aviris

img.bands = aviris.read_aviris_bands(rootdir + '92AV3C.spc')

hsi.imshow(img, (30, 20, 10))

import spectral

spectral.settings.WX_GL_DEPTH_SIZE = 16

hsi.view_cube(img, bands=[29, 19, 9])
