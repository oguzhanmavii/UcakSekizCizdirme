from dronekit import  connect,VehicleMode,Command,LocationGlobalRelative,Vehicle
import time
from  pymavlink import mavutil

print("Bağlanıyor..")
baglanti_adresi="tcp:127.0.0.1:5762"
ucak = connect(baglanti_adresi,wait_ready=True,timeout=100)

def arm_ol():
    while ucak.is_armable==False:
        print("Arm olamıyor !")
        time.sleep(1)
    ucak.mode = VehicleMode("GUIDED")
    while ucak.mode == 'GUIDED':
        print("GUIDED moda geçiliyor..")
        time.sleep(1)
    print("GUIDED moda geçildi.")
    ucak.armed = True
    while ucak.armed is False:
        print("Arm için bekleniyor..")
        time.sleep(1)
    print("Arm oldu.")


def kalkis(irtifa):
    kalkis_komutu= Command(0,0,0,3,mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,0,0,15,0,0,0,0,0,irtifa)
    print("Kalkış komutu oluşturuldu")
    return kalkis_komutu

def hedefNoktayaGidildi(enlem,boylam,irtifa):
    komut_git= Command(0,0,0,3,mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,0,0,0,0,0,0,enlem,boylam,irtifa)
    print("Hedef Noktaya gidiliyor..")
    return  komut_git

def inis(enlem,boylam):
    komut_inis= Command(0,0,0,3,mavutil.mavlink.MAV_CMD_NAV_LAND,0,0,0,0,0,0,enlem,boylam,0)
    print("İniş için hazırlanıyor..")
    return komut_inis

def sagaDon(saniye,yon,enlem,boylam,irtifa):

    saga_Don= Command(0,0,0,3,mavutil.mavlink.MAV_CMD_NAV_LOITER_TIME,1,0,saniye,0,yon,0,enlem,boylam,irtifa)
    print("Saga donüş gerçekleştiriliyor..")
    return saga_Don

def solaDon(saniye,yon,enlem,boylam,irtifa):

    sola_Don= Command(0,0,0,3,mavutil.mavlink.MAV_CMD_NAV_LOITER_TIME,1,0,saniye,0,yon,0,enlem,boylam,irtifa)
    print("Sola donüş gerçekleştiriliyor..")
    return sola_Don

komut= ucak.commands
komut.download()
komut.wait_ready()
komut.clear()

komut1=kalkis(25)
komut2=hedefNoktayaGidildi(39.9038518,41.2362063,20)
komut3=sagaDon(3,+1,39.9047078,41.2371182,20)
komut4=solaDon(3,-1,39.9054649,41.2378049,20)
komut5=inis(39.9043703,41.2366140)


komut.add(komut1)
komut.add(komut2)
komut.add(komut3)
komut.add(komut4)
komut.add(komut5)

ucak.flush()
ucak.mode=VehicleMode("AUTO")
arm_ol()

ucak.mode=VehicleMode("AUTO")
