#!/usr/bin/env /client/venv/bin/python
import json
import os
import platform
import socket
import subprocess
import sys
import time
from importlib import import_module

import easygui

#from connection_dut import controller_login_mcu

global test_suite
test_suite = ""
for_break = False


def client_run(s):
    global test_suite, for_break
    print(os.system("date"))
    if os.path.exists("./script.tar.gz"):
        if platform.system() == 'Linux':
            subprocess.getoutput("rm script.tar.gz")
        else:
            subprocess.getoutput('del *.tar.gz')
    if os.path.exists("./Temp"):
        if platform.system() == 'Linux':
            subprocess.getoutput("rm -r Temp/")
        else:
            subprocess.getoutput('rmdir /Q /S Temp')
    with open('script.tar.gz', 'wb') as f:
        print('file opened')
        l = s.recv(1024)
        while 1:
            f.write(l)
            time.sleep(0.2)
            l = s.recv(1024)
            print("Receiving data....", l[-75:])
            if b"sent" in l:
                break
    if platform.system() == 'Linux':
        os.mkdir("./Temp")
    else:
        os.mkdir('./Temp')
    back_dir = os.getcwd()
    os.chdir("./Temp")
    subprocess.getoutput("tar -xvf ../script.tar.gz")
    print(s.recv(1024))
    s.send(b"Extraction Done")
    print("hello")
    time.sleep(2)
    data = s.recv(8192).decode()
    print(data)
    data1 = json.loads(data)
    print(data)
    data2 = data1.get("test_cases_details")
    mac = data1.get("maclist")
    test_suite = data1.get("test_suite_name")
    serial_numbers = data1.get('serial_number_list')
    c = os.getcwd()
    print(c)
    serial_object = ''
    test_output = []
    os.chdir("./" + test_suite + "/test_scripts")
    c = os.getcwd()
    print(c)
    sys.path.append(c)
    s.send(b"start")
    for test in data2:
        data1_dict = s.recv(4026).decode()
        print('data1_dict', data1_dict)
        send = json.loads(data1_dict)
        try:
            func = getattr(import_module(test["tc_name"]), test["tc_name"])
        except ImportError as e:
            print(e)
        except ImportWarning as e:
            print(e)
        except:
            print('Import Test Module Error')
        
        send["object"] = serial_object
        send["test_output"] = test_output
        send["image_flash"] = 1
        send['serial_number_list'] = serial_numbers
        send["mac_list"] = mac
        ret_dict = func(**send)
        serial_object = ret_dict["object"]
        ret_dict["object"] = ''
        test_output = ret_dict["test_output"]
        ret_dict["client_ip"] = sys.argv[1]
        print(ret_dict)
        data = json.dumps(ret_dict)
        data_len = str(len(data))
        print("Length....", data_len)
        s.send(data_len.encode())
        time.sleep(2)
        s.sendall(data.encode())
        time.sleep(1)
        i = 1
        while i < 10:
            data_check = s.recv(1024).decode()
            if "Data_received" in data_check:
                print("Data Received on Server.")
                for_break = False
                break
            elif "Data_not_received" in data_check:
                time.sleep(2)
                i = i + 1
                for_break = True
                s.sendall(data.encode())
                print("Data Again Send to server")
            else:
                print("---------------- Unknown Message received. ------------------")
        if for_break:
            break
        time.sleep(1)
        if ret_dict["test_status"] == "FAILED":
            if test['exit_on_failure']:
                os.chdir("/client/")
                break
        time.sleep(1)
    os.chdir(back_dir)
    s.close()
    easygui.msgbox('\tTest Are Done.\n\n\tYou can Start Again', 'Test Done')
    if platform.system() == 'Linux':
        subprocess.getoutput("rm -r Temp/")
        subprocess.getoutput("rm *.tar.gz")
    else:
        subprocess.getoutput('rmdir /Q /S Temp')
        subprocess.getoutput('del *.tar.gz')


def socket_init():
    global test_suite
    s = None
    try:
        s = socket.socket()
        while 1:
            connect = s.connect_ex((sys.argv[2], int(sys.argv[3])))
            if connect == 0:
                break
            else:
                time.sleep(5)
                print("Waiting for server connection")
                continue
        while 1:
            print(
                "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" + "\n" + "\t\t\tClient Started\t" + "\n" + "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            data = s.recv(1024)
            if b"start" in data:
                print("Started")
                client_run(s)
            if not data:
                s.close()
                socket_init()
            else:
                continue
    except:
        if s is not None:
            s.close()
            time.sleep(5)
        else:
            time.sleep(2)
        print(test_suite)
        os.chdir("/client/")
        socket_init()


socket_init()
