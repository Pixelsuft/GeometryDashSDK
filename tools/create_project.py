import os
import sys
import ctypes
import shutil


def print_center(text: str) -> None:
    for line in text.split('\n'):
        if not line.strip():
            continue
        try:
            print(' ' * round(os.get_terminal_size()[0] / 2 - len(line) / 2), end='')
        except:
            pass
        print(line)


print_center('GeometryDashSDK by Pixelsuft')
print_center('Cocos-Headers and GD.h by HJfod')
print_center('CappuccinoSDK by AndreNIH')
print_center('MinHook by TsudaKageyu')
print_center('Thanks to Matcool, JaanDev')
print('\n\n')


is_win = 'windll' in dir(ctypes)
if not is_win:
    print('[Error]: This Script Can Be Runned Only Under Windows!')
    sys.exit(1)


os.chdir(os.path.join(os.path.dirname(__file__), '..'))


if len(sys.argv) <= 1:
    print('[Error]: No Project Name')
    print(f'[Info]: Example: "{sys.executable}" "{__file__}" "project_name"')
    sys.exit(1)


project_name = sys.argv[1]
clear_project_name = project_name.lower().strip()


'''if clear_project_name == 'tools' or clear_project_name == 'template':
    print(f'[Error]: Can\'t Use Project Name "{project_name}"')
    sys.exit(1)'''


if ' ' in project_name:
    print(f'[Error]: Project Name Can\'t Contain Spaces - Use "{project_name.replace(" ", "-")}" or "{project_name.replace(" ", "_")}"')
    sys.exit(1)


projects_dir = os.path.join(os.getcwd(), 'projects')


if not os.path.isdir(projects_dir):
    os.mkdir(projects_dir)


project_dir = os.path.join(projects_dir, project_name)


if os.path.isdir(project_dir):
    print(f'[Warning]: Project "{project_name}" Is Already Exists')
    while True:
        input_ = input('[Prompt]: Do You Want To Continue? [Y/n]').lower().strip()
        if input_ == 'y':
            break
        if input_ == 'n':
            sys.exit(0)
    shutil.rmtree(project_dir)


print('[Info]: Copying Template')
shutil.copytree(os.path.join(os.getcwd(), 'template'), project_dir)


print('[Info]: Editing "CMakeLists.txt"')


cmake_lists_path = os.path.join(project_dir, 'CMakeLists.txt')
f = open(cmake_lists_path, 'r')
cmake_lists = f.read()
f.close()


print('[Info]: Writing "CMakeLists.txt"')
f = open(cmake_lists_path, 'w')
f.write(cmake_lists.replace('%PROJECT_NAME%', project_name))
f.close()


print('[Info]: OK\n\n')
print_center('Happy Hacking!')
print_center('Good Luck & Have Fun!')

