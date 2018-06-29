condition=True

def sumOfPrimes(m):
    total=0
    for i in range(1,m):                    # +1
        restart = False     
        for j in range(2,i):                # +2
            if i%j==0:                      # +3
                restart = True
                break
        if restart:                         # +2
            continue
        total+=i
    return total                            # Cognitive Complexity=8

    
def getWords(number):
    if number==1:                           # +1
        return 'one'
    elif number==2:                         # +1
        return 'a couple'
    elif number==3:                         # +1
        return 'a few'
    else:                                   # +1
        return 'lots'                       # Cognitive Complexity = 4
                                
def switch_demo(argument):
    switcher = {
        1: "one",
        2: "a couple",
        3: "a few"       
    }
    print (switcher.get(argument, "lots"))  # Cognitive Complexity=0    


def a_decorator(a, b):    
    def inner(func):                        # nesting = 0
        if condition:                       # +1
            print(b)
        func()
    return inner                            # Cognitive Complexity = 1

 
def not_a_decorator(a, b):
    condition=True
    def inner(func):                        # nesting = 1
        if condition:                       # +1 structure, +1 nesting
            print(b)
        func()
    return inner                            # Cognitive Complexity = 2


def decorator_generator(a):
    def generator(func):
        def decorator(func):                # nesting = 0
            if condition:                   # +1
                print()
            return func()
        return decorator
    return generator                        # Cognitive Complexity = 1

def my_method():
    condition2=False
    try:
        if condition:                       # +1
            for i in range(0,10):           # +2 (nesting=1)
                while(condition2):          # +3 (nesting=2)
                    print(i)                 
    except Exception as e:                  # +1
        if condition2:                      # +2
            print(e)                        # Cognitive Complexity 9
            
            
def myMethod2():
    def r ():                               # +0 (but nesting level is now 1)
        if (condition):                     # +2 (nesting=1)
            print()                         # Cognitive Complexity = 2
            

def logical_operators_easy():
    a=b=c=d=False
    return a and b and c and d

def logical_operators_hard():
    a=b=c=d=False
    return a or b and c or d

def logical_operators_hard_2():
    a=b=c=d=e=f=False
    if (a and b and c) or (d or e) and f:   # +1 if  +1 and b and c  +1 or d or e  +1 and f  
        print()                             # Cognitive Complexity = 4

def logical_operators_not():
    a=b=c=False                             # +1 if  +1 and  +1 not(b and c)
    if a and not(b and c):                  # Cognitive Complexity = 3
        print()
      
def overridenSymbolFrom(classType,name):
    if classType.isUnknow():                                    # +1
        return None
    
    unk=False
    symbols=classType.getSymbol().members().lookup(name)  
    for os in symbols:                                          # +1
        if os.isKind("JavaSymbol") and not os.isStatic():       # +2 (nesting = 1)
            method=os                                           # +1
            if canOverride(method):                             # +3 (nesting = 2)
                overriding=checkParameters(method,classType)
                if overriding is None:                          # +4 (nesting = 3)
                    if not unk:                                 # +5 (nesting =5)
                        unk=True
                elif overriding:                                # +1
                    return method
    if unk:                                                     # +1    
        return None
    return None
                                                                # Cognitive Complexity = 19

 
def addVersion(entry,txn):
    ti = _persistit.getTransactionIndex()
    while True:                                                         # +1
        try:
            with lock:
                if frst != None:                                        # +2 (nesting = 1)
                    if frst.getVersion() > entry.getVersion():          # +3 (nesting = 2)
                        raise RollbackException()

                    if txn.isActive():                                  # +3 (nesting = 2)
                        for e in e.getPrevious() :                      # +4 (nesting = 3)
                            version = e.getVersion()
                            depends = ti.wwDependency(version,txn.getTransactionStatus(), 0)
                            if depends == TIMED_OUT:                    # +5 (nesting = 4)
                                raise WWRetryException(version)
                            if depends != 0 and depends != ABORTED:     # +5 (nesting = 4) +1
                                raise RollbackException()
                entry.setPrevious(frst)
                frst = entry
                break
        except WWRetryException as e:                                   # +2 (nesting = 1)
            try:
                depends = _persistit.getTransactionIndex().wwDependency(re.getVersionHandle(),txn.getTransactionStatus(),SharedResource.DEFAULT_MAX_WAIT_TIME)
                if depends != 0 and depends != ABORTED:                 # +3 (nesting = 2) +1
                    raise RollbackException()
            except InterruptedException as ie:                          # +3 (nesting = 2)
                raise PersistitInterruptedException(ie)

        except InterruptedException as ie:                              # +2 (nesting = 1)
            raise PersistitInterruptedException(ie)
                                                                        # Cognitive Complexity = 35
                
def toRegexp(antPattern, directorySeparator) :
    escapedDirectorySeparator = '\\' + directorySeparator
    sb = StringBuilder(antPattern.length())
    sb.append('^')
    i = 1 if antPattern.startsWith("/") or antPattern.startsWith("\\") else 0           # +1 +1
    while i < antPattern.length() :                                                     # +1
        ch = antPattern.charAt(i)
        if SPECIAL_CHARS.indexOf(ch) != -1 :                                            # +2 (nesting = 1)
            sb.append('\\').append(ch)
        elif (ch == '*') :                                                              # +1
            if i + 1 < antPattern.length() and antPattern.charAt(i + 1) == '*' :        # +3 (nesting = 2) +1
                if i + 2 < antPattern.length() and isSlash(antPattern.charAt(i + 2)):   # +4 (nesting = 3) +1
                    sb.append("(?:.*").append(escapedDirectorySeparator).append("|)")
                    i += 2
                else :                                                                  # +1
                    sb.append(".*")
                    i += 1

            else :                                                                      # +1
                sb.append("[^").append(escapedDirectorySeparator).append("]*?")

        elif (ch == '?') :                                                              # +1
            sb.append("[^").append(escapedDirectorySeparator).append("]")
        elif (isSlash(ch)) :                                                            # +1
            sb.append(escapedDirectorySeparator)
        else :                                                                          # +1
            sb.append(ch)
    i+=1

    sb.append('$')
    return                                                                              # Cognitive Complexity = 20
