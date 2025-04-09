# -*- coding: UTF-8 -*-
import xbmc, xbmcgui, xbmcplugin, xbmcaddon,requests, xbmcvfs, resolveurl
import re, os

#USERDATA_PATH = xbmcvfs.translatePath('special://home/addons/')

#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}
#read_pb = requests.get('https://pastebin.com/raw/gjN94ax1', verify=False, headers=headers)
#html_pb = read_pb.text

#scraping regex codes thru pastebin

#pflix_main_regex = r'<pinoystvflix>(.+?)</pinoystvflix>'
#pflix_main_block = re.compile(pflix_main_regex,re.DOTALL).findall(str(html_pb))


def replace_unicode(text):
	text = text.replace('&#7424;','A').replace('&#665;','B').replace('&#7428;','C').replace('&#7429;','D').replace('&#7431;','E').replace('&#1171;','F').replace('&#610;','G').replace('&#668;','H').replace('&#618;','I').replace('&#7434;','J').replace('&#7435;','K').replace('&#671;','L').replace('&#7437;','M').replace('&#628;','N')\
	.replace('&#7439;','O').replace('&#7448;','P').replace('&#42927;','Q').replace('&#640;','R').replace('&#42801;','S').replace('&#7451;','T').replace('&#7452;','U').replace('&#7456;','V').replace('&#7457;','W').replace('&#120;','X').replace('&#655;','Y').replace('&#7458;','Z').replace('&#7458;','Z').replace('\\\\t','')
	return text





#send_log(block2,'BLOCK2')

def scrape_main():
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}
	Readit = requests.get('https://pinoysflixlambingan.su/',headers=headers)
	html = Readit.text


	main_regex = r'<div class="main-container">(.+?)<h3 class="widget-title">'
	main_block = re.compile(main_regex,re.DOTALL).findall(str(html))

	#return main_block

	#xbmc.log('pflix_main######################################################### '+str(pflix_main_block),2)

	
	pbin_flix_main_regex = r'<div class="featured-wrap clearfix">.+?<a href="(.+?)".+?><img.+?src="(.+?)".+?<h2 class="title.+?<a href.+?>(.+?)</a>'
	pbin_flix_main_block = re.compile(pbin_flix_main_regex,re.DOTALL).findall(str(main_block))

	source = []

	for url,image,title in pbin_flix_main_block:
		sources = '<name>'+title+'</name><icon>'+image+'</icon><url>'+url+'</url>'
		source.append(sources)


	np = re.compile('<a class="next page-numbers" href="(.+?)"><i class=' ,re.DOTALL).findall(str(html))
	#np = re.compile(pbin_np_block,re.DOTALL).findall(html)

	xbmc.log('np ######################################################### '+str(np),2)
	
	for url in np:
		url = '<nextpage>nextpagepflix/'+url+'</nextpage>'
		source.append(url)

	data = (str(source))
	new_data = replace_unicode(data)
	return new_data	

	#return sources
	#xbmc.log('sources######################################################### '+str(sources),2)
	
def get_p_links(url):
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}
	Readit = requests.get(url,headers=headers)
	html = Readit.content
	Sources = []
	#new_sources = []
	#html = html.decode('utf-8')
	#xbmc.log('HTMLPINOYFLIX######################################################### '+str(html),2)


	blocklinks_regex = r'<div class="main-container">(.+?)Leave a Reply'
	main_block = re.compile(blocklinks_regex,re.DOTALL).findall(str(html))[0]
	#listmatch_regex = r'<[iI][fF][rR][aA][mM][eE].+?[sS][rR][cC]="(.+?)"'
	#main_listmatch = re.compile(listmatch_regex,re.DOTALL).findall(str(main_block))
	#xbmc.log('Regex_main_block ######################################################### '+str(main_listmatch),2)

	if "<strong>Coming Soon</strong>" in main_block:
		source = '<url>COMING SOON</url>'
		xbmc.log('SOURCE ######################################################### '+str(source),2)
		#else:
		#	source = '<url>NO LINKS FOUND</url>'
		Sources.append(source)
		#xbmc.log('SOURCES######################################################### '+str(sources),2)
	else:
		listmatch_regex = r'<[iI][fF][rR][aA][mM][eE].+?[sS][rR][cC]="(.+?)"'
		main_listmatch = re.compile(listmatch_regex,re.DOTALL).findall(str(main_block))
	# 	#xbmc.log('pbin_main_listmatch######################################################### '+str(pbin_main_listmatch),2)
	# 	#thisRegex =r'<h2 style=\"text-align(.+?)<div id="recent-posts-2'
	#	Regex_me = re.compile(main_listmatch,re.DOTALL).findall(str(html))
		xbmc.log('Regex######################################################## '+str(main_listmatch),2)

		for link in main_listmatch:
			links = '<url>'+link+'</url>'
			xbmc.log('link_source ######################################################## '+str(links),2)
			Sources.append(links)
		xbmc.log('Sources ######################################################## '+str(Sources),2)
	
	return Sources


def scrape_pinoysflix():
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}
	Readit = requests.get('https://pinoyflixs.com/',headers=headers)
	html = Readit.text


	main_regex = r'<div class="main-container">(.+?)<h3 class="widget-title">'
	main_block = re.compile(main_regex,re.DOTALL).findall(str(html))

	#return main_block

	#xbmc.log('pflix_main######################################################### '+str(pflix_main_block),2)

	
	pbin_flix_main_regex = r'<div class="featured-wrap clearfix">.+?<a href="(.+?)".+?><img.+?src="(.+?)".+?<h2 class="title.+?<a href.+?>(.+?)</a>'
	pbin_flix_main_block = re.compile(pbin_flix_main_regex,re.DOTALL).findall(str(main_block))

	source = []

	for url,image,title in pbin_flix_main_block:
		sources = '<name>'+title+'</name><icon>'+image+'</icon><url>'+url+'</url>'
		source.append(sources)


	np = re.compile('<a class="next page-numbers" href="(.+?)"><i class=' ,re.DOTALL).findall(str(html))
	#np = re.compile(pbin_np_block,re.DOTALL).findall(html)

	xbmc.log('np ######################################################### '+str(np),2)
	
	for url in np:
		url = '<nextpage>nextpagepflix/'+url+'</nextpage>'
		source.append(url)

	data = (str(source))
	new_data = replace_unicode(data)
	return new_data	

	#return sources
	#xbmc.log('sources######################################################### '+str(sources),2)



