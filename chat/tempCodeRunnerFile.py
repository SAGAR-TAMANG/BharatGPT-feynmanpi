def history_creator(history):
  print("\nHISTORY\n", history)
  

test_val =  [('Anonymous', 'Tell me about Aliens in 5 words.'), ('BharatGPT', 'Aliens refer to something that is out of ordinary'), ('Anonymous', 'tell me more')]
history_creator(test_val)

# output = [
#     parts {text: "text here"} role: "user",
#     parts {text: "text here"} role: "model",
#     parts { text: "text here" } role: "user"
#   ]

test_val = [{'text': text, 'role': 'user' if role == 'Anonymous' else 'model'} for role, text in test_val]

print(test_val)

test_val = [('Anonymous', 'text here'), ('BharatGPT', 'text here'), ('Anonymous', 'text here')]

output = []

for role, text in test_val:
    # Format the text and role into the desired format and append it to the output list
    if role == "Anonymous":
      role = 'user'
    else:
      role = 'model' 
    output.append(f'parts {{ text: "{text}" }} role: "{role}"')

print(output)

import re

text = []
count = 0 
for i in output:
  if count == 0:
    i = re.sub("parts", "[parts", i)
  count += 1
  text.append(i + ',')
  print(i + ',')


print(output)