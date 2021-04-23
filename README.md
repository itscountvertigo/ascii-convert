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

- Run the file
- Paste/type in a file location
- Give it new smaller dimensions (remember to keep the correct aspect ratio). Somewhere around 50x50 should be fine for a square image.
- Tell it whether or not you want the colors to be flipped (with 'y' or 'n'). If you don't know, just try both out!

Now look in the newly created output folder, it should be in a text file named after the original file.

## How to install

All you'll need is to have Python 3 and the PIL library installed with ```pip install PIL```. 
