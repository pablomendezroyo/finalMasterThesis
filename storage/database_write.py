import pandas as pd
import pymysql
import sshtunnel


host='database-smartcontract.cwi83idjai0q.eu-west-3.rds.amazonaws.com'
port=3306
db='database-smartcontract'
user='admin'
password='energysmart66'

with sshtunnel.SSHTunnelForwarder(
    ('ssh.pythonanywhere.com'),
    ssh_username='your PythonAnywhere username', ssh_password='the password you use to log in to the PythonAnywhere website',
    remote_bind_address=('your PythonAnywhere database hostname, eg. yourusername.mysql.pythonanywhere-services.com', 3306)
) as tunnel:
    connection = mysql.connector.connect(
        user='your PythonAnywhere username', password='your PythonAnywhere database password',
        host='127.0.0.1', port=tunnel.local_bind_port,
        database='your database name, eg yourusername$mydatabase',
    )
    # Do stuff
    connection.close()
