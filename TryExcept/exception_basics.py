try:
        num = int(num)
        result = 10 / num
        # if num < 0:
        #     raise Exception("Must be a positive number")
except ValueError:
        print("Not a number")
except ZeroDivisionError:
        print("Cannot be 0 -- choose another number")
finally:
        print("End test.")
    

    
