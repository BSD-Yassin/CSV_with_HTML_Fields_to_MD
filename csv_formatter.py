import pandas as pd
from bs4 import BeautifulSoup as bs

class File():
    def __init__(self, path):
        self.path = path
        self.data = []

    def get_data(self):
        data = pd.read_csv(self.path)
        self.data = data
        return self.data
    
    def write_data(self, outpath):
        try:
            for title, description, content in zip(self.data['title'], self.data['description'], self.data['content']):
                if description == str:
                    description = description.str.replace('\n', ' ')
                else: 
                    pass
                with open(f'{outpath}/{title}.md', 'w+') as file:
                    file.write(str(description))
                    file.write(content)
                    file.close()
                print('File created' ':' f'{title}')
        except:
            print('Columns not found')

fichier = File('db_files/database_backup_pages.csv')
fichier.get_data()
fichier.write_data('output_folder')