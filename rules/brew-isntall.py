def match(command, settings):
    return ('unknown command: isntall' in command.stderr.lower())

def replace_if_needed(s):
  if s.find('isntall') != -1:
    return 'install'
  else:
    return s

def get_new_command(command, settings):
    split = command.script.split(' ')
    after = map(replace_if_needed, split)
    return ' '.join(after)
