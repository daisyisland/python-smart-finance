import { Meteor } from 'meteor/meteor';
Meteor.methods({
        azurecnt: function(){
            var PythonShell = require('python-shell');
            var pyshell = new PythonShell('c:/Users/10025/Desktop/smart-finance/smart-finance/server/azuretest.py');
            pyshell.on('message', function (message) {
            // received a message sent from the Python script (a simple "print" statement) 
            console.log(message);
            });
            const data = "39,State-gov,77516,Bachelors,13,Never-married,Adm-clerical, Not-in-family,White,Male,2174, 0,40,United-States"
            pyshell.send(data)
        
            pyshell.end(function(){
                console.log("python closed")
            })
        }
    })