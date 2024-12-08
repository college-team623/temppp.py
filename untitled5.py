
from http.server import BaseHTTPRequestHandler, HTTPServer
import pyodbc

# Database connection parameters
server = 'LAPTOP-O9NAVCSL'
database = 'school'
username = 'your_username'  # Replace with your username if needed
password = 'your_password'  # Replace with your password if needed

# Connection string for SQL Server
conn_str = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Connect to the database
            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()

            # Execute the query
            cursor.execute("SELECT * FROM students")
            rows = cursor.fetchall()

            # Generate HTML content for the response with CSS styling
            html_content = """
            <html>
            <head>
                <title>Students List</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        background-color: #B3D9FF; /* Baby blue background */
                        margin: 20px;
                        padding: 20px;
                        display: flex;
                        justify-content: center;
                        flex-direction: column;
                        align-items: center;
                        box-sizing: border-box;
                    }
                    h1 {
                        color: #333;
                        margin-bottom: 20px;
                    }
                    table {
                        width: 100%;
                        max-width: 1000px;
                        border-collapse: collapse;
                        margin: 20px 0;
                        background-color: #fff;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    }
                    th, td {
                        padding: 10px;
                        border: 1px solid #ddd;
                        text-align: center;
                    }
                    th {
                        background-color: #4CAF50;
                        color: white;
                    }
                    tr:nth-child(even) {
                        background-color: #f2f2f2;
                    }
                    tr:hover {
                        background-color: #f1f1f1;
                    }
                    @media (max-width: 768px) {
                        table {
                            width: 100%;
                            font-size: 14px;
                        }
                        th, td {
                            padding: 8px;
                        }
                    }
                </style>
            </head>
            <body>
                <h1>Students List</h1>
                <table>
                    <tr>
            """

            # Add column headers (assumes the first row contains column names)
            columns = [column[0] for column in cursor.description]
            for col in columns:
                html_content += f"<th>{col}</th>"
            html_content += "</tr>"

            # Add rows of data
            for row in rows:
                html_content += "<tr>"
                for column in row:
                    html_content += f"<td>{column}</td>"
                html_content += "</tr>"

            html_content += """
                    </table>
                </body>
            </html>
            """

            # Send HTTP response header
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Send the HTML content
            self.wfile.write(html_content.encode('utf-8'))

            # Close the cursor and connection
            cursor.close()
            conn.close()

        except Exception as e:
            # Handle any connection or query errors
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            error_message = f"<html><body><h1>Error:</h1><p>{e}</p></body></html>"
            self.wfile.write(error_message.encode('utf-8'))

# Run the server on port 8080
server_address = ('', 8080)
httpd = HTTPServer(server_address, RequestHandler)
print("Server running on http://localhost:8080")
httpd.serve_forever()
from http.server import BaseHTTPRequestHandler, HTTPServer
import pyodbc

# Database connection parameters
server = 'LAPTOP-O9NAVCSL'
database = 'school'
username = 'your_username'  # Replace with your username if needed
password = 'your_password'  # Replace with your password if needed

# Connection string for SQL Server
conn_str = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Connect to the database
            conn = pyodbc.connect(conn_str)
            cursor = conn.cursor()

            # Execute the query
            cursor.execute("SELECT * FROM students")
            rows = cursor.fetchall()

            # Generate HTML content for the response
            html_content = "<html><head><title>Students List</title></head><body>"
            html_content += "<h1>Students List</h1>"
            html_content += "<table border='1'><tr>"

            # Add column headers (assumes the first row contains column names)
            columns = [column[0] for column in cursor.description]
            for col in columns:
                html_content += f"<th>{col}</th>"
            html_content += "</tr>"

            # Add rows of data
            for row in rows:
                html_content += "<tr>"
                for column in row:
                    html_content += f"<td>{column}</td>"
                html_content += "</tr>"

            html_content += "</table></body></html>"

            # Send HTTP response header
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Send the HTML content
            self.wfile.write(html_content.encode('utf-8'))

            # Close the cursor and connection
            cursor.close()
            conn.close()

        except Exception as e:
            # Handle any connection or query errors
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            error_message = f"<html><body><h1>Error:</h1><p>{e}</p></body></html>"
            self.wfile.write(error_message.encode('utf-8'))

# Run the server on port 8080
server_address = ('', 8080)
httpd = HTTPServer(server_address, RequestHandler)
print("Server running on http://localhost:8080")
httpd.serve_forever()







