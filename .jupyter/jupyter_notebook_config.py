c.ServerProxy.servers = {
  'TimeSched': {
    'command': ['python3', '-m', 'http.server', '{port}', '--directory', '.'],
    'absolute_url': False
  }
}
