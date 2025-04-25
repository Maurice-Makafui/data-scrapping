#import scrapy  # type: ignore

#class WwrSpider(scrapy.Spider):  # You can keep the class name as WwrSpider
 #   name = 'wwr'  # Change the name to something relevant, like 'glassdoor'
  #  allowed_domains = ['glassdoor.com']
   # start_urls = ['https://www.glassdoor.com/Job/jobs.htm']

    #def parse(self, response):
        # Select the job listings on the page
     #   job_listings = response.xpath('//ul[@class="jlGrid hoverable"]//li[@class="jl"]')

      #  for job in job_listings:
       #     title = job.xpath('.//a[@class="jobLink"]//text()').get()
        #    link = job.xpath('.//a[@class="jobLink"]/@href').get()
         #   company = job.xpath('.//div[@class="jobInfoItem jobEmpolyerName"]//text()').get()
          #  location = job.xpath('.//div[@class="location"]//text()').get()

            # Clean up extracted data (e.g., strip whitespace)
           # title = title.strip() if title else 'N/A'
            #company = company.strip() if company else 'N/A'
            #ocation = location.strip() if location else 'N/A'

            # Ensure the full URL is formed if it's a relative link
            #if link and not link.startswith('http'):
             #   link = response.urljoin(link)

            # Yield the job details
            #yield {
               # 'title': title,
                #'company': company,
                #'location': location,
           #     'link': link,
            #}

        # Handle pagination (if any)
        #next_page = response.xpath('//li[@class="next"]//a/@href').get()
        #if next_page:
        #    yield response.follow(next_page, self.parse)""
        
import scrapy

class BookSpider(scrapy.Spider):
    name = 'wwr'
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        for book in response.css('article.product_pod'):
            rating_class = book.css('p.star-rating::attr(class)').get()
            if rating_class:
                rating = rating_class.split()[-1]
            else:
                rating = 'No Rating'
            
            availability = book.css('p.in_stock.availability::text').get()
            yield {
                'title': book.css('h3 a::attr(title)').get(),
                'price': book.css('p.price_color::text').get(),
                'availability': availability.strip() if availability else 'Not Available',
                'rating': rating,
                'url': book.css('h3 a::attr(href)').get()
            }

        # Handle pagination (if any)
        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page:
            yield response.follow(next_page, self.parse)
