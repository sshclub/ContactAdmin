"""
main executable Moduel
"""
from model.contact import  Contact
import service.contact_service as svc
#def _init_contact():
#    f = open("contact.dat","w")
#    f.close()

import sqlite3
def main():
#    _init_contact()
    "주소 객체 생성"
###

    create_table_query = 'create table contact (name text, hpnum text,email text,age int);'
    insert_query = "insert into contact values(?,?,?,?)"
    #1 establish connction
    con = sqlite3.connect('connect.db')
    #2 get cusor from the db
    cur = con.cursor()
    #3 send SQL iin the db from cusor
    #cur.execute((create_table_query))
    cur.execute(insert_query, ('kim', '010-1234-5678','kim@naver.com', 20))
    cur.execute('select * from contact')
    a_record = cur.fetchone()
    print(a_record)
    print('table created')
    #4 transaction
    con.commit()
    #5 release resource
    con.close()

"""
    c = Contact('song','010-1234-5841','song@naver.com','asan')
    svc.regist_contact(c)

    print("주소 등록 성공")

    list = svc.view_all_contact()
    print(list)
"""
if __name__  == "__main__":
    main()

