import pandas as pd
import json

##fyst er det innholdet til indivuelle chatter
## etter dette så er det 

with open('data/json/chat_history.json', encoding='utf-8') as f:
    data = json.load(f)
i = 0

## Iterates through the chats and messages
for chat in data.keys():
    df = pd.DataFrame(['From', 'Created', 'Content', 'Conversation Title', 'IsSender'])
    entry = data[chat]
    for message in entry:
        df = df._append(
            {
                'From': message['From'],
                'Created': message['Created'],
                'Content': message['Content'],
                'Conversation Title': message['Conversation Title'],
                'IsSender': message['IsSender'],
            },
            ignore_index=True
        )
        print('Added message from ', message['From'], ' message number ', i)
        i += 1
    df.to_csv('csv_data/' + chat + '.csv', index=False)
    

print ('Added ', i, ' messages to the csv file')





## Shows available chats in the data
print(data.keys())
## Shows message keys
known_user = 'username'
print(data[known_user][0].keys())