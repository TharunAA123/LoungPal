#import mysql
import mysql.connector as mys


class SqlConnector(object):
    
    sql_connection = None
    @staticmethod
    def get_connection():
        if not SqlConnector.sql_connection:
            
            SqlConnector.sql_connection = mys.connect(host='localhost',user='root',passwd='1234',
                                     database='LoungPalDB', auth_plugin='mysql_native_password')
       
          
        return SqlConnector.sql_connection

