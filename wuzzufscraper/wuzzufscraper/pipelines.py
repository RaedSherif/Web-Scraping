# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WuzzufscraperPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        field_names = adapter.field_names()

        for field_name in field_names:
                ## Strip whitespace and "-" from company-name
                if field_name == 'company_name':
                    company_name = adapter.get(field_name)

                    if isinstance(company_name,str): 
                        company_name = company_name.strip().rstrip('-').rstrip()
                    elif isinstance(company_name, (list, tuple)):
                        company_name = ' '.join(map(str, company_name)).strip().rstrip('-').rstrip()
                    
                    adapter[field_name] = company_name

                ## Lowercase and replace space with hyphen for "mode" and "type"
                if field_name == 'mode' or field_name == 'type':
                    value = adapter.get(field_name)

                    if isinstance(value, str):
                        value = value.lower().replace(' ', '-')
                    elif isinstance(value, (list,tuple)):
                        value = ' '.join(map(str, value)).lower()
                    
                    adapter[field_name] = value

                ## Lowercase the job position string
                if field_name == 'name':
                    new_name = adapter.get(field_name)
                    if isinstance(new_name, str):
                        new_name = new_name.lower()
                    elif isinstance(new_name, (tuple,list)):
                        new_name = " ".join(new_name).lower().strip()
                        adapter[field_name] = new_name

                    adapter[field_name] = new_name

                ## Splitting the location into three variables for better data analysis later on
                if field_name == 'location':
                    location_value = adapter.get(field_name)
                    part = []

                    if isinstance(location_value, (tuple,list)):
                        location_value = " ".join(location_value).strip()

                    if isinstance(location_value, str):  # Ensure it's now a string
                        location_value = location_value.strip()
                        parts = location_value.split(',')
                    
                    
                    city = None
                    governate = None
                    country = None

                    if len(parts) == 1:
                        city = None
                        governate = None
                        country = parts[0].strip()

                    elif len(parts) == 2:
                        city = None
                        governate = parts[0].strip()
                        country = parts[1].strip()

                    elif len(parts) == 3:
                        city = parts[0].strip()
                        governate = parts[1].strip()
                        country = parts[2].strip()
                    
                    else:
                        city = None
                        governate = None
                        country = None
                    
                    
                    adapter['city'] = city
                    adapter['governate'] = governate
                    adapter['country'] = country

        ## This orders the fields and their respective values in the order we want
        ordered_item = {
            'name': adapter.get('name'),
            'company_name': adapter.get('company_name'),
            'type': adapter.get('type'),
            'mode': adapter.get('mode'),
            'location': adapter.get('location'),
            'city': adapter.get('city'),
            'governate': adapter.get('governate'),
            'country': adapter.get('country'),
            'url': adapter.get('url'),
        }

        return ordered_item
