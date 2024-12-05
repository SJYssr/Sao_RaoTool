from pykeyboard import PyKeyboard
import pyperclip
import time
import random
import linecache
import configparser
k = PyKeyboard()
#------------------------------------------------------------------
def read_config(file_path):
    config = configparser.ConfigParser()
    config.read(file_path, encoding='utf-8')
    one = config.get('TYPE','1')
    two = config.get('TYPE','2')
    three  = config.get('TYPE','3')
    four = config.get('TYPE','4')
    five = config.get('TYPE','5')
    return{
        'TYPE':{
            '1':one,
            '2':two,
            '3':three,
            '4':four,
            '5':five
        }
    }
#-------------------------------------------------------------------
print("\033[0;32;40m////////////////////////////////////////////////////////////////////")
print("//                          _ooOoo_                               //")
print("//                         o8888888o                              //")
print("//                         88''.''88                              //")
print("//                         (| ^_^ |)                              //")
print("//                         O\  =  /O                              //")
print("//                      ____/`---'____                            //")
print("//                    .'  \|     |//   `.                         //")
print("//                   /  \|||  :  |||//   \                        //")
print("//                  /  _||||| -:- |||||-  \                       //")
print("//                  |   | \\  -  /// |     |                       //")
print("//                  | _|   ''---/''    |  |                       //")
print("//                  \  .-__  `-`  ___/-.  /                       //")
print("//                 ___`. .'  /--.--\  `. . ___                    //")
print("//             ."" '<  `.____<|>_/___.'  >   '''.                   //")
print("//            | | :  `- `.;`\ _ /`;.`/ - ` : | |                  //")
print("//            \  \ `-.   _ __\ /__ _/   .-` /  /                  //")
print("//      ========`-.____`-.________/___.-`____.-'========          //")
print("//                          `=---='                               //")
print("//     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^         //")
print("//            佛祖保佑       永不宕机     永无BUG                 //")
print("////////////////////////////////////////////////////////////////////\033[0m")
print("\033[0;34;40m好友骚扰神器\033[0m")
print("\033[0;31;40mPowered BY SJY\033[0m")
print("\033[0;32;40m--------------------------------------------------------------------\033[0m")
def sendMsg(msg):
    pyperclip.copy(f"{msg}")
    time.sleep(.1)
    k.press_key(k.control_key)
    k.tap_key('v')
    k.release_key(k.control_key)
    time.sleep(.1)
    k.tap_key(k.enter_key)
def suiji():
    time.sleep(3)
    while True:
        # 读取txt文件路径
        def get_total_lines(filename):
            with open(filename, encoding='utf-8', mode='r') as f:
                lines = sum(1 for line in f)
            return lines
        # 获取随机行号
        def get_random_line_number(total_lines):
            return random.randint(1, total_lines)
        # 获取随机行
        def get_random_line(filename, random_line_number):
            line = linecache.getline(filename, random_line_number)
            return line.strip()
        total_lines = get_total_lines(filename)
        random_line_number = get_random_line_number(total_lines)
        random_line = get_random_line(filename, random_line_number)
        msm = random_line
        sendMsg(msm)
        time.sleep(shijian)
def shunxu():
    time.sleep(3)
    while True:
        def get_total_lines(filename):
            with open(filename, encoding='utf-8', mode='r') as f:
                lines = sum(1 for line in f)
            return lines
        # 获取第一行
        def get_first_line(filename):
            with open(filename, encoding='utf-8', mode='r') as f:
                first_line = f.readline().strip()
            return first_line
        # 获取指定行
        def get_line(filename, line_number):
            with open(filename, encoding='utf-8', mode='r') as f:
                for i, line in enumerate(f):
                    if i == line_number - 1:
                        return line.strip()
            return None
        total_lines = get_total_lines(filename)
        for i in range(1, total_lines + 1):
            line = get_line(filename, i)
            if line:
                msm = line
                sendMsg(msm)
                time.sleep(shijian)
if __name__ == "__main__":
    config_data = read_config('config.ini')
    filename = config_data['TYPE']['1']
    bh = input("请输入文本编号(1~5):")
    print("1.随机发送"+"  "+"2.顺序发送")
    key = input("请选择发送方式：")
    print("1.自定义时间间隔"+"  "+"2.默认时间间隔")
    tm = input("请选择时间间隔方式：")
    if bh == "1":
        filename = config_data['TYPE']['1']
    elif bh == "2":
        filename = config_data['TYPE']['2']
    elif bh == "3":
        filename = config_data['TYPE']['3']
    elif bh == "4":
        filename = config_data['TYPE']['4']
    elif bh == "5":
        filename = config_data['TYPE']['5']
    if tm == "1":
        shijian = int(input("请输入时间间隔："))
        if key == "1":
            while True:
                suiji()
        else:
            while True:
                shunxu()
    else:
        if key == "1":
            while True:
                shijian = random.randint(0, 60) / 6
                suiji()
        else:
            while True:
                shijian = random.randint(0, 60) / 6
                shunxu()