//jshint esversion : 6
const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.json([{
      'name' : 'bob',
      'email' : 'bob@gmail.com',
      'message': 'Hello World!'
    },
    {
        'name' : 'alice',
        'email' : 'alice@gmail.com',
        'message': 'Hello World!'     
    },
    {
        'name' : 'jake',
        'email' : 'jake@gmail.com',
        'message': 'Hello World!'     
    },
    {
        'name' : 'gody',
        'email' : 'gody@gmail.com',
        'message': 'Hello World!'     
    },
    
])
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})