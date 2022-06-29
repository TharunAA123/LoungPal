from PyQt5.QtCore import QObject

from model import sql_queries

from model.sql_connector import SqlConnector




class SqlOperations():

    def login_request(self, user_id, password) -> str:
        sql_connection = SqlConnector.get_connection()
        cursor = sql_connection.cursor()
        cursor.execute(sql_queries.USER_AUTHENTICATION_QUERY, (user_id, password))
        record = cursor.fetchone()

        if record:
            valid_user=True
            msg = "Welcome: " + record[0]
        else:
            valid_user=False
            msg = "User unidentified. Please signup"

        cursor.close()

        return valid_user,msg
    
    
    def signup(self, username, user_id, password) -> str:
        sql_connection = SqlConnector.get_connection()
        cursor = sql_connection.cursor()
        cursor.execute(sql_queries.USER_CHECK_QUERY,(user_id,))
        record = cursor.fetchone()
        
        
        if record:
            #valid_user=True
            msg = "User exists. Please login"
            print(msg)
            cursor.close()
        else:
            #valid_user=False
            msg="Welcome new user. Please login now"
            print(msg)
            cursor.close()
            cursor = sql_connection.cursor()
            cursor.execute(sql_queries.USER_SIGNUP_QUERY, (username, user_id, password))
            sql_connection.commit()
            cursor.close()
            
        return msg
    
    
    def get_all_locations(self):

        sql_connection = SqlConnector.get_connection()
        cursor = sql_connection.cursor()
        cursor.execute(sql_queries.ALL_LOCATIONS_QUERY)
        # [(0, 0, KFC), (1,0, BK),....]
        records = cursor.fetchall()
        
        location_dict={}
        
        for record in records:
            
            hori = int(record[0])
            vert = int(record[1])
            service_name = record[2]
            unique_no = record[3]
            service_no = record[4]
            location_dict[(hori, vert)] = (service_name,unique_no,service_no)
            
            

        cursor.close()

        return location_dict
    
    def get_route(self, source, dest):
        
        sql_connection = SqlConnector.get_connection()
        cursor = sql_connection.cursor()
        cursor.execute(sql_queries.ROUTE_QUERY, (source, dest))
        record = cursor.fetchone()
        
        if record:
            
            return record[0].split("-")
        
        
        
