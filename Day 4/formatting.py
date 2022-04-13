msg_template = """Hello {name}, 
Thank you for joining {website}, we are very happpy
to have you with us
"""
#.format(name= 'Ruby', webstite = 'samuelruby.com')

def format_msg(my_name = 'Ruby', my_website = 'samuelruby.com'):
    my_msg = msg_template.format(name = my_name, website = my_website)
    #print (my_msg)
    return my_msg