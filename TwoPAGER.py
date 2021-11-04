from subprocess import call, check_output

import sys

try:

    if sys.version[0] == '2':
        try:
            print('Python 2 is default interpreter...going to try Python 3')
            py_check = check_output('where python').split('\r\n')
            py3_intepreter = ''.join([i for i in py_check if 'miniforge' in i])
            the_call = py3_intepreter + ' ' + sys.argv[0]
            call(the_call)
        except Exception as e:
            print(e)
            raw_input('Hit enter to continue...')

    else:
        from src.manage import Manage

        if __name__=='__main__':
            manage = Manage()
            app_path = './src/gui.py'
            try:
                manage.checkForUpdates()
                manage.startApp(app_path)
            except Exception as e:
                print(e)
except Exception as e:
    import ctypes
    print(e)
    input('Hit enter')
    messageBox = ctypes.windll.user32.MessageBoxW
    error = sys.exc_info()[0]
    messageBox(0, u"Unexpected error: {er} | If this problem persists, and you've ensured it's not user error, ask your developers to write better code.".format(
        er=error), u"HazPy", 0x1000)
