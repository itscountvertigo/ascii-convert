# ASCII Art Converter

Takes an image and converts it to ASCII art.

## Example (might not work on mobile):
```
                            {W@@@@@@@@@@@b<
                     ]@@@@@@@@@@@@@@@@@@@@@@@@@@c
                 0@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@X
              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@O
           >@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
         }@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      o@@@@@@@@@@;\@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@n+@@@@@@@@@@c
     @@@@@@@@@@@       ;@@@@@@@@@@@@@@@@@@@@@@{       @@@@@@@@@@@
    @@@@@@@@@@@@                                      M@@@@@@@@@@@
   @@@@@@@@@@@@@                                      h@@@@@@@@@@@@
  *@@@@@@@@@@@@@                                      @@@@@@@@@@@@@@
  @@@@@@@@@@@@@#                                      O@@@@@@@@@@@@@|
 @@@@@@@@@@@@@.                                         @@@@@@@@@@@@@
 @@@@@@@@@@@@c                                          }@@@@@@@@@@@@f
@@@@@@@@@@@@@                                            @@@@@@@@@@@@@
@@@@@@@@@@@@@                                            @@@@@@@@@@@@@
@@@@@@@@@@@@@                                            @@@@@@@@@@@@@
@@@@@@@@@@@@@                                            @@@@@@@@@@@@@
@@@@@@@@@@@@@                                            @@@@@@@@@@@@@
@@@@@@@@@@@@@@                                          @@@@@@@@@@@@@o
^@@@@@@@@@@@@@@                                        W@@@@@@@@@@@@@
 @@@@@@@@@@@@@@@                                      @@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@                                  @@@@@@@@@@@@@@@@
  !@@@@@@@@8@@@@@@@@@1                          -@@@@@@@@@@@@@@@@@@
   -@@@@@@d    @@@@@@@@@@@@@              @@@@@@@@@@@@@@@@@@@@@@@@,
     @@@@@@@@   n@@@@@@@@@@;               @@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@    #@@@@@@@L                v@@@@@@@@@@@@@@@@@@@@
       [@@@@@@@    {_ @  0                  @@@@@@@@@@@@@@@@@@Q
         8@@@@@@@                           @@@@@@@@@@@@@@@@@
           8@@@@@@@@@@@@@@                  @@@@@@@@@@@@@@@
             |@@@@@@@@@@@@>                 @@@@@@@@@@@@Y
                h@@@@@@@@@!                 @@@@@@@@@k
                    @@@@@@^                 @@@@@@                
```
## How to use

To use this, all you have to do is run the file with the arguments you want. To run it, use the following flags:

```python ascii_convert.py -i "FILE_PATH" -x X_SIZE -y Y_SIZE [-c CONTRAST] [-f]```

or their longer forms 

```python ascii_convert.py --input "FILE_PATH" --resize_x X_SIZE --resize_y Y_SIZE [--contrast CONTRAST] [--flipped]```

Flags between [brackets] are optional. If you can't figure something out, run the file with only the ```-h``` or ```--help``` flag.

## How to install

All you'll need is to have Python 3 and the PIL library installed with ```pip install PIL```. 

## Sources

I've taken the long character set from http://paulbourke.net/dataformats/asciiart/
