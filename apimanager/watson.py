from ibm_watson import ApiException
from gensim.summarization import summarize


class Watson:

	def extractSummary(self, content, api_call=False):
		summary = summarize(content)
		if api_call:
			try:
				return {'data':summary, 'success':True}
			except ApiException as ex:
				return {'message':ex.message, 'code':ex.code, 'success':False}

		return summary 
