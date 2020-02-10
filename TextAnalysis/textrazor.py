from textrazor import TextRazor

client = TextRazor("2f78eb712e4edc588ae00c248e8e4ffe0a499ef372f9043c0bc2e438", extractors=["entities"])
response = client.analyze("Barclays misled shareholders and the public about one of the biggest investments in the bank's history, a BBC Panorama investigation has found.")

for entity in response.entities():
	print entity