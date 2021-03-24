const express = require('express');
const app = express();



module.exports = (req, res) => {
    res.json({
      body: req.body,
      query: req.query,
      cookies: req.cookies,
    })
  }
