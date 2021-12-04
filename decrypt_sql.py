#!/usr/bin/python

import base64
import sqlite3

def base(bascode):
    return base64.b64decode(bascode)


def first_decrypt(first_string):
    return first_string.replace("'", "z").replace("@", "Z").replace("^", "H").replace("#", "O").replace("!", "i").replace("%", "e")


def last_decrypt(last_string):
    return last_string.replace("@", "H").replace("#", "i").replace("$", "e").replace("%", "u").replace("^", "d").replace("&", "p")

conn = sqlite3.connect('data.sqlite')

print ("Opened database successfully");
cursor = conn.execute("SELECT id, codes, definition, causes from BMW")

for row in cursor:
    
   print ("id = ", row[0])
   print ("codes = ", row[1])
   base64_messaged =first_decrypt(row[2])
   dec = base(base64_messaged)
   print ("definition = ", dec)
   base64_messagedd = last_decrypt(row[3])
   decs = base(base64_messagedd)
   print ("causes = ", decs)
   conn.execute("UPDATE BMW set definition =?  where ID =? ", (dec,row[0]))
   conn.execute("UPDATE BMW set causes =?  where ID =? ", (decs, row[0]))
   conn.commit()


conn.close()


