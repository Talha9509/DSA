# collectString

def collectString(obj):
    newObj=obj
    result=[]
    for key in newObj:
        if type(newObj[key]) is str:
            result.append(newObj[key])
        elif type(newObj[key]) is dict:
            result=result+ collectString(newObj[key])
    return result

obj = {
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}
print(collectString(obj))