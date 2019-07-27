
def rW(Sentence): 
	words = Sentence.split(" ") 
	newWords = [word[::-1] for word in words] 
	newSentence = " ".join(newWords) 
	return newSentence 

S= input()
print(rW(S)) 
