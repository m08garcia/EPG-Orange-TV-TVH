#!/usr/bin/env python3
import requests
import urllib3
from datetime import datetime, timedelta
from xml.etree.ElementTree import Element, SubElement, tostring
from html import escape
import ssl
import sys
import gzip
import io
import re

CHANNEL_MAP = {
    '1010': 'La 1 HD',
    '1062': 'La 2 HD',
    '1011': 'Antena 3 HD',
    '1012': 'Cuatro HD',
    '1013': 'Telecinco HD',
    '1014': 'laSexta HD',
    '11001': 'STAR Channel',
    '11011': 'AMC',
    '11007': 'Warner TV',
    '11002': 'AXN',
    '11005': 'ComedyCentr',
    '11003': 'Calle 13',
    '12057': 'XTRM',
    '11004': 'SYFY',
    '11006': 'Cosmo',
    '11063': 'Enfamilia',
    '11045': 'SELEKT',
    '11093': 'Runtime Series',
    '1032': 'FDF',
    '1027': 'Neox',
    '1030': 'Energy',
    '1042': 'Atreseries',
    '1034': 'Divinity',
    '1028': 'Nova',
    '11010': 'C Hollywood',
    '11008': 'AXNMovies',
    '11029': 'Somos',
    '11012': 'TCM',
    '11052': 'Sundance TV',
    '11053': 'Dark',
    '1089': 'Runtime Cine y Series',
    '11091': 'Runtime Thriller/Terror',
    '11094': 'Runtime Acción',
    '11092': 'Runtime Comedia',
    '11095': 'Runtime Crimen',
    '11096': 'Runtime Romance',
    '11097': 'RunTime Clásico',
    '11098': 'Cines Verdi TV',
    '11099': 'Cine Feel Good',
    '12032': 'Paramount N',
    '1043': 'Be Mad TV',
    '11173': 'Squirrel TV',
    '11174': 'BOM Cine',
    '11182': 'RunTime Familia',
    '11019': 'C Historia',
    '11017': 'NatGeo',
    '11009': 'AMC BREAK',
    '11018': 'Odisea',
    '1039': 'Discovery',
    '1008': 'NatGeo Wild',
    '11042': 'AMC CRIME',
    '11151': 'Sangre Fría',
    '11020': 'CanalCocina',
    '11027': 'Decasa',
    '11112': '¡BUENVIAJE!',
    '1084': 'NatureTime',
    '11157': 'Love the Planet',
    '11156': 'Love Wine',
    '11154': 'Historia y Vida',
    '1016': 'Mega',
    '1018': 'DMAX',
    '12054': 'Ten ',
    '11016': 'Nick',
    '11015': 'DisneyJr',
    '11055': 'Nick JR',
    '11169': 'BabyTV',
    '1085': 'Dreamworks',
    '11100': 'Toon Goggles',
    '11176': 'Pocoyó',
    '1021': 'Boing',
    '1064': 'Clan HD',
    '1077': 'Gulli',
    '11168': 'SkyShowtime 1',
    '11035': 'Eurosport 1',
    '11059': 'Eurosport 2',
    '1063': 'TDP HD',
    '11190': 'M Liga de Campeones HDR',
    '11191': 'M Liga de Campeones HDR 2',
    '11030': 'M Copa del Rey',
    '11013': 'M LALIGATV',
    '11026': 'M LALIGATV 2',
    '1023': 'M Liga de Campeones',
    '1050': 'M Liga de Campeones 2',
    '1051': 'M Liga de Campeones 3',
    '1052': 'M Liga de Campeones 4',
    '11083': 'LALIGATV HYPERMOTION',
    '11084': 'LALIGATV HYPERMOTION 2',
    '11129': 'LALIGA Inside',
    '11120': 'Tennis Channel',
    '11121': 'MyPadel TV',
    '1095': 'Trace Sport Stars',
    '11175': 'Horse TV',
    '11128': 'Nautical Channel',
    '11104': 'Surf Channel',
    '11105': 'Motorvision',
    '11031': 'GOL PLAY',
    '12052': 'Real Madrid',
    '11178': 'Top Barça',
    '1019': 'Betis TV',
    '1033': 'Cazavisión',
    '12007': 'FightSports',
    '1091': 'Fight Box HD',
    '12006': 'Fast&FunBox',
    '1081': 'Moto ADV',
    '11050': 'MTV España',
    '1044': 'DKISS',
    '11102': 'Vivir con gatos',
    '11103': 'Vivir con perros',
    '11109': 'Inglés total - Multinivel',
    '11061': 'Ubeat',
    '1086': 'Gametoon',
    '11183': 'Anime Visión',
    '11184': 'Anime Visión Classics',
    '11051': 'MTV Live',
    '1026': 'MTV 00s',
    '1031': 'Mezzo HD',
    '11177': 'Flamenco Auditorio',
    '1088': 'Qwest TV',
    '11119': 'Sol Música',
    '11106': 'TRACE Latina',
    '11107': 'TRACE Urban',
    '12002': 'iConcerts',
    '11060': 'Festival 4K',
    '12003': 'Classica HD',
    '12005': 'MezzoLiveHD',
    '12004': 'Djazz',
    '1017': 'TR3CE',
    '11049': 'El Toro TV',
    '1068': 'EWTN',
    '1035': 'CanalSur ',
    '12050': 'TelemadridI',
    '1036': 'TV3CAT',
    '1038': 'Galicia TV',
    '1037': 'ETB Basque',
    '12051': '24 horas',
    '1090': 'Euronews',
    '11021': 'BBC WorldHD',
    '11022': 'CNN',
    '11075': '1+1 Marathon',
    '11025': 'Al Jazeera',
    '11024': 'Deutsche W',
    '11108': 'Bloomberg Originals',
    '11185': 'Negocios TV',
    '1029': 'Caracol TV',
    '11028': 'Pro TV',
    '11023': 'TV5MONDE',
    '1082': 'France 2',
    '1083': 'France 5',
    '1070': 'M6',
    '1057': 'M LALIGATV 3',
    '1058': 'M LALIGATV 4',
    '11085': 'LALIGATV HYPERMOTION 3',
    '1053': 'M Liga de Campeones 5',
    '1054': 'M Liga de Campeones 6',
    '1055': 'M Liga de Campeones 7',
    '1056': 'M Liga de Campeones 8',
    '11036': 'M Liga de Campeones 9',
    '1096': 'M Liga de Campeones 10',
    '1097': 'M Liga de Campeones 11',
    '1098': 'M Liga de Campeones 12',
    '1099': 'M Liga de Campeones 13',
    '50001': 'Prueba OTT '
}

