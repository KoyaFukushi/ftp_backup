# coding:utf-8
import yaml
import os
import datetime
import threading

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

if __name__ == "__main__":
	StartBackup()

