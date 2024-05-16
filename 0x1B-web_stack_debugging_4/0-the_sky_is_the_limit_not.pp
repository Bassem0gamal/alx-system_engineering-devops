# Increases the amount of traffix that Nginx can handle

exec {'replace':
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx',
  before   => Exec['restart'],
}

exec {'restart':
  command  => 'sudo service nginx restart',
}
    