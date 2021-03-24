const express = require('express');
const app = express();



module.exports = function () {
    app.get('/', (req, res) => {
        res.send('Hello World!')
      })
}
