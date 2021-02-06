from kaggle.api.kaggle_api_extended import KaggleApi
from tqdm import tqdm

class KAGGLE:
    def __init__(self):
        self.api = KaggleApi()
        self.api.authenticate()

    def search(self, category):
        competitions = self.api.competitions_list(category = category)
        for comp in competitions:
            print(comp.ref, comp.reward, comp.userRank, sep=',')

    def download(self, name):
        files = self.api.competition_download_files(name)
        return files

if __name__ == '__main__':
    kaggle = KAGGLE()
    kaggle.search('all')
    kaggle.download('vinbigdata-chest-xray-abnormalities-detection')

