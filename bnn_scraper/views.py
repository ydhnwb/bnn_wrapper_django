from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import *
from .models import *
from . import constants
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class StatisticViewSet(viewsets.ViewSet):
    #test
    serializer_class = StatisticSerializer

    def init_driver(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--disable-dev-shm-usage')
        self.chrome_options.binary_location = constants.GOOGLE_CHROME_PATH
        self.driver = webdriver.Chrome(executable_path=constants.CHROMEDRIVER_PATH, chrome_options= self.chrome_options)
        return self.driver

    def scan(self, url):
        self.init_driver()
        global temp
        for u in constants.bnn_links:
            if u.get('url') == url:
                temp = u
                break

        print("Current province {0}".format(temp))
        return temp.get('url')



    def get_stats(self, url):
        global stats
        print("Getting statistic from {0}".format(url))
        self.driver.get(url)
        rows = self.driver.find_elements_by_class_name("numberrowKetujuh")
        stats = Statistic(total_kasus=str(rows[0].text), total_tersangka=str(rows[1].text),
                          total_pasien_penyalahgunaan=str(rows[2].text),
                          jumlah_penggiat_anti_narkoba=str(rows[3].text),
                          jumlah_sebaran_informasi=str(rows[4].text))

        print(stats)
        return stats

    def create(self, request):
        url = request.data.get('url')
        print(url)
        url_available = self.scan(url)
        if url_available is not None:
            stat = self.get_stats(url_available)
            if stat is not None:
                print("Asoy")
                serializer = StatisticSerializer(stats, many=False)
                print(serializer.data)
                return Response({'status': True, 'data': serializer.data})
            else:
                return Response({'status': True, 'data': {}})

        else:
            return Response({'message':'Url not valid','status':False, 'data':{}})


    @action(detail=False, methods=['post'])
    def filter(self, request):
        return Response({'status':True, 'data': 'Contoh'})


class ProvinceViewSet(viewsets.ViewSet):
    serializer_class = ProvinceSerializer

    def list(self, request):
        provinces = ProvinceSerializer(constants.bnn_links, many=True)
        return Response({'status': True, 'data': provinces.data})