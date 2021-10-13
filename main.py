import socket


import config




# the bot identifying itself

class Bot:
  def __init__(self):
    self.irc_server = 'irc.twitch.tv'
    self.irc_port = 6667
    self.oauth_token = config.TWITCH_TOKEN
    self.username = 'snugbottv'
    self.channels = ['RealSkybreon']

  def send_privmsg(self, channel, text):
    self.send_command(f'PRIVMSG #{channel} :{text}')

  def send_command(self, command):
    if 'PASS' not in command:
      print(f'<{command}')
    self.irc.send((command + '\r\n').encode())
  

  def connect(self):
    self.irc = socket.socket()
    self.irc.connect((self.irc_server, self.irc_port))
    self.send_command(f'PASS {self.oauth_token}')
    self.send_command(f'NICK {self.username}')
    for channel in self.channels:
      self.send_command(f'JOIN #{channel}')
      self.send_privmsg(channel, 'I AM HERE!')
    self.loop_for_messages()

  def loop_for_messages