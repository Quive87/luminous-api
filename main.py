from fastapi import FastAPI, HTTPException
from bs4 import BeautifulSoup
import requests

app = FastAPI()

@app.get("/")
async def fetch_pdf_links():
    url = "https://dpsranchi.com/question_answer_paper.html"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail=f"Failed to retrieve webpage: {response.status_code}")
        
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        
        pdf_links = []
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and href.endswith('.pdf'):
                pdf_links.append(href)
        
        return {"pdf_links": pdf_links}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
