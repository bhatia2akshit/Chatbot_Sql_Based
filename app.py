
from flask import Flask, render_template, request
import openai
import pandas as pd
from pandasql import sqldf

openai.api_key = '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'
app = Flask(__name__)
app.static_folder = 'static'

def chatbot_response(question):
    prompt = '''
    ### Postgres SQL tables, with their properties:
    #
    # df(indicator,period,source,location,value,value_type,Sub-dashboard)
    #
    '''

    prompt += '### '+question+'\nSelect'

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=['#', ';']
    )

    if len(response['choices'])<1:
        print("Sorry, I am facing some problem. Maybe internet is down or maybe the openAI is not responding.")

    if response['choices'][0]['text'] == '':
        return "Sorry, I couldn't find a response."
    sql='Select '+response['choices'][0]['text'].strip()
    print(f'the sql query obtained is: {sql}....')
    return sql

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/load_data", methods = ['GET', 'POST'])
def load_csv():
    if request.method == 'POST':
        csvfile=request.files['csvLoad']
        global df
        df = pd.read_csv(csvfile)
        print('file is loaded')
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    sql_query = chatbot_response(userText)
    pysqldf = lambda q: sqldf(q, globals())
    response_df = pysqldf(sql_query)
    print(response_df)
    keys = response_df.keys()
    output = 'According to me, the '
    arr_output = []
    for key in keys:
        if len(response_df[key].values) > 1:
            values = []
            for value in response_df[key].values:
                values.append(str(value))
            values_str = ', '.join(values)
            arr_output.append(f'the number of {key} is {len(values)} and they are {values_str}')
        else:
            values = response_df[key].values[0]
            arr_output.append(f'{key} is {values}')

    arr_ = ' and '.join(arr_output)
    output += arr_
    output.strip()
    return output

if __name__ == "__main__":
    app.run()