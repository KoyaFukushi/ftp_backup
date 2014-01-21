# coding:utf-8
import yaml
import os
import datetime
import threading

SLEEP_TIME = 86400 #一日
FILEIN_DICT = "config.yaml"

def StartBackup():
	
	d = datetime.datetime.today()
	current_time = d.strftime("%Y-%m-%d %H:%M:%S")

	#ドキュメントルートをバックアップするパス
	path = "./" + current_time + "/"

	f = open(FILEIN_DICT, 'r')
	conf = yaml.load(f)
	f.close()

	wget = "wget -mck ==passive-ftp -O '" + path + "' ftp://" + conf["user"] + ":" + conf["pass"] + "@" + conf["url"]
	print wget
	os.system(wget)

	t = threading.Timer(SLEEP_TIME, StartBackup)
	t.start()


if __name__ == "__main__":

	t = threading.Timer(SLEEP_TIME, StartBackup)
	t.start()

