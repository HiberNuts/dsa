from flask import Flask, redirect, url_for, request
app = Flask(__name__)

d={
    '69.162.81.155':'01-23-45-67-89-AB',
    '192.199.248.75':'2c-54-91-88-c9-e3'
}
@app.route('/success/')
def sucess():    
        return 'New ip \'s mac address is added successfully ' 
@app.route('/create',methods=['POST','GET'])
def create():
    if request.method == 'POST':
        macaddr=request.form['mac']
        ipa=request.form['ip']
        dic[ipa]=macaddr
        return redirect(url_for('success'))
    else:
        user = request.args.get('mac')
        ipaddr=request.form['ip']
        return redirect(url_for('success'))   

@app.route('/success/<ip>')
def success(ip):
   return 'mac address is %s' % d[ip]

@app.route('/check',methods = ['POST', 'GET'])
def check():
   if request.method == 'POST':
      ip = request.form['ipa']
      if ip not in d:
        # return '/create.html'
        return '<html><body>		<form action = "http://localhost:5000/create" method = "post"><p>    Your ip address doesnot exist</p><p>Enter ip address: </p> <p><input type = "text" name = "ipa" /></p>	 <p>Enter mac address corresponding to your ip address: </p>	<p><input type = "text" name = "mac" /></p>	<p><input type = "submit" value = "submit" /></p>	</form>	</body></html>'
      return redirect(url_for('success',ip=ip))
   else:
      user = request.args.get('ip')
      return redirect(url_for('success',ip=ip))

if __name__ == '__main__':
   app.run(debug = True)