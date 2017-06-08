#!/usr/bin/python


#--------------------------------
def routes():
	return (('get', '/', ('/',  'newController::createWebFormPage')),
			('post', '/', ('/', 'newController::respondToSubmit')),

			('get', '/longlat', ('/longlat', 'newController::createLongLatPage')),
			('post', '/longlat', ('/', 'newController::respondToLongLat')),
			)
