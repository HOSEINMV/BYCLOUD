#HOSEIN_MV
import socket
import sys
print('''
 ,ggggggggggg,   ,ggg,         gg      ,gggg,         ,gggg,     _,gggggg,_      ,ggg,         gg  ,gggggggggggg,   
dP"""88""""""Y8,dP""Y8a        88    ,88"""Y8b,      d8" "8I   ,d8P""d8P"Y8b,   dP""Y8a        88 dP"""88""""""Y8b,   
Yb,  88      `8bYb, `88        88   d8"     `Y8      88  ,dP  ,d8'   Y8   "8b,dPYb, `88        88 Yb,  88       `8b,   VERSION 2
 `"  88      ,8P `"  88        88  d8'   8b  d8   8888888P"   d8'    `Ybaaad88P' `"  88        88  `"  88        `8b
     88aaaad8P"      88        88 ,8I    "Y88P'      88       8P       `""""Y8       88        88      88         Y8
     88""""Y8ba      88        88 I8'                88       8b            d8       88        88      88         d8
     88      `8b     88       ,88 d8            ,aa,_88       Y8,          ,8P       88        88      88        ,8P
     88      ,8P     Y8b,___,d888 Y8,          dP" "88P       `Y8,        ,8P'       88        88      88       ,8P'
     88_____,d8'      "Y88888P"88,`Yba,,_____, Yb,_,d88b,,_    `Y8b,,__,,d8P'        Y8b,____,d88,     88______,dP' 
    88888888P"             ,ad8888  `"Y8888888  "Y8P"  "Y88888   `"Y8888P"'           "Y888888P"Y8    888888888P"   
                          d8P" 88                                                                                   
                        ,d8'   88                                                                                   
                        d8'    88                                                                                   
                        88     88                                                                                   
                        Y8,_ _,88                                                                                   
                         "Y888P"                                                                                    

CODED BY HOSEIN_MV

OUR TELEGRAM CHANNEL:@CRACKER_CLUB AND @NH_PY

SUP : @MESTER_LINUX
''')
def cloudflare():
    try:
        subdomain = ['ftp','cpanel','shop','api','mysql','secure','server','mail','webmail','direct','ip','sctp','ipv4','ipv6','ICMP','rsvp','ipsec','igmp','ecn','icmpv6','BGP','DHCP','DNS','HTTP','HTTPS','IMAP','LDAP','MGCP','MQTT','MNTP','NTP','POP','PTP','PTP','RTP','RTSP','RIP','SIP','SMTP','SNMP','SOCKS','SSH','Telnet','TLS','ssl','FTAM','ATP','DDP','NCP','ICMP','Gopher','SLIP','udp','tcp','slip','ppp','IPX','stp','nwlink','arp','dhcp','NetBEUI','CSMA','cd','SMS','NetFlow','SMB','DHCP','EIGRP','OSPF','APPLICATION','TRANSPORT','INTERNET','Interface','NEWS','BGP','DHCP','CIDR','IPX','DDP','admin','blog','host','cdn','www','YAHOO','Bluetooth','FTPS']

        url = input("Enter Your Target with out http/https :")

        if url == "":
            try:
                print("I COULD NOT BYPASS")
                sys.exit()
            except:
                return
        for sub in subdomain:
            try:
                http = str(sub) + "." + str(url)
                bypass = socket.gethostbyname(str(http))
                print(" [!] BYPASSED BY HOSEIN MV: " + str(bypass) + ' | ' + str(http))
            except:
                pass
        try:
            input(' [*]FINISH back to menu (press enter...)')
        except:
            print("")
            sys.exit()
    except:
        print("")
cloudflare()
