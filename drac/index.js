node_ssh = require('node-ssh')
ssh = new node_ssh()
 
ssh.connect({
  host: '185.53.160.137',
  username: 'root',
  password: 'T5n1iCoIgS!0k3u22&21'
})
/*
 Or
 ssh.connect({
   host: 'localhost',
   username: 'steel',
   privateKey: fs.readFileSync('/home/steel/.ssh/id_rsa')
 })
 if you want to use the raw string as private key
 */
.then(function() {
ssh.execCommand('racadm serveraction powerstatus').then(function(result) {
    console.log('status: \n' + result.stdout)
  })


});