class TLSAdapter(requests.adapters.HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        ctx = ssl.create_default_context()
        ctx.set_ciphers('DEFAULT@SECLEVEL=1')
        ctx.options |= 0x4
        kwargs['ssl_context'] = ctx
        return super().init_poolmanager(*args, **kwargs)

class OrangeEPG:
    def __init__(self):
        self.base_url = "https://epg.orangetv.orange.es/epg/Smartphone_Android/1_PRO/"
        self.image_base_url = "https://orangetv.orange.es/pc/api/rtv/v1/images/"
        self.session = requests.Session()
        self.session.mount('https://', TLSAdapter())
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
            'Referer': 'https://orangetv.orange.es/epg',
            'Accept': 'application/json'
        }

    def get_epg(self, days=5):
        epg_data = {}
        today = datetime.now()
        
        for day_offset in range(days):
            current_date = today + timedelta(days=day_offset)
            date_str = current_date.strftime("%Y%m%d")
            
            for segment in [1, 2, 3]:
                url = f"{self.base_url}{date_str}_8h_{segment}.json"
                try:
                    response = self.session.get(url, headers=self.headers, timeout=15)
                    response.raise_for_status()
                    self._process_response(response.json(), epg_data)
                except Exception as e:
                    print(f"Error: {str(e)}", file=sys.stderr)
        return epg_data

    def _process_response(self, data, epg_data):
        for channel in data:
            channel_id = channel['channelExternalId']
            if channel_id not in CHANNEL_MAP:
                continue
            epg_data.setdefault(channel_id, []).extend(channel['programs'])

    def generate_xmltv(self):
        tv = Element('tv')
        tv.set('generator-info-name', 'Orange TV EPG')
        tv.set('generator-info-url', 'https://orangetv.orange.es')
        
        for chan_id, name in CHANNEL_MAP.items():
            channel = SubElement(tv, 'channel', {'id': chan_id})
            SubElement(channel, 'display-name').text = name
            
        epg_data = self.get_epg()
        for chan_id, programs in epg_data.items():
            for program in programs:
                self._add_programme(tv, chan_id, program)
        
        return self._serialize_xml(tv)

    def _add_programme(self, parent, chan_id, program):
        programme = SubElement(parent, 'programme', {
            'start': self._format_time(program['startDate']),
            'stop': self._format_time(program['endDate']),
            'channel': chan_id
        })
        
        original_title = program.get('name', 'Sin título')
        season = episode = None

        match = re.search(r' - T(\d+), E0?(\d+)', original_title)
        if match:
            season, episode = map(int, match.groups())

        modified_title = re.sub(r'( - T\d+), E0?(\d+)', r'\1 E\2', original_title)
        
        SubElement(programme, 'title').text = escape(modified_title)
        SubElement(programme, 'desc').text = escape(program.get('description', ''))
        
        if season is not None and episode is not None:
            SubElement(programme, 'episode-num', {'system': 'onscreen'}).text = f"S{season} E{episode}"

        if 'attachments' in program:
            for attachment in program['attachments']:
                if attachment.get('name') == 'COVER':
                    image_path = attachment['value'].lstrip('/')
                    SubElement(programme, 'icon', {'src': f"{self.image_base_url}{image_path}"})

    def _format_time(self, timestamp):
        return datetime.utcfromtimestamp(timestamp/1000).strftime('%Y%m%d%H%M%S +0000')

    def _serialize_xml(self, tv_element):
        xml_header = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE tv SYSTEM "xmltv.dtd">\n'
        return xml_header + tostring(tv_element, encoding='unicode', short_empty_elements=False)

def main():
    urllib3.disable_warnings()
    
    if '-d' in sys.argv or '--description' in sys.argv:
        print("EPG Orange TV")
        return
    if '-v' in sys.argv or '--version' in sys.argv:
        print("6.1")
        return
    if '-c' in sys.argv or '--capabilities' in sys.argv:
        print("baseline")
        return

    epg = OrangeEPG()
    xml_content = epg.generate_xmltv()
    
    if '-z' in sys.argv or '--gzip' in sys.argv:
        with io.BytesIO() as buffer:
            with gzip.GzipFile(fileobj=buffer, mode='w') as f:
                f.write(xml_content.encode('utf-8'))
            sys.stdout.buffer.write(buffer.getvalue())
    else:
        print(xml_content)

if __name__ == "__main__":
    main()
