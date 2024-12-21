import scrapy
import urllib.parse
from wuzzufscraper.items import WuzzufscraperItem

class JobspiderSpider(scrapy.Spider):
    name = "jobspider"
    allowed_domains = ["wuzzuf.net"]
    start_urls = ['https://wuzzuf.net/a/IT-Software-Development-Jobs-in-Egypt?filters%5Broles%5D%5B0%5D=IT%2FSoftware%20Development&start=0']


    def parse(self, response):

        job_item = WuzzufscraperItem()

        def fix(x):
            current_location = []
            for i in range(len(x)):
                loc =x[i]
                loc = loc.strip()
                current_location.append(loc)

                if not loc.endswith(','):
                    locs = current_location
                    return(' '.join(locs))

        jobs = response.css('div.css-pkv5jc')
        if not jobs:
            self.log(f"No more jobs found. Stopping at {response.url}")
            return


        for job in jobs:

            location_list =job.css('span.css-5wys0k::text').getall()
            if location_list == [] :
                break

            
            job_item['name'] = job.css('h2.css-m604qf a::text').get(),
            job_item['company_name'] = job.css('a.css-17s97q8::text').get(),
            job_item['type'] = job.css('a.css-n2jc4m  span::text').get(),
            job_item['location'] = fix(location_list),
            job_item['mode'] = job.css('span.css-o1vzmt::text').get(),
            job_item['url'] = job.css('h2.css-m604qf a::attr(href)').get() 
            

            yield job_item

            next_page = response.css('a.css-1fcv3il ::attr(href)').get()

            if jobs:
                next_page_url = next_page
                yield response.follow(next_page_url, callback = self.parse)

        self.log(f"Scraping page: {response.url}")

        

        # Extract the current 'start' parameter
        url = response.url
        parsed_url = urllib.parse.urlparse(url)
        query_params = urllib.parse.parse_qs(parsed_url.query)
        current_start = int(query_params.get('start', [0])[0])

        # Increment 'start' for the next page
        next_start = current_start + 1
        query_params['start'] = [str(next_start)]
        next_query = urllib.parse.urlencode(query_params, doseq=True)
        next_url = urllib.parse.urlunparse(parsed_url._replace(query=next_query))

        # Check if a "Next" button exists before yielding the next request
        next_button = response.css('a.css-1fcv3il ::attr(href)').get()
        if next_button:
            self.log(f"Next URL: {next_url}")
            yield scrapy.Request(url=next_url, callback=self.parse)
