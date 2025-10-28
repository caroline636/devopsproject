import io
import pdfplumber
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def extract_text_from_pdf(file_stream):
    text = ""
    with pdfplumber.open(file_stream) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text() or ""
            text += "\n" + page_text
    return text


def clean_text(t):
    if not t:
        return ""
    t = t.replace("\n", " ")
    t = re.sub(r"\s+", " ", t)
    return t.strip().lower()


def score_resume_against_jd(resume_text, job_description, top_k_matches=10):
    docs = [clean_text(resume_text), clean_text(job_description)]
    vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
    tfidf = vectorizer.fit_transform(docs)
    sim = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]  # scalar between 0 and 1
    # compute top matching terms by looking at high tf-idf in resume that appear in JD
    jd_terms = set(vectorizer.inverse_transform(tfidf[1])[0])
    resume_terms = vectorizer.inverse_transform(tfidf[0])[0]
    matches = [str(t) for t in resume_terms if t in jd_terms]
    # unique and take top_k
    matches = list(dict.fromkeys(matches))[:top_k_matches]
    return float(sim), matches
