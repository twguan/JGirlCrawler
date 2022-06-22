import pandas as pd

def combine(excel:pd.DataFrame, html, test_name):
    # get the table from .html
    table = pd.read_html(html)
    df = pd.DataFrame(table[1])
    # pick 'Avg' as score
    df2 = pd.DataFrame(df[['User','Avg']])
    score = pd.DataFrame()

    # check if the student still on list
    for i in df2.index:
        id = df2.at[i, 'User'][:9] if len(df2.at[i, 'User']) >= 9 else ''
        
        if id in excel['ID'].values:
            score = pd.concat([score, df2[i:i+1]], ignore_index=True)
        excel.reset_index(inplace=True, drop=True)

    excel = excel.join(score['Avg'])
    excel.rename(columns={'Avg':test_name}, inplace=True)
    return excel

def make_score(excel, htmls, test_name):
    for i in range(5):
        excel = combine(excel, htmls[i], test_name[i])
        
    return excel
    



# judge girl scoreboard .html
hw1 = './HW1.html'
hw2 = './HW2.html'
hw3 = './HW3.html'
hw4 = './HW4.html'
final = './Final.html'

excel_path = './123.xlsx'
save_path = './score.xlsx'

htmls = [hw1, hw2, hw3, hw4, final]
test_name = ['Hw1', 'Hw2', 'Hw3', 'Hw4', 'Final']

excel = pd.read_excel(excel_path, usecols='A,C')
# capturt from student name
excel = excel[2:].rename(columns={'SIS Login ID':'ID'})

for i in excel.index:
    excel.at[i, 'ID'] = excel.at[i, 'ID'][:9]
excel = make_score(excel, htmls, test_name)
excel.set_index('Student', inplace=True)

# demo .xlsx on std output
print(excel)
excel.to_excel(save_path)
