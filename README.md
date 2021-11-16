# Image Data(with bounding box) Generate For Learning

## Rembg

[Rembg Danielgatis github](https://github.com/danielgatis/rembg)

### Requirements <h3> 
- python 3.8 or newer

### Install Rembg <h3> 
```
pip install torch==1.7.1+cpu torchvision==0.8.2+cpu -f https://download.pytorch.org/whl/torch_stable.html
  
pip install rembg
```
## Eg
  
Background img:
  ![pngtree-qing-plaid-dining-table-banner-background-design-picture-image_911656](https://user-images.githubusercontent.com/66662065/141941659-208d48df-f6d8-4bb2-95de-c97acbc46e5e.jpg)
  
Object img:
  ![15154889601_new](https://user-images.githubusercontent.com/66662065/141941752-efd114b9-d747-4627-804b-98ce9cc304ba.jpg)

Merge img:
  ![0_7](https://user-images.githubusercontent.com/66662065/141941624-caa9b983-7f4a-45b3-9a1d-b386fb5be295.png)

Merge txt:
  0 95.0 220.0 349.0 438.0 
  
## File
  ```
  ___  background    (put background image)
   |_  object        (put object image)    
   |_  label.txt     (labels index)
   |_  data  ___ img (generate merge data)                                      
              |_ txt (generate merge data's label, bbox(xmin, ymin, xmax, ymax))
  ```
 
