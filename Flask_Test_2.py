# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 16:54:38 2020

@author: Kenneth
"""


from flask import Flask 
app = Flask(__name__) 
  
@app.route('/hello/<name>') 
def hello_name(name): 
   return 'Hello %s!' % name 
  
if __name__ == '__main__': 
   app.run() 