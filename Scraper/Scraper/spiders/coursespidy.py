import scrapy
from Scraper.items import ScraperItem


class CoursespidySpider(scrapy.Spider):
    name = "coursespidy"
    allowed_domains = ["www.coursera.org"]
    start_urls = ["https://www.coursera.org/professional-certificates/"]

    def parse(self, response) :
        page_urls = response.css("a.font-md ::attr(href)").getall()
        for page in page_urls :
            page_link = "https://www.coursera.org" + page
            yield response.follow(page_link, callback = self.parse_certificate)

    def parse_certificate(self, response) :
        certificate_urls = response.css("a.css-j655ez ::attr(href)").getall()
        for certificate in certificate_urls :
            certificate_link = "https://www.coursera.org" + certificate
            yield response.follow(certificate_link, callback = self.parse_page)    

    def parse_page(self, response) :
        course_urls = response.css("a.css-g8gmtr ::attr(href)").getall()
        for course in course_urls :
            course_link = "https://www.coursera.org" + course
            yield response.follow(course_link, callback = self.parse_course)

    def parse_course(self, response) :

        course_details = ScraperItem()
        course_name =  response.css("h1.cds-119 ::text").get()
        no_enrolled =  response.css("p.cds-119 strong span ::text").get()
        fin_aid_status = response.css("button.button-link ::text").get()
        star_rating = response.css("div.css-h1jogs ::text").get()
        no_reviews = response.css("p.css-dmxkm1 ::text").get()
        skills = "|".join(response.css("span.css-18p0rob ::text").getall()).lower()
        url = response.url
        
        course_details["course_name"] = course_name
        course_details["no_enrolled"] = no_enrolled
        course_details["fin_aid_status"] = fin_aid_status
        course_details["star_rating"] = star_rating
        course_details["no_reviews"] = no_reviews
        course_details["skills"] = skills

        yield course_details
        



        


        
    
