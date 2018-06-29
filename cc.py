'''
@author: Simone Papandrea
'''

import redbaron

redbaron.ipython_behavior = False

class CognitiveComplexity(object):
    
    def evaluate(self,filename):
        '''
        Calcola la Complessità Cognitiva per tutte le funzioni ed i metodi definiri nel file.
        - filename: file python da parsare
        -> torna un dizionario { 'nomeFunzione': cc, 'nomeClasse.nomeMetodo': cc }
        '''
        fns=dict()
        with open(filename) as file:
            red = redbaron.RedBaron(file.read())
            # trova tutti i metodi delle classi
            for cls in red.find_all("ClassNode"):
                for fn in cls.find_all("DefNode"):
                    #if not fn.parent_find("DefNode"): # FIXME: necessario?
                    cc= self.__sequences(fn)+self.__conditions(fn)+ self.__structures(fn)
                    fns[cls.name + '.' + fn.name]=cc

            # trova tutte le funzioni
            for fn in red.find_all("DefNode"):
                #if not fn.parent_find("DefNode"): # FIXME: necessario?
                    cc= self.__sequences(fn)+self.__conditions(fn)+ self.__structures(fn)
                    fns[fn.name]=cc
        return fns
        
    def __sequences(self,func):
        cc=0
        last=None  
        for node in func.find_all("BooleanOperatorNode" ):            
            if last is None or node.value !=last.value or node.parent_find(last) is None:
                cc+=1
            
            if 'not' in [node.value for node in node.find_all("UnitaryOperatorNode")]:
                cc+=1
                
            last=node
        return cc
  
    def __conditions(self,func):
        return len(func.find_all("ElifNode")) + len(func.find_all("ElseNode"))
        
    def __structures(self,func):            
            
        increments= {"IfNode","TernaryOperatorNode","ComprehensionIfNode","ForNode","ComprehensionLoopNode",
                    "WhileNode","ExceptNode"}
        levels=increments.union({"ElseNode","ElifNode","DefNode","LambdaNode"})
        nodes=list()
        
        for node in increments:
            nodes.extend(func.find_all(node))
            
        cc=0
        for node in nodes:
            node=node.parent
            while node!=func.parent:
                name=node.__class__.__name__
                if name in levels and (name!='DefNode' or not self.__is_decorator(node)):
                    cc+=1
                node=node.parent
        return cc     
         
    def __is_decorator(self,func):
        values=[node.__class__.__name__ for node in func.value 
                                        if node.__class__.__name__ not in ['CommentNode','EndlNode']]                
        return len(values)==2 and values[0]=='DefNode' and values[1]=='ReturnNode'

if __name__ == '__main__':    
    import sys
    file=r"test.py" if len(sys.argv) != 2 else sys.argv[1]
    cc=CognitiveComplexity()
    results=cc.evaluate(file)
    for name,cc in results.items():
        print('{} : {}'.format(name,cc))
