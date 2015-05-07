var express = require('express');
var child_process = require('child_process');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/volatility', function(req, res, next){
  var python = require('child_process').exec(
    'python python/vol.py',
    function (error, stdout, stderr) {
      res.json({vol: stdout});
      console.log('stdout: ' + stdout);
      console.log('stderr: ' + stderr);
      if (error !== null) {
        console.log('exec error: ' + error);
      }
    }
  );
});
module.exports = router;
