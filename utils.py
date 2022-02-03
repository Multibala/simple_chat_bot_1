


from sklearn.feature_extraction.text import CountVectorizer

from sklearn.metrics.pairwise import cosine_similarity





def index_sort(list_var):
  length = len(list_var)
  list_index = list(range(0,length))
  x = list_var
  for i in range(length):
    for j in range(length):
      if x[list_index[i]]>x[list_index[j]]:
        list_index[i],list_index[j] = list_index[j],list_index[i]
  return list_index

def bot_response(user_input,sentence_list,bot_responses):
  user_input = user_input.lower()
  sentence_list.append(user_input)
  bot_response = ''
  cm = CountVectorizer().fit_transform(sentence_list)
  similarity_scores = cosine_similarity(cm[-1],cm)
  similarity_scores_list = similarity_scores.flatten()
  index = index_sort(similarity_scores_list)
  index = index[1:]
  if similarity_scores_list[index[0]]>0.0:
    bot_response = bot_responses[index[0]]
  else:
    bot_response = 'i apologize , I dont understand ..'
  sentence_list.remove(user_input)
  return bot_response


