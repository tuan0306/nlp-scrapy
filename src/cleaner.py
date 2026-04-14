import re
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s : %(message)s')

class DataCleaner:
    def __init__(self):
        self.amenity_keywords = {
            "Máy lạnh": ["máy lạnh", "điều hòa", "điều hoà", " ml ", " đh ", "aircon", " ac ", "a/c"],
            "Giờ giấc tự do": ["giờ giấc tự do", "tự do", "không chung chủ", "ko chung chủ", " kcc ", " ggtd ", "lối đi riêng", "chìa khóa riêng", "chìa khoá riêng", "24/24", "24/7", "đi sớm về khuya"],
            "An ninh": ["an ninh", "an toàn", "camera", "cctv", "bảo vệ", " bv ", "khóa vân tay", "khoá vân tay", "thẻ từ", "cửa cuốn", "dân trí cao"],
            "Sạch sẽ": ["sạch sẽ", "sạch đẹp", "mới tinh", "mới toanh", "mới cáu", "vệ sinh", "không ẩm mốc", "thoáng sạch", "sạch boong"],
            "Thoáng mát": ["thoáng mát", "mát mẻ", "nhiều ánh sáng", "đón gió", "view thoáng", "không bí", "sáng sủa", "view chill"],
            "Máy giặt": ["máy giặt", " mg ", "chỗ phơi", "sân phơi", "khu giặt", "giặt sấy", "máy sấy"],
            "Yên tĩnh": ["yên tĩnh", "không ồn", "cách âm", "an tĩnh", "văn minh", "yên ắng", "dân văn phòng"],
            "Cửa sổ": ["cửa sổ", " cs ", "ban công", "giếng trời", "ánh sáng tự nhiên", "view ngoài", "mặt tiền"],
            "Tủ lạnh": ["tủ lạnh", " tl ", "tủ mát"],
            "Siêu thị/Cửa hàng": ["siêu thị", "sthi", "cửa hàng tiện lợi", "minimart", "tạp hóa", "tạp hoá", "bách hóa xanh", " bhx ", "winmart", "vinmart", "coop", "circle k", "gs25", "family mart"],
            "Gần chợ": ["gần chợ", "kế chợ", "sát chợ", "cách chợ", "bước ra là chợ", "đi bộ ra chợ", "chợ dân sinh"],
            "Khóa vân tay/Thẻ từ": ["vân tay", "khóa vân tay", "khoá vân tay", "cổng vân tay", "cửa vân tay", "ra vào vân tay", "thẻ từ", "khóa từ", "khoá từ", "mã số", "smartlock", "khóa thông minh"],
            "Nước nóng": ["nước nóng", "máy nước nóng", "máy nn", "nóng lạnh", "bình nóng lạnh", "có nóng lạnh", "bình nl"],
            "Full nội thất": ["full nội thất", "full nt", "đầy đủ nội thất", "đầy đủ đồ", "full đồ", "xách vali", "trang bị đầy đủ", "bao trọn đồ"]
        }
    
    def clean_area(self,area_str):
        if not area_str: return None
        match=re.search(r'(\d+)',str(area_str))
        return float(match.group(1)) if match else None
    
    def clean_price(self,price_str):
        if not price_str: return None
        price_cleaned=re.sub(r'[^\d]','',str(price_str))
        return float(price_cleaned) if price_cleaned else None
    
    def extract_amenities(self,description):
        if not description : return []
        found_amenities=[]
        desc_lower=description.lower()
        for standard_name, keywords in self.amenity_keywords.items():
            if any(kw in desc_lower for kw in keywords):
                found_amenities.append(standard_name)
        return found_amenities
    
    def extract_district(self,address):
        if not address: return None
        parts=address.split(',')
        for part in parts:
            part=part.strip()
            if 'Quận' in part or 'Huyện' in part:
                return part
        return None
    
    def process_item(self,raw_item):
        desc=raw_item.get('description')
        
        return {
            'title':raw_item.get('title'),
            'area':self.clean_area(raw_item.get('area')),
            'price':self.clean_area(raw_item.get('price')),
            'telephone':raw_item.get('telephone'),
            'district':self.extract_district(raw_item.get('address')),
            'address':raw_item.get('address'),
            'amenities':self.extract_amenities(raw_item.get('description')),
            'url':raw_item.get('url'),
            'description_original':raw_item.get('description')
        }