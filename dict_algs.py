ivan = {
"name" : "ivan" ,
"age" : 34 ,
"children" : [{
"name" : "vasja" ,
"age" : 12 ,
}, {
"name" : "petja" ,
"age" : 10 ,
}],
}

slava = {
"name" : "slava" ,
"age" : 51 ,
"children" : [{
"name" : "olga" ,
"age" : 19 ,
}, {
"name" : "masha" ,
"age" : 21 ,
}],
}

darja = {
"name" : "darja" ,
"age" : 41 ,
"children" : [{
"name" : "kirill" ,
"age" : 21 ,
}, {
"name" : "pavel" ,
"age" : 15 ,
}],
}

emps = [ ivan , darja,slava]
def older_18 (emps):
 bool_ch = 0
 print("Сотрудники, имеющие детей старше 18-ти лет:")
 for people in emps:
     for child in people.get("children"):
         if child.get("age")>15:
           bool_ch = 1
           break
     if bool_ch == 1:
      print(people.get("name"))
      bool_ch=0

older_18 (emps)