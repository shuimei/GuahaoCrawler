hospitals = {
	"template": "HospitalList",
	"fields": {
		"name": "//ul[@class='hos_ul']/li/div/div/dl/dt/a/text()",
		"page_link": "//ul[@class='hos_ul']/li/a/@href",
		"rank": "//ul[@class='hos_ul']/li/div/div/dl/dt/em/text()",
		"tel": "//ul[@class='hos_ul']/li/div/div/dl/dd/p[@class='tel']/span/text()",
		"address": "//ul[@class='hos_ul']/li/div/div/dl/dd/p[@class='addr']/span/text()",
		"order": "//div[@class='comment comment2 g-clear']/label[@monitor]/text()"
			}
}