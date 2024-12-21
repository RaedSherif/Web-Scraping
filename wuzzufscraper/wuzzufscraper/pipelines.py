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
                     company_name = adapter.get(field_name).strip().rstrip('-').rstrip()
                     adapter[field_name] = company_name

                ## Lowercase and replace space with hyphen for "mod" and "type"
                if field_name == 'mode' or field_name == 'type':
                    value = adapter.get(field_name)
                    value = value.lower().replace(' ', '-')
                    adapter[field_name] = value

                ## Lowercase the job positon string
                if field_name == 'name':
                    new_name = adapter.get(field_name).lower()
                    adapter[field_name] = new_name




        return item

        

            



        return item
