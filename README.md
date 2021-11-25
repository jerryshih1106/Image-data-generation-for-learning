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
  
  ![stock-photo-wood-dining-table-decor-wooden-wood-grain-wooden-background-round-table-wooden-texture-modern-furniture-19c7dd43-d199-4667-96bc-0b5bfd620025](https://user-images.githubusercontent.com/66662065/143493344-88b26c6c-4558-42a1-b644-34c37b90f364.jpg)

  
Object img:
  
  ![15154889601_new](https://user-images.githubusercontent.com/66662065/141941752-efd114b9-d747-4627-804b-98ce9cc304ba.jpg)

Merge img:
  
  ![0_0](https://user-images.githubusercontent.com/66662065/143493364-5e9eef30-de67-4df9-b582-ba6161df72d0.png)


Merge txt:
  
  0 105 165 279 403  
  
## File
  ```
  ___  background    (put background image)
   |_  object        (put object image)    
   |_  label.txt     (labels index)
   |_  data  ___ img (generate merge data)                                      
              |_ txt (generate merge data's label, bbox(xmin, ymin, xmax, ymax))
  ```
 
