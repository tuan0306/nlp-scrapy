import urllib.request
import os

def download_vn_stopwords():
    url = "https://raw.githubusercontent.com/stopwords/vietnamese-stopwords/master/vietnamese-stopwords.txt"
    
    folder_path='assets'
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, "vietnamese-stopwords.txt")
    
    try:
        urllib.request.urlretrieve(url,file_path)
        
    except Exception as e:
        print(f"Lỗi khi tải file: {e}")
        
if __name__=="__main__":
    download_vn_stopwords()