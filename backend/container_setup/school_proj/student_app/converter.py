class IntOrStrConverter:
    regex = '[0-9]*[a-zA-Z]*'
        
    def to_python(self,val):
        if val.isdigit():
            return int(val)
        else:
            return str(val)   
    def to_url(self,val):
        return str(val)