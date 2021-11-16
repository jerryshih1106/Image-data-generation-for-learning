# my_img_label_tool

## Rembg

[Rembg Danielgatis github](https://github.com/danielgatis/rembg)

### Requirements <h3> 
- python 3.8 or newer

```
pip install torch==1.7.1+cpu torchvision==0.8.2+cpu -f https://download.pytorch.org/whl/torch_stable.html
  
pip install rembg
```
  
## File
  ```
  ___  background    (put background image)
   |_  object        (put object image)    
   |_  label.txt     (labels index)
   |_  data  ___ img (merge data)                                      
              |_ txt (merge data's label, bbox(xmin, ymin, xmax, ymax))
  ```
 
