class Config(dict):
    schema = {
        'type':'dict',
        'non_empty':True,
        'content':{
            'players':{
                'type':'list',
                'non_empty':True,
                'content':{
                    'type':'dict',
                    'content':{
                        'name':{
                            'type':'string'
                        },
                        'deck':{
                            'type':'list',
                            'content':{
                                'type':'string'
                            }
                        }
                    }
                }
            }
        }
    }
    
    def _validate_node(self,node,schema):
        if schema['type']=='list':
            if schema.get('non_empty',False) and not node: return False
            for elem in node:
                if not self._validate_node(elem,schema['content']): return False
        if schema['type']=='dict':
            if schema.get('non_empty',False) and not node: return False
            for key,value in schema['content'].iteritems():
                if not isinstance(node,dict) or key not in node.keys() or not self._validate_node(node[key],value): return False
        if schema['type']=='string':
            return isinstance(node,str)
        if schema['type']=='int':
            return isinstance(node,int)
        if schema['type']=='float':
            return isinstance(node,float)
        return True
    
    def self_validate(self):
        return self._validate_node(self,Config.schema)
    
class Game(object):
    def __init__(self,config):
        assert config.self_validate(), "Invalid Config"
        self.config = config
        self.setup()
    
    def step(self):
        pass
    def setup(self):
        pass
    def start(self):
        pass
    def get_next_player(self):
        pass
    
class Player(object):
    def __init__(self):
        pass

class Game1(Game):
    def setup(self):
        self.curr_player = 0
        self.next_player = self.curr_player+1


cdict = {
'players':[{'name':'p1','deck':['c1','c2']},{'name':'p2','deck':['c3']}]
}
c = Config(cdict)

c.self_validate()

g = Game(c)