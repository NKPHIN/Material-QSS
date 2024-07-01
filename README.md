# MaterialQSS
Material style QSS stylesheets for Qt C++ <br>
<br>
All StyleSheet is from qt-material python lib, the export function it provided is not suitable for Qt C++ project  <br>
so I rewrite it in qss.py and the StyleSheet exported is in the ```qss``` folder

## step1
find theme you need in the ```qss``` fold, place this folder in the Qt project directory

## step2
modify your Qt .pro file to append resource info, like this:
```
RESOURCES += \
    light_red/resources.qrc
```

## step3
rebuild and run your project
if it's not material style, clean your project and rebuild it again.
