from fastapi import FastAPI, jsonify
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI Quive Edition!"}


@app.route('/links', methods=['GET'])
def get_pdf_links():
    url = "https://dpsranchi.com/question_answer_paper.html"
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text
    else:
        return jsonify({"error": "Failed to retrieve webpage"}), 500

    soup = BeautifulSoup(html_content, 'html.parser')

    pdf_links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.endswith('.pdf'):
            pdf_links.append(href)

    return jsonify({"pdf_links": pdf_links})
