import openai

openai.api_key = open("D:\\frigdrivers\\pass\\key.txt").readline()
resp = openai.Completion.create(
     prompt= "Ethan Kilgore Hadley, usually" ,
     engine="text-davinci-002",
     max_tokens=300,
     top_p=1,
     frequency_penalty=0,
     presence_penalty=0)
     
print(resp)