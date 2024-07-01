# Material-QSS
Material style QSS stylesheets for Qt C++ <br>
<br>
All StyleSheet is from qt-material python lib, the export function it provided is not suitable for Qt C++ project.  <br>
so I rewrite it in qss.py and the StyleSheet exported is in the ```qss``` folder.

## step1
Find theme you need in the ```qss``` fold, place theme folder(e.g. light_red) in the Qt project directory. <br>
each theme folder include a .qss file, a .qrc file and a image folder. 

## step2
Modify your Qt .pro file to append resource info, like this:
```
RESOURCES += \
    light_red/resources.qrc
```

## step3
Set stylesheet for your QApplication in main.cpp, like this:
```c++
int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    QFile qssFile(":file/light_red.qss");
    if(qssFile.open(QFile::ReadOnly))
        a.setStyleSheet(qssFile.readAll());
    qssFile.close();

    Widget w;
    w.show();
    return a.exec();
}
```

## step4
rebuild and run your project. <br>
if it's not material style, clean your project and rebuild it again.
