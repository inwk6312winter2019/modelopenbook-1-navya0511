fin=open("running-config.cfg",'r')

def list_ifname_ip(fin):
    dict={}  
    for line in fin:
        if 'no' not in line:
            if 'nameif' in line:
                line=line.strip()
                key=line.split(" ")
               
            if 'ip address' in line and '.' in line:
                line=line.strip()
                iptemp=line.split(" ")
                tup=(iptemp[2],)
                dict.setdefault(key[1],(iptemp[2],iptemp[3]))
           
    return dict
print(list_ifname_ip(fin))
