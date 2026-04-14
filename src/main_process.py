import json
import os
from cleaner import DataCleaner
from nlp_processor import NLPProcessor

def run_cleaning_pipeline():
    input_path='data/raw/raw_data.json'
    output_path='data/processed/clean_data.json'
    
    try:
        with open(input_path,'r',encoding='utf-8') as f:
            raw_data=json.load(f)
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file {input_path}")
        return
    
    cleaner=DataCleaner()
    clean_data=[]
    
    for item in raw_data:
        clean_data.append(cleaner.process_item(item))
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path,'w',encoding='utf-8') as f:
        json.dump(clean_data,f,ensure_ascii=False,indent=4)
        
def run_nlp_pipeline():
    input_path='data/processed/clean_data.json'
    output_path='data/processed/nlp_data.json'
    
    try:
        with open(input_path,'r',encoding='utf-8') as f:
            raw_data=json.load(f)
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file {input_path}")
        return
    
    nlp_processor=NLPProcessor('assets/vietnamese-stopwords.txt')
    
    for item in raw_data:
        nlp_description=nlp_processor.process_text(item.get('description_original',''))
        item['nlp_description']=nlp_description
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path,'w',encoding='utf-8') as f:
        json.dump(raw_data,f,ensure_ascii=False,indent=4)
        
def run_master_pipline():
    run_cleaning_pipeline()
    run_nlp_pipeline()
    
    
if __name__=="__main__":
    run_master_pipline()