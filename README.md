# ASCII Art Converter

Takes an image and converts it to ASCII art.

## Example (might not work on mobile):
```
                           , ~ ; = ! ! ; : - .                        
                     , ; * @ @ @ @ @ @ @ @ @ # = -                    
                 - ! @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ ! ,                
             . = @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ ; .            
           , * @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ ! .          
         , # @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ * .        
       . # @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ * .      
       ! @ @ @ @ # * @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ # # @ @ @ @ =      
     ~ @ @ @ @ @ ,   , = @ @ @ @ $ $ $ @ @ @ @ = ,   , @ @ @ @ @ ~    
   . # @ @ @ @ $ .       , : - , . . . , - ~ ,       . # @ @ @ @ # .  
   ~ @ @ @ @ @ #                                       # @ @ @ @ @ :  
   * @ @ @ @ @ $ .                                   . $ @ @ @ @ @ * .
 , @ @ @ @ @ @ $ .                                   . # @ @ @ @ @ @ -
 : @ @ @ @ @ @ ~                                       ~ @ @ @ @ @ @ ;
 ! @ @ @ @ @ # .                                       . # @ @ @ @ @ *
 # @ @ @ @ @ =                                           ; @ @ @ @ @ $
 @ @ @ @ @ @ :                                           : @ @ @ @ @ @
 @ @ @ @ @ @ :                                           ~ @ @ @ @ @ @
 @ @ @ @ @ @ ;                                           : @ @ @ @ @ @
 @ @ @ @ @ @ !                                           = @ @ @ @ @ @
 $ @ @ @ @ @ # .                                       . # @ @ @ @ @ $
 * @ @ @ @ @ @ ~                                       - @ @ @ @ @ @ *
 ; @ @ @ @ @ @ # .                                   . * @ @ @ @ @ @ ;
 - @ @ @ @ @ @ @ ! .                               . ! @ @ @ @ @ @ @ ,
 . * @ @ @ # @ @ @ # ~ .                       . ~ # @ @ @ @ @ @ @ *  
   ~ @ @ $ - , * @ @ @ $ ! ; .           . ; ! $ @ @ @ @ @ @ @ @ @ ~  
   . * @ @ $ - . # @ @ @ @ # .           . * @ @ @ @ @ @ @ @ @ @ * .  
     - @ @ @ # . ~ $ @ @ @ :               ~ @ @ @ @ @ @ @ @ @ @ -    
       : @ @ @ : . - = ! : .               - @ @ @ @ @ @ @ @ @ ;      
         = @ @ $ -     . . .               , @ @ @ @ @ @ @ @ ! .      
         . = @ @ @ ! : : : .               , @ @ @ @ @ @ @ ! .        
             ; @ @ @ @ @ @ -               , @ @ @ @ @ @ = .          
               ~ $ @ @ @ @ -               , @ @ @ @ $ ~              
                 . ; $ @ @ -               , @ @ $ ; .                
                     . : = .               . = : .                    
```
## How to use

To use this, all you have to do is run the file with the arguments you want. To run it, use the following flags:

```python main.py -i "FILE_PATH" -x X_SIZE -y Y_SIZE [-c CONTRAST] [-f]```

or their longer forms 

```python main.py --input "FILE_PATH" --resize_x X_SIZE --resize_y Y_SIZE [--contrast CONTRAST] [--flipped]```

Flags between [brackets] are optional. If you can't figure something out, run the file with only the ```-h``` or ```--help``` flag.

## How to install

All you'll need is to have Python 3 and the PIL library installed with ```pip install PIL```. 