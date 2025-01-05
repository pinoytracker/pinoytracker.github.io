# -*- coding: UTF-8 -*-
import xbmc, xbmcgui, xbmcplugin, xbmcaddon,requests, xbmcvfs, resolveurl
import re, os, sys, urllib, urllib.parse, inspect

USERDATA_PATH = xbmcvfs.translatePath('special://home/addons/')


def add_dir(dir_type='',mode='',url='',title='',iconimage='',fanart='',description=''):
	u = sys.argv[0]+"?mode="+str(mode)+"&iconimage="+urllib.parse.quote_plus(iconimage)+"&description="+urllib.parse.quote_plus(description)
	x=2; num = inspect.getfullargspec(add_dir); i = len(num[0])
	while i-2 >0:
		u += "&"+num[0][x]+"="+urllib.parse.quote_plus(locals()[num[0][x]])
		x+=1; i-=1


	lis = xbmcgui.ListItem(title)
	videoInfoTag = lis.getVideoInfoTag()
	videoInfoTag.setTitle(title)
	videoInfoTag.setPlot(description)
	#origcode
	#({ 'poster': 'poster.png', 'banner' : 'banner.png' })
	lis.setArt({'poster':iconimage,'thumb':iconimage})

	#lis.setInfo( type="Video", infoLabels={"Title": title,"Plot":description})
	#liz.setInfo( type="Video", infoLabels={"Title": name,"Plot":description})
	lis.setProperty( "Fanart_Image", fanart)
	if dir_type != '': fo=True
	else: fo=False ; lis.setProperty("IsPlayable","true")
	link = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=lis,isFolder=fo)
	return link

def replace_unicode(text):
	text = text.replace('&#7424;','A').replace('&#665;','B').replace('&#7428;','C').replace('&#7429;','D').replace('&#7431;','E').replace('&#1171;','F').replace('&#610;','G').replace('&#668;','H').replace('&#618;','I').replace('&#7434;','J').replace('&#7435;','K').replace('&#671;','L').replace('&#7437;','M').replace('&#628;','N')\
	.replace('&#7439;','O').replace('&#7448;','P').replace('&#42927;','Q').replace('&#640;','R').replace('&#42801;','S').replace('&#7451;','T').replace('&#7452;','U').replace('&#7456;','V').replace('&#7457;','W').replace('&#120;','X').replace('&#655;','Y').replace('&#7458;','Z').replace('&#7458;','Z').replace('\\\\t','')
	return text

def asianc_main():
	add_dir('f','','','[B][COLOR red]test[/COLOR][/B]','','')
	return all()

