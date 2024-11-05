# Make a new file named update_hr_doc.py. You are starting with a list extracted from 
# an employee database, in the form of a list of tuples: 

# hr_list = [('0123', 'HR', 'Rebecca Yang', '69000'), ('0121', 'IT', 'Mark Blick', '67000'), 
# ('0068', 'IT', 'Kahna Larsen', '112000'), ('0234', 'OPS', 'Jim Smith', '54000')] 
# 2. For the contents of this list: 
# ∗ Mark just reported a name change. Update Mark’s last name to Blick-Hawley. 
# ∗ Jim has accepted a new account manager role in another department. Change Jim’s 
# department code from OPS to CS and update his salary to 60000. 
# 3. Display the updated contents on multiple lines in the following format, using the pipe 
# symbol | to separate each value and formatting the salary to use a comma: 
# Employee# | DeptCode | Name | NN,NNN 
# ∗ Formatting that last value can be deceptively tricky! Consider that you might have to 
# cast it as another data type when using the format function… 

hr_list = [('0123', 'HR', 'Rebecca Yang', '69000'), ('0121', 'IT', 'Mark Blick', '67000'), 
('0068', 'IT', 'Kahna Larsen', '112000'), ('0234', 'OPS', 'Jim Smith', '54000')] 

Rebecca,Mark,Kahna,Jim= hr_list
num1=Mark[0]
num2=Mark[1]  
num3=Mark[2]   
print(num3)
num3.replace("Blick", "Blick-Hawley")
print(num3)

