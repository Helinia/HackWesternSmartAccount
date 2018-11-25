import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import random
import csv
def bankextract():
	with open('/Users/lawrence/Desktop/test/test2.csv', 'r') as csvfile:
		Bank= []
		AccountType = []
		AccountName = []
		MonthFee = []
		MiniBalance = []
		TransNum = []
		emt = []
		interestR = []
		interestR2 = []
		i = 0 
		reader = csv.reader(csvfile)
		for row in reader:
			if row[1] == "Savings":
				Bank.append(row[0])
				AccountType.append(row[1])
				AccountName.append(row[2])
				MonthFee.append(row[3])
				MiniBalance.append(row[4])
				TransNum.append(row[5])
				emt.append(row[6])
				interestR.append(row[7])
				interestR2.append(float(row[7].replace('%',''))*0.01)
		csvfile.close()
		return {'Bank':Bank, 'AccountType':AccountType, 'AccountName':AccountName, 'MonthFee':MonthFee, 
			'MiniBalance': MiniBalance, 'TransNum':TransNum, 'emt':emt, 'interestR':interestR, 'interestR2': interestR2
			}

def dataextract():
	with open('/Users/lawrence/Desktop/test/test1.csv', 'r') as csvfile:
		date = []
		balance = []
		reader = csv.reader(csvfile)
		for row in reader:
			try:
				date.append(row[0])
				balance.append(float(row[-1]))
			except:
				pass
		csvfile.close()
		return {'date':date, 'balance':balance}

def interest():
	with open('/Users/lawrence/Desktop/test/test2.csv', 'r') as csvfile:
		date = []
		balance = []
		reader = csv.reader(csvfile)
		print (reader)
		for row in reader:
			print (row)
			date.append(row[0])
			balance.append(float(row[-1]))
		csvfile.close()
		return {'date':date, 'balance':balance}

def third(bankinfo):
	pre = bankinfo['interestR2']
	lis = []
	temp = max(pre)
	lis.append(max(pre))
	pre.remove(temp)
	
	temp = max(pre)
	lis.append(max(pre))
	pre.remove(temp)

	temp = max(pre)
	lis.append(max(pre))
	pre.remove(temp)

	







rawdata = dataextract()
bankinfo = bankextract()

app = dash.Dash()
app.layout = html.Div([
	html.Div([
		dcc.Graph(
			id = 'example-graph',
			figure={
				'data':[
					{'x':rawdata['date'],'y':rawdata['balance']},
					],
				'layout':{
					'title': "Bank Statements"
					}
				}
			)
		], className="six columns"),



	html.Div([
 		dcc.Graph(
			figure=go.Figure(
				data=[ 
					go.Bar(x = bankinfo['AccountName'], 
						y = bankinfo['interestR'],
						marker=go.bar.Marker(color='rgb(26, 118, 255)')
							)
						]		
					)
				)
		], className="six columns"),

	html.Div([
		dcc.Graph(
    		figure=go.Figure(
        		data=[
            	go.Bar(
                	x=[1996, 1997, 1998],
                	y=[12,3,4],
                	name='Rest of world',
                	marker=go.bar.Marker(
                    color='rgb(55, 83, 109)'
                    )
                 ),
            	]
            	)
    		)], className="six columns"),
	], className="row")








app.css.append_css({
	'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
	app.run_server(debug=True)