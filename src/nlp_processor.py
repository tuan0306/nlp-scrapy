import re
from underthesea import word_tokenize

class NLPProcessor:
    def __init__(self,stopwords_path):
        self.stopwords=set()
        self.load_stopwords(stopwords_path)
        self.clean_regex=re.compile(r'[^\w\s]')
        
    def load_stopwords(self,stopwords_path):
        try:
            with open(stopwords_path,'r',encoding='utf-8') as f:
                self.stopwords=set(line.strip() for line in f if line.strip())
        except FileNotFoundError:
            print(f"Không tìm thấy file {stopwords_path}")
            
    def clean_text(self,text):
        if not text: return ""
        text_lower=text.lower()
        text_clean=self.clean_regex.sub(' ',text_lower)
        return text_clean
    
    def process_text(self,text):
        cleaned_text=self.clean_text(text)
        tokenized_text=word_tokenize(cleaned_text,format="text")
        words=tokenized_text.split()
        filtered_words=[word for word in words if word not in self.stopwords]
        return " ".join(filtered_words)   