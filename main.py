from fastapi import FastAPI, HTTPException
from bs4 import BeautifulSoup
import requests

app = FastAPI()

@app.get("/")
async def fetch_pdf_links(url: str):
    try:
        # Fetching the webpage content
        response = requests.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail=f"Failed to retrieve webpage: {response.status_code}")

        # Parsing HTML content using BeautifulSoup
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        # Using regex to find all links ending with '.pdf'
        pdf_links = re.findall(r'href=[\'"]?([^\'" >]+.pdf)', html_content)

        return {"pdf_links": pdf_links}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
