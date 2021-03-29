from boilerpy3 import extractors
import requests


def if_403_error(url, extractor):

  headers = {
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko)'
      'Chrome/50.0.2661.102 Safari/537.36'}

  resp = requests.get(url, headers=headers)
  if resp.ok:
      doc = extractor.get_doc(resp.text)
      return doc

  else:
      raise Exception(f'Failed to get URL: {resp.status_code}')


def get_text_from_url(url):
  response = {}
  try:
    extractor = extractors.ArticleExtractor()
    doc = extractor.get_doc_from_url(url)
    response = {'title': doc.title, 'content': doc.content,
                'success': True, 'error': None}

  except Exception as e:
    if e.code == 403:
      doc = if_403_error(url, extractor)
      response = {'title': doc.title, 'content': doc.content,
                  'success': True, 'error': None}

  return response
