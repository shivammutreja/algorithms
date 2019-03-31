import time

def time_elapsed(func): 
        def calculate(*args, **kwargs): 
            start = time.time() 
            result = func(*args, **kwargs) 
            end = time.time() 
            print ('%r  %2.3f ms' %  
                    (func.__name__, (end - start) * 1000) 
                  ) 
            return result 
        return calculate

arr = [88,18,31,96,78,69,86,15,5,66,35,68,14,42,83,69,25,17,92,38,44,48,22,36,56,33,66,15,17,80]
