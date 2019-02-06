fin=("running-config.cfg")
fnew=("running-confignew.cfg")
def new_config(fin,fnew):
    for line in fin:
        if 'ip address' in line and '.' in line:
            line=line.strip()
            line=line.split()
            ipadd=line[2]
            mask=line[3]
            ipadd=ipadd.split('.')
            mask=mask.split('.')
            if ipadd[0] =='192' or ipadd[0] =='172':
                ipadd[0]='10'

            if (mask[0]=='255' and mask[1]=='255') or mask[2]=='255':
                mask[1]=mask[2]=mask[3]='0'

            ipadd=' ip address '+'.'.join(ipadd)+' '+'.'.join(mask)+'\n'
            
            fnew.write(ipadd)

        else:
            fnew.write(line)
    return True

