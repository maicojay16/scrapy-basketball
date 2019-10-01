import scrapy
from sampleBasketball1.items import Samplebasketball1Item
from datetime import datetime
import re


class Samplebasketball1(scrapy.Spider):
	name = "basketball_scrape"

	# First Start Url
	start_urls = ["https://www.slamonline.com"]
    # start_urls.append()

	# npages = 2

	# This mimics getting the pages using the next button. 
	# for i in range(2, npages + 2):
	# 	start_urls.append("https://fundrazr.com/find?category=Health&page="+str(i)+"")
	
	def parse(self, response):
		for href in response.xpath("//div[contains(@class,'plist')]/a//@href"):
			# add the scheme, eg http://
			url  = "https:" + href.extract() 
			yield scrapy.Request(url, callback=self.parse_dir_contents)	
					
	def parse_dir_contents(self, response):
		item = Samplebasketball1Item()

		# Getting Campaign Title
		item['storyTitle'] = response.xpath("//div[contains(@class,'post-detail__title-inner')]//h1/text()").extract()[0]

		# Getting Amount Raised
		# item['amountRaised']= response.xpath("//span[contains(@class, 'stat')]/span[contains(@class, 'amount-raised')]/descendant::text()").extract()

		# # Goal
		# item['goal'] = " ".join(response.xpath("//div[contains(@class, 'stats-primary with-goal')]//span[contains(@class, 'stats-label hidden-phone')]/text()").extract()).strip()

		# # Currency Type (US Dollar Etc)
		# item['currencyType'] = response.xpath("//div[contains(@class, 'stats-primary with-goal')]/@title").extract()

		# # Campaign End (Month year etc)
		# item['endDate'] = "".join(response.xpath("//div[contains(@id, 'campaign-stats')]//span[contains(@class,'stats-label hidden-phone')]/span[@class='nowrap']/text()").extract()).strip()

		# # Number of contributors
		# item['numberContributors'] = response.xpath("//div[contains(@class, 'stats-secondary with-goal')]//span[contains(@class, 'donation-count stat')]/text()").extract()

		# Getting Story
		# story_list = response.xpath("//div[contains(@id, 'full-story')]/descendant::text()").extract()
		# story_list = [x.strip() for x in story_list if len(x.strip()) > 0]
		# item['story']  = " ".join(story_list)

		# Url (The link to the page)
		item['url'] = response.xpath("//meta[@property='og:url']/@content").extract()

		yield item
