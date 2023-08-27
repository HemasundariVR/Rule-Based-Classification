# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        ## ratings --> Float
        try :
            adapter["star_rating"] = float(adapter.get("star_rating"))
        except ValueError :
            adapter["star_rating"] = 0.0

        ## reviews --> int 
        try :
            adapter["no_reviews"] = int(adapter.get("no_reviews").split(" ")[0].replace("(","").replace(",",""))
        except ValueError :
            adapter["no_reviews"] = 0   

        ## enrolled --> int
        try :
            adapter["no_enrolled"] = int(adapter.get("no_enrolled").replace(",",""))
        except :
            adapter["no_enrolled"] = 0        
          
        return item
