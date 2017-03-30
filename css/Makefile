all: google.com.css youtube.com.css facebook.com.css baidu.com.css wikipedia.org.css yahoo.com.css reddit.com.css qq.com.css taobao.com.css amazon.com.css tmall.com.css sohu.com.css twitter.com.css live.com.css vk.com.css instagram.com.css sina.com.cn.css 360.cn.css jd.com.css linkedin.com.css weibo.com.css yandex.ru.css hao123.com.css netflix.com.css t.co.css imgur.com.css ebay.com.css pornhub.com.css wordpress.com.css msn.com.css bing.com.css aliexpress.com.css livejasmin.com.css tumblr.com.css microsoft.com.css stackoverflow.com.css ok.ru.css

%.css:
	curl 'http://cssstats.com/stats?url=http%3A%2F%2F'$*'&ua=Browser%20Default' | ../html2css.py > $@
	sleep 2
