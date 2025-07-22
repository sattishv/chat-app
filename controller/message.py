

# Message web controller

class message_web_controller(object):
  """Initiailize message_web_controller"""
  def __init__(self):
    pass

  # Http Get processor
  def get(self,*args,**kwargs)
    if self.request=="/messages/send":
     return render_template('messages/send.html', var=self.var)
    elif self.request=="/messages": 
     return render_template('messages/list.html', var=self.var)
 
