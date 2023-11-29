# Setting up my client config file
include stdlib

file_line { 'Turn off passwd auth':
  ensure  => present,
  path    => '~/.ssh/school',
  line    => '    PasswordAuthentication no',
  replace => true,
}

file_line { 'Delare identity file':
  ensure  => present,
  path    => '~/.ssh/school',
  line    => '     IdentityFile ~/.ssh/school',
  replace => true,
}
