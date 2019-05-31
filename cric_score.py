import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.cricbuzz.com/live-cricket-scores/22345/ire-vs-afg-2nd-odi-afghanistan-tour-of-ireland-2019')
s = r.text
soup = BeautifulSoup(s, 'html.parser')
soup.find_all('a',class_='cb-text-link')
player_run=soup.find_all('div',class_='cb-col-10')

#test for match status by cuurently playing players
tst=str(player_data)[0] 

if tst == "[":
  status=soup.find_all('div',class_='cb-text-mom')
  ms=str(status[0])
  ms=ms.split('>')[1].split('<')[0]
  print("Match Ended : "+ms)
  
else:
  # ball for player who is currentlly at strick
  p1b=str(player_run[2])
  p1b=p1b.split('>')[1].split('<')[0]
  p_ball=[int(p1b)]
  # ball for partner player
  p2b=str(player_run[4])
  p2b=p2b.split('>')[1].split('<')[0]
  p_ball.append(int(p2b))




  # name for player who is currentlly at strick
  p1=str(player_data[0])
  p1=p1.split('>')[1].split('<')[0] 
  p_name=[p1+"("+str(p_ball[0])+" Balls)"]
  # name for partner player
  p2=str(player_data[1])
  p2=p2.split('>')[1].split('<')[0]
  p_name.append(p2+"("+str(p_ball[1])+" Balls)")




  # run for player who is currentlly at strik
  p1r=str(player_run[2])
  p1r=p1r.split('>')[1].split('<')[0]
  p_run=[int(p1r)]
  # run for partner player
  p2r=str(player_run[4])
  p2r=p2r.split('>')[1].split('<')[0]
  p_run.append(int(p2r))

  # plotting data into bars format
  width = 0.4
  mp.ylabel("runs")
  mp.xlabel("Players Name")
  mp.bar(p_name,p_run,width)


  