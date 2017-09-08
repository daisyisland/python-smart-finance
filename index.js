
Meteor.call('azurecnt', function(){
    console.log('call method sucessed')
})

var bodyx = {
                "Inputs": {
                    "input1": {
                    "ColumnNames": [
                        "age",
                        "workclass",
                        "fnlwgt",
                        "education",
                        "education-num",
                        "marital-status",
                        "occupation",
                        "relationship",
                        "race",
                        "sex",
                        "capital-gain",
                        "capital-loss",
                        "hours-per-week",
                        "native-country"
                    ],
                    "Values": [
                        [
                        "39",
                        "State-gov",
                        "77516",
                        "Bachelors",
                        "13",
                        "Never-married",
                        "Adm-clerical",
                        "Not-in-family",
                        "White",
                        "Male",
                        "2174",
                        "0",
                        "40",
                        "United-States"
                        ]
                    ]
                    }
                },
                "GlobalParameters": {}
            };