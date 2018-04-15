'use strict';

const express = require('express');
const rp = require('request-promise');

// Constants
const PORT = 80;
const HOST = '0.0.0.0';

// App
const app = express();
// app.get('/', (req, res) => {
//   res.send('Hello world\n');
// });

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);

const name = "Allen"
let msgCount = 1

setInterval(()=>{
  var options = {
    uri: 'http://product-service',
    qs: {
        sender: name,
        message: 'I have sent ' + msgCount + ' message(s)',
    },
    headers: {
        'User-Agent': 'Request-Promise'
    },
    json: true
  };

  rp(options)
      .then(function (data) {
        msgCount++;
          console.log(data);
      })
      .catch(function (err) {
          // API call failed...
      });
},3000)
