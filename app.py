from flask import Flask,render_template
import math
app = Flask(__name__)
import mysql.connector
@app.route('/')
def index():
   mydb = mysql.connector.connect(
  host="ec2-15-206-77-23.ap-south-1.compute.amazonaws.com",
  user="root",
  passwd="admin123",
auth_plugin='mysql_native_password'
)
   mycursor = mydb.cursor()
   mycursor.execute("use bit")
   mycursor = mydb.cursor()
   mycursor.execute("SELECT * FROM Announcements order by id desc LIMIT 5")
   myresult = mycursor.fetchall()
   return render_template('index.html', annons=myresult,getDate=getDate)

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/placement')
def placement():
   return render_template('placement.html')

@app.route('/archive/<int:page>')
def archive(page):
   mydb = mysql.connector.connect(
  host="ec2-15-206-77-23.ap-south-1.compute.amazonaws.com",
  user="root",
  passwd="admin123",
auth_plugin='mysql_native_password'
)
   mycursor = mydb.cursor()
   mycursor.execute("use bit")
   mycursor = mydb.cursor()
   mycursor.execute("select count(*) from Announcements")
   myresult = mycursor.fetchall()
   count = myresult[0][0]
   pages = math.ceil(count/5)
   mycursor = mydb.cursor()
   mycursor.execute("SELECT * FROM Announcements order by id desc LIMIT "+str((page-1)*5)+",5")
   myresult = mycursor.fetchall()
   return render_template('archive.html',pages=pages,annons=myresult,page=page,getDate=getDate)

@app.route('/contact')
def contact():
   return render_template('contact.html')

@app.route('/announcement/<id>')
def announcement(id):
   mydb = mysql.connector.connect(
  host="ec2-15-206-77-23.ap-south-1.compute.amazonaws.com",
  user="root",
  passwd="admin123",
auth_plugin='mysql_native_password'
)
   mycursor = mydb.cursor()
   mycursor.execute("use bit")
   mycursor = mydb.cursor()
   mycursor.execute("SELECT * FROM Announcements where id="+id)
   myresult = mycursor.fetchall()[0]
   mycursor1 = mydb.cursor()
   mycursor1.execute("SELECT * FROM documents where id="+id)
   myresult1 = mycursor1.fetchall()
   return render_template('single-post.html',myresult=myresult, docs=myresult1)

@app.route('/videospost')
def videopost():
   return render_template('video-post.html')

@app.route('/department/<string:dept>')
def departmemt(dept):
   mydb = mysql.connector.connect(
  host="ec2-15-206-77-23.ap-south-1.compute.amazonaws.com",
  user="root",
  passwd="admin123",
auth_plugin='mysql_native_password'
)
   mycursor = mydb.cursor()
   mycursor.execute("use bit")
   mycursor = mydb.cursor()
   mycursor.execute("SELECT * FROM Faculty where Dept='%s'" %(dept))
   myresult = mycursor.fetchall()
   if(dept=="CSE"):
      return render_template("cse.html",facs=myresult)
   elif(dept=="ECE"):
      return render_template("ece.html",facs = myresult)
   elif(dept=="CV"):
      return render_template("cv.html",facs=myresult)
   elif(dept=="ME"):
      return render_template("me.html",facs = myresult)

def getDate(myDate):
    date_suffix = ["th", "st", "nd", "rd"]

    if myDate % 10 in [1, 2, 3] and myDate not in [11, 12, 13]:
        return date_suffix[myDate % 10]
    else:
        return date_suffix[0]


if __name__ == '__main__':
   app.run(debug=True)
   