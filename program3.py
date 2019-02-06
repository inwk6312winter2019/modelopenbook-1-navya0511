transit_access_in=[]
fw_management_access_in=[]
global_access=[]
fin=open("running-config.cfg")
def list_ifname_ip(fin):
	for line in fin:
		line=line.strip()
		if "access-list" in line:
			if "transit_access_in" in line:
				transit_access_in.append(line)
			elif "fw-management_access_in" in line:
				fw_management_access_in.append(line)
			elif "global_access" in line:
				global_access.append(line)
print(list_ifname_ip(fin))
print(transit_access_in)
print(fw_management_access_in)
print(global_access)
