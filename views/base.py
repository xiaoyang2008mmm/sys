# -*- coding: utf-8 -*- 
import tornado.web 

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
       return self.application.db



    def archivemgr_path(self):
	archivemgr= "/root/d/src/uarchivemgr-linux64"

	return  archivemgr

    def tmp_video_path(self):
	tmp_video_path = "/tmp/ucloud/download/"
	
	return tmp_video_path
