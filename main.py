from GenericHandler import ExceptionHandler

@ExceptionHandler.handler
def test():
  return 5 / 0

test()
