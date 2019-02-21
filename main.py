#Starter code to clone VMs and print ip addresses
#Sources: https://github.com/RTCedu/CNA350/blob/master/CNA350/VirtualBoxBasic.py // https://pythonhosted.org/pyvbox/virtualbox/pool.html
#Wyatt Humphreys: wlhumphreys@student.rtc.edu | 2/21/19 CNA 350
import os, virtualbox, vboxapi, win32com, time

from virtualbox.pool import MachinePool


vm_create_number = input("How many VM's do you want? ")
int_vcn = int(vm_create_number)
vm_os = raw_input("UbuntuMini, Lubuntu, or UbuntuFull? ")
str_vmos = str(vm_os)
counter = 0


if vm_os == "UbuntuMini":
    while counter < int_vcn:
        pool = MachinePool('UbuntuMini')
        sessions = []
        sessions.append(pool.acquire("name", "password"))
        counter = counter + 1
    print(counter)
    # You now have three running machines.
    vbox = virtualbox.VirtualBox()
    vm = vbox.find_machine('UbuntuMini Pool')
    vm.launch_vm_process()
    session = vm.create_session()
    time.sleep(30)
    session.console.keyboard.put_keys('name')
    session.console.keyboard.put_keys(['ENTER'])
    time.sleep(0.5)
    session.console.keyboard.put_keys('password')
    session.console.keyboard.put_keys(['ENTER'])
    time.sleep(15)
    session.console.keyboard.put_keys('ifconfig')
    time.sleep(30)
    session.console.power_down()
elif vm_os == "Lubuntu":
    pool = MachinePool('Lubuntu')
    sessions = []
    while counter < int_vcn:
        sessions.append(pool.acquire("name", "password"))
        counter = counter + 1
    print(counter)
    # You now have three running machines.
    vbox = virtualbox.VirtualBox()
    # print("VM(s):\n + %s" % "\n + ".join([vm.name for vm in vbox.machines]))
    vm = vbox.find_machine('Lubuntu Pool')
    vm.launch_vm_process()
    session = vm.create_session()
    time.sleep(40)
    session.console.keyboard.put_keys(['TAB'])
    time.sleep(0.5)
    session.console.keyboard.put_keys('password')
    session.console.keyboard.put_keys(['ENTER'])
    time.sleep(30)
    session.console.power_down()
elif vm_os == "UbuntuFull":
    pool = MachinePool('UbuntuFull')
    sessions = []
    while counter < int_vcn:
        sessions.append(pool.acquire("name", "password"))
        counter = counter + 1
    print(counter)
    # You now have three running machines.
    vbox = virtualbox.VirtualBox()
    # print("VM(s):\n + %s" % "\n + ".join([vm.name for vm in vbox.machines]))
    vm = vbox.find_machine('UbuntuFull Pool')
    vm.launch_vm_process()
    session = vm.create_session()
    time.sleep(70)
    session.console.keyboard.put_keys(['TAB'])
    time.sleep(0.5)
    session.console.keyboard.put_keys('password')
    session.console.keyboard.put_keys(['ENTER'])
    time.sleep(30)
    session.console.power_down()
else:
    print("Please type a listed OS")

