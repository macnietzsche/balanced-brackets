CLOSING_PAIRS={
    "(":")",
    "[":"]",
    "{":"}"
}

def getValueByIndex(arr,index):
    if index not in arr:
        return None
    return arr[index]

def getLastElement(arr):
    size=len(arr);
    if size<=0:
        return None
    return arr[size-1]

def isBalanced(exp):
    stack=[]
    for element in exp:
        closing=getValueByIndex(CLOSING_PAIRS,getLastElement(stack))
        if element==closing:
            stack.pop()
        elif element in CLOSING_PAIRS.values() and element!=closing:
            return False
        elif element in CLOSING_PAIRS or element in CLOSING_PAIRS.values():
            stack.append(element)
    return len(stack)==0

str="([{fghg}]){()}[]"
print(isBalanced(str))
    