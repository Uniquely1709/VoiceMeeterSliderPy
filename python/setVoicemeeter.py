import voicemeeter

# Can be 'basic', 'banana' or 'potato'
kind = 'potato'

# Ensure that Voicemeeter is launched
# voicemeeter.launch(kind)

with voicemeeter.remote(kind) as vmr:
  # Set the mapping of the second input strip
  vmr.inputs[1].A4 = False
  vmr.inputs[0].gain = -5.0