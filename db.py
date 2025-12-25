import psycopg2
db_name= "TaskListDB"
db_user = "tasklistuser"
db_pw= "Mamta@123"
db_host= "localhost"

def getTaskList():
    con=psycopg2.connect(database=db_name,user=db_user,password=db_pw,host=db_host)
    cur=con.cursor()
    cur.execute(' select id,task_name, is_active from public."TaskList"')
    tasklist=cur.fetchall()
    con.commit()
    con.close()
    return tasklist

def addtask(taskname, due_date):
    executequery(' insert into public."TaskList"(task_name, due_date) values (%s, %s)', (taskname, due_date))

def updatetask(name,id):
    executequery(' update public."TaskList" set task_name=%s where id=%s', (name,id))

def deletetask(id):
    executequery(' delete from public."TaskList" where id=%s', (id))

def executequery(query,params=None):
    con=psycopg2.connect(database=db_name,user=db_user,password=db_pw,host=db_host)
    cur=con.cursor()
    cur.execute(query,params)
    con.commit()
    con.close()