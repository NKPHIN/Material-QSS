import PyQt5
import os
from qt_material import export_theme

dark = ['dark_amber', 'dark_teal', 'dark_yellow',
        'dark_blue', 'dark_pink', 'dark_lightgreen',
        'dark_red', 'dark_medical', 'dark_cyan',
        'dark_purple']

light = ['light_lightgreen', 'light_pink', 'light_blue',
         'light_purple', 'light_purple_500', 'light_cyan_500',
         'light_teal_500', 'light_red_500', 'light_teal',
         'light_orange', 'light_lightgreen_500', 'light_red',
         'light_cyan', 'light_yellow', 'light_pink_500',
         'light_blue_500', 'light_amber']

icon = ['tab_close.svg', 'leftarrow.svg', 'rightarrow.svg',
        'checkbox_indeterminate_invert.svg', 'branch-end.svg', 'vline.svg',
        'radiobutton_unchecked_invert.svg', 'float.svg', 'checkbox_unchecked.svg',
        'checklist_invert.svg', 'uparrow2.svg', 'splitter-vertical.svg',
        'branch-closed.svg', 'checklist_indeterminate_invert.svg', 'slider.svg',
        'sizegrip.svg', 'close.svg', 'checklist_indeterminate.svg',
        'checkbox_unchecked_invert.svg', 'downarrow.svg', 'branch-open.svg',
        'downarrow2.svg', 'branch-more.svg', 'checkbox_indeterminate.svg',
        'toolbar-handle-horizontal.svg', 'toolbar-handle-vertical.svg', 'leftarrow2.svg',
        'checklist.svg', 'base.svg', 'radiobutton_checked.svg',
        'rightarrow2.svg', 'uparrow.svg', 'checkbox_checked.svg',
        'radiobutton_unchecked.svg', 'splitter-horizontal.svg', 'checkbox_checked_invert.svg',
        'radiobutton_checked_invert.svg']

extra = {

    # Button colors
    'danger': '#dc3545',
    'warning': '#ffc107',
    'success': '#17a2b8',

    # Font
    'font_family': 'Klee',
    'font_size': '13px',
    'line_height': '13px',

    # Density Scale
    'density_scale': '0',

    # environ
    'pyside6': True,
    'linux': True,
}


def qrc(color):
    rcc = os.path.join(color, 'resources.qrc')
    with open(rcc, 'w+') as f:
        f.write('<RCC>\n')
        f.write('   <qresource prefix="icon">\n')

        for img in icon:
            url = os.path.join('theme', 'disabled', img)
            f.write('       <file>' + url + '</file>\n')

        for img in icon:
            url = os.path.join('theme', 'primary', img)
            f.write('       <file>' + url + '</file>\n')

        for img in icon:
            url = os.path.join('theme', 'active', img)
            f.write('       <file>' + url + '</file>\n')

        f.write('   </qresource>\n')
        f.write('   <qresource prefix="file">\n')
        url = os.path.join(color+'.qss')
        f.write('       <file>' + url + '</file>\n')
        f.write('   </qresource>\n')
        f.write('</RCC>')


def generate(color, invert):
    theme = color + '.xml'
    qss = os.path.join(color, color + '.qss')
    output = os.path.join(color, 'theme')

    # 自动生成的qrc文件有问题
    # 一是没有包括active的图片信息
    # 二是icon前缀有误
    #
    # 如果按照官网上的示例用 prefix = 'icon/'
    # 则 qss 文件提供的图片url无法访问
    # 因此采用了如下参数，并手动配置qrc文件
    # 具体见文档
    export_theme(theme=theme,
                 qss=qss,
                 output=output,
                 prefix=':icon/theme/',
                 invert_secondary=invert,           # 深色背景为False, 浅色背景为True
                 extra=extra,
                 )

    qrc(color)
    print(color + ' has convert to qss!')


if __name__ == '__main__':
    # generate(dark[0], False)

    for theme in dark:
        generate(theme, invert=False)

    for theme in light:
        generate(theme, invert=True)
