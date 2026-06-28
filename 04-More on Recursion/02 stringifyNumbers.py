# Stringify

def stringify(obj):
    newObj=obj
    for key in newObj:
        if type(newObj[key]) is int:
            newObj[key]=str(newObj[key])
        if type(newObj[key]) is dict:
            newObj[key]=stringify(newObj[key])
    return newObj

obj = {
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}
print(stringify(obj))