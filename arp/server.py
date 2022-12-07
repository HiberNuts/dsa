from flask import Flask, redirect, url_for, request
app = Flask(__name__)
dic={
    '69.162.81.155':'01-23-45-67-89-AB',
    '192.199.248.75':'2c-54-91-88-c9-e3'
}
ipaddr='123'
@app.route('/result/<name><mac>')
def result(name,mac):    
        return 'Mac address of %s is %s' % name % mac

@app.route('/success/<name><ip>')
def sucess(name,ip):    
        return 'hi %s . New ip %s \'s mac address is added successfully ' % name % ip
   
@app.route('/create',methods=['POST','GET'])
def create():
    if request.method == 'POST':
        macaddr=request.form['mac']
        dic[ipaddr]=macaddr
        return redirect(url_for('success',name=user,ip=ipaddr))
    else:
        user = request.args.get('mac')
        ipaddr=request.form['ip']
        return redirect(url_for('success', name=user,ip=ipaddr))    



@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        ipaddr=request.form['ip']
        if ipaddr in dic:
            temp=dic[ipaddr]
            return redirect(url_for('result',name=user,mac=temp))
        else: 
            return redirect(url_for('create'))
    else:
        user = request.args.get('nm')
        ipaddr=request.form['ip']
        return redirect(url_for('login', name=user,ip=ipaddr))


if __name__ == '__main__':
	app.run(debug=True)
