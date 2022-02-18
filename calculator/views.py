import math
from django.shortcuts import render

# Create your views here.
def calculator_action(request):
    if request.method == 'GET':
        context = initial_context()
        return render(request, 'calculator/calculator.html', context)
    try:
        inputs = process_parameters(request.POST)
        if 'digit' in inputs:
            context = process_digit(inputs)
        else:
            context = process_operation(inputs)
        return render(request,'calculator/calculator.html',context)
    except Exception as e:
        return render(request, 'calculator/error.html',{'error': str(e)})

# Initialize the content of the calculator
def initial_context():
    print('run initials')
    
    context = {}
    top = ""
    middle = ""
    bottom = "0"
    
    context['output'] = bottom
    context['top'] = top
    context['middle'] = middle
    context['bottom'] = bottom
    context['entering'] = 'true'
    return context;

# method that find the input is a digit or operation

def process_parameters(request):
    inputs = {}
    value = request['button']
    bottom = request['bottom']
    top = request['top']
    middle = request['middle']
    entering = request['entering']

    if(check_malForm(entering, top, middle, bottom)):
        top = ''
        middle = ''
        bottom = '0'
        entering = 'true'
        raise Exception("input being malformed!")
    else:
        if(len(value) > 1):
            inputs["operation"] = value
        else:
            inputs["digit"] = value
   
    inputs['top'] = top
    inputs['bottom'] = bottom
    inputs['middle'] = middle
    inputs['entering'] = entering

    return inputs


def process_digit(inputs):
    print(inputs)
    context = {}
    digit = inputs['digit']
    top = inputs['top']
    middle = inputs['middle']
    bottom = inputs['bottom']
    entering = inputs['entering']

    if(entering == 'true'):
        bottom = bottom + digit
    else:
        if(check_full_stack(top,middle,bottom)):
            top = ''
            bottom = '0'
            middle = ''
            entering = 'true'
            raise Exception("Stack Overflow!")
        else:
            top = str(middle)
            middle = str(bottom)
            bottom = '0'
            entering = 'true'

            bottom = digit
    
    context['top'] = top
    context['middle'] = middle
    context['output'] = int(bottom)
    context['bottom'] = int(bottom)
    context['entering'] = entering

    return context

def process_operation(inputs):
    print(inputs)
    context = {}

    op = inputs['operation']
    top = inputs['top']
    middle = inputs['middle']
    bottom = inputs['bottom']
    entering = inputs['entering']

    # push the number to output
    if(op == "push"):
        if(check_full_stack(top, middle, bottom)):
            top = ''
            bottom = '0'
            middle = ''
            entering = 'true'
            raise Exception("Stack Overflow!")
        else:
            top = str(middle)
            middle = str(bottom)
            bottom = str(0)
        
        context['output'] = bottom
        context['top'] = top
        context['middle'] = middle
        context['bottom'] = bottom
        context['entering'] = entering
        return context
    
    # check for underflow
    if(check_under_flow(middle)):
        top = ''
        bottom = '0'
        middle = ''
        entering = 'true'
        raise Exception("Stack Underflow!")
    else:
        if(op == 'plus'):
            bottom = str(int(middle) + int(bottom))
            middle = str(top)
            top = ""
            entering = False
        if(op=="minus"):
            bottom = str(int(middle) - int(bottom))
            middle = str(top)
            top = ""
            entering = False
        if(op=="times"):
           bottom = str(int(middle) * int(bottom))
           middle = str(top)
           top = ""
           entering = False
        if(op=='divide'):
            if(bottom =='0'):
                top = ''
                middle = ''
                bottom ='0'
                entering = 'true'
                raise Exception("Divide by zero!")
            bottom = math.floor(int(middle)/int(bottom))
            middle = str(top)
            top = ''
            entering = False

    context['output'] = bottom
    context['entering'] = entering
    context['bottom'] = bottom
    context['top'] = top
    context['middle'] = middle
    return context

def check_under_flow(m):
    if(len(m) < 1):
        return True
    else:
        return False

def check_full_stack(top, mid, low):
    if(len(top) > 0 and len(mid) > 0 and len(low) > 0):
        return True
    else:
        return False

def check_malForm(entering, top, middle, bottom):
    if(len(entering) < 6):
        if(len(top) < 5 and len(middle) < 5 and len(bottom) < 5):
            return False
        else:
            return True
    else:
        return True

