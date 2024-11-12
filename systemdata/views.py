from django.shortcuts import render
from django.http import HttpResponse
import os
from datetime import datetime
import subprocess
import getpass
import pytz

def htop(request):
    full_name = "Ananya A S" 
    system_username = getpass.getuser()
    
    # Set the time zone to IST (Indian Standard Time)
    timezone = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S IST")
    
    # Get the output of the 'top' command
    top_output = subprocess.getoutput('top -n 1 -b')
    
    # Generate HTML content
    html_content = f'''
    <html>
        <body>
            <h1>System Info</h1>
            <p>Name: {full_name}</p>
            <p>Username: {system_username}</p>
            <p>Server Time (IST): {server_time}</p>
            <pre>{top_output}</pre>
        </body>
    </html>
    '''
    
    return HttpResponse(html_content)
