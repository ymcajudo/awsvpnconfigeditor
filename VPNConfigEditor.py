import string

#위 D폴더에 AWS에서 다운로드한 VPN config 파일을 awsvpnconfig-src.txt 로 이름 변경해서 저장
#srcFile = open("D:/03.SW development/01.Python/02.AWSVPNConfigEditer/AWSVPNConfigFiles/awsvpnconfig-src.txt","r")

#프로그램 파일이 있는 폴더에서 아래 파일을 read할 때
#AWS에서 다운로드 받은 VPN config 파일은 awsvpnconfig-src.txt로 이름을 변경해서 본 파이썬 실행파일과 같은 폴더에 저장
srcFile = open("awsvpnconfig-src.txt","r")

lines = []

for paragraph in srcFile:        
    #lines = string.split(paragraph, "\n")
    lines = paragraph.split("\n")
    #resFile = open("D:/03.SW development/01.Python/02.AWSVPNConfigEditer/AWSVPNConfigFiles/awsvpnconfig-res.txt","a")
    resFile = open("awsvpnconfig-res.txt","a")
    for each_line in lines:
        if each_line.find("set") == 0 :       #찾을 문자가 있는 위치값 반환(예: .find("#") == 0 #이 행의 첫번째에 있을 때)
            data = "%s\n" % each_line
            resFile.write(data)
        else:
            pass
        resFile.close()

srcFile.close()
