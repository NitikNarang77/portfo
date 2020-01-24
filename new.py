from flask import Flask,render_template,url_for,request,redirect
import csv
import operator

app = Flask(__name__)

@app.route('/')
def hello_world():

    return render_template('index.html')

@app.route('/<string:page_name>')
def hello(page_name):

    return render_template(page_name)

def write_to_file(data):
    with open('data.csv',mode='a') as database:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        csv_writer=csv.writer(database,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
        
        csv_writer.writerow([email,message,subject])

@app.route('/submit_form',methods=['GET','POST'])

def submit_form():
    if request.method=='POST':
        try:
            data=request.form.to_dict()
            write_to_file(data)
            return redirect('/thank you.html')
        except:
            return 'did not saved to database' 

    else:
        return 'something went wrong'       

if __name__ == '__main__':
    app.debug = True
    app.run()
