import requests

def save(mvid):
    headers = {
        'authority': 'mindgeek.in',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'referer': 'https://mindgeek.in/channel.php',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,tr;q=0.8',
        'cookie': '_ga=GA1.2.1132054486.1555947257; _gid=GA1.2.1064032949.1556324271; PHPSESSID=mgfl320o88fdk5js0voergmhc1; _gat_gtag_UA_130576077_2=1',
    }
    
    params = (
        ('id',mvid),
    )

    r = requests.get('https://mindgeek.in/edit-channel.php', headers=headers, params=params)
    s = r.text

    if s.find("selected>") == -1:
        return(str(mvid)+','+'none'+','+'none'+','+'none'+'\n')
    else:
        start = 'selected>'
        end = '</option>'
        firstname = (s.split(start))[1].split(end)[0]
        start = '<input type="text" name="channel_name" id="channel_name" value="'
        end = '" required/>'
        lastname = (s.split(start))[1].split(end)[0]
        start = 'placeholder="http://www.xyz.com/channel_name.mp4" value="'
        end = '" required/>'
        dlink = (s.split(start))[1].split(end)[0]
        print(str(mvid)+','+firstname+','+lastname+','+dlink+'\n')
        return(str(mvid)+','+firstname+','+lastname+','+dlink+'\n')

file1 = open("alllinks.txt","a")
for i in range(18384,18385):
    file1.write(save(str(i))) 
file1.close()