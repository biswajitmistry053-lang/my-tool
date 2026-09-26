import os, socket, getpass, phonenumbers
from phonenumbers import carrier, geocoder, timezone
R="\033[91m"; G="\033[92m"; Y="\033[93m"; C="\033[96m"; W="\033[97m"
PWD="Biswajit"
os.system("clear")
print(f"{G} ____ ___ ______ ___ _ _____ _____ ___ _ ")
print(f"{C}======= BISWAJIT TOOL v2.1 - FIXED =======")
p=getpass.getpass(f"{W} Enter Password: {C}")
if p!=PWD:
 print(f"{R} Wrong Password!"); exit()

while True:
 os.system("clear")
 print(f"{G} BISWAJITH TOOL v2.1")
 print(f"{W}-------------------------------------------")
 print(f"{G}[1] IP Tracker\n[2] Website IP Finder\n[3] My IP & Location")
 print(f"{Y}[4] Phone Number Info [FIXED]\n[5] Instagram User Info [NEW]")
 print(f"{R}[0] Exit")
 print(f"{W}-------------------------------------------")
 ch=input(f"{W} Select Option (1-5): {C}")

 if ch=="1":
  ip=input(f"{W} Enter IP: {C}")
  os.system(f"curl -s ipinfo.io/{ip}")
  input(f"\n{Y}Press Enter...")
 elif ch=="2":
  s=input(f"{W} Enter Website: {C}")
  try:
   ip=socket.gethostbyname(s)
   print(f"{G}{s} => {W}{ip}")
   os.system(f"curl -s ipinfo.io/{ip}")
  except: print(f"{R} Not Found!")
  input(f"\n{Y}Press Enter...")
 elif ch=="3":
  os.system("curl -s ipinfo.io")
  input(f"\n{Y}Press Enter...")
 elif ch=="4":
  num=input(f"{W} Enter Phone with +91: {C}")
  try:
   if not num.startswith("+"): num="+"+num
   ph=phonenumbers.parse(num)
   print(f"{G} Valid: {W}{phonenumbers.is_valid_number(ph)}")
   print(f"{G} Country: {W}{geocoder.description_for_number(ph,'en')}")
   print(f"{G} Carrier: {W}{carrier.name_for_number(ph,'en')}")
   print(f"{G} TimeZone: {W}{timezone.time_zones_for_number(ph)}")
   print(f"{G} Region: {W}{phonenumbers.region_code_for_number(ph)}")
  except Exception as e: print(f"{R} Error: {e}")
  input(f"\n{Y}Press Enter...")
 elif ch=="5":
  user=input(f"{W} Enter Instagram Username: {C}")
  print(f"{Y} Instagram is blocking without login. Need login tool, por e banabo.")
  input(f"\n{Y}Press Enter...")
 elif ch=="0": break
