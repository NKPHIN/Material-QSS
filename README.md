# MaterialQSS
Material style QSS stylesheets for Qt C++

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
