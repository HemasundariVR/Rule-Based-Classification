# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScraperItem(scrapy.Item):
    # define the fields for your item here like:
    course_name =  scrapy.Field()
    no_enrolled =  scrapy.Field()
    fin_aid_status = scrapy.Field()
    star_rating = scrapy.Field()
    no_reviews = scrapy.Field()
    skills = scrapy.Field()

