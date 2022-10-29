import osascript
# target_volume = 100
#  osascript.osascript("set volume output volume {}".format(target_volume))
import re
while True:
    result = osascript.osascript('get volume settings')
    find=re.findall('output volume:\S+',result[1])
    find=str(find)
    find=find.split(':')
    volume=int(find[1].replace(",']",''))
    print(volume)
