def fib2(delim):
    # Check if the value is numeric and positive
    if type(delim) != int:
        raise TypeError("Value needs to be an Integer")
    if delim < 0:
        raise ValueError("Value needs to be greater than 0")
    
    fib_series = [1,1]
    # Create an empty list to append all the 
    for i in range(2,delim):
        fib_series.append(fib_series[i - 1] + fib_series[i - 2] )
        
    return fib_series