# Executes a command of terminating
exec { 'pkill killmenow':
  path => '/usr/bin:/usr/sbin:/bin'
}
