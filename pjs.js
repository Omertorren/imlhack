var webPage = require('webpage');
var fs = require('fs');

var path = 'output.txt';
var page = webPage.create();
page.open('http://www.israelhayom.com/site/today.php?id=3168', function (status) {
    fs.writeFile("test.txt",page.content, function(){})
});
